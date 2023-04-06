from datetime import date
import requests

import pandas as pd
import streamlit as st

def create_selic_df():
    response = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json').json()
    
    selic_df = pd.DataFrame.from_records(response)
    selic_df['data'] = pd.to_datetime(selic_df['data'], format='%d/%m/%Y')
    selic_df['valor'] = selic_df['valor'].astype('float') / 100

    return selic_df


def recalculate_fine_price(due_date, payment_dt, original_value):
    acc_selic = selic_df[(selic_df['data'] > pd.to_datetime(due_date)) & \
                (selic_df['data'] < pd.to_datetime(payment_dt) - pd.offsets.MonthBegin(1))]['valor'].sum()
    
    return round(original_value*(acc_selic+1.01), 2)

def check_password():
    '''Returns `True` if the user had the correct password.'''

    def password_entered():
        '''Checks whether a password entered by the user is correct.'''
        if st.session_state['password'] == st.secrets['password']:
            st.session_state['password_correct'] = True
            del st.session_state['password']  # don't store password
        else:
            st.session_state['password_correct'] = False

    if 'password_correct' not in st.session_state:
        # First run, show input for password.
        st.text_input(
            'Password', type='password', on_change=password_entered, key='password'
        )
        return False
    elif not st.session_state['password_correct']:
        # Password not correct, show input + error.
        st.text_input(
            'Password', type='password', on_change=password_entered, key='password'
        )
        st.error('😕 Password incorrect')
        return False
    else:
        # Password correct.
        return True
    

valores_multas_df = pd.read_csv('valores_multas.csv')
selic_df = create_selic_df()

st.title('Calculadora de preço de multas com juros.')

if check_password():
    st.write('Informe a data de vencimento da multa, a data em que foi paga e seu valor tabelado nos campos abaixo.')

    multa = st.selectbox(
        label='Escolha a Multa',
        options=valores_multas_df['descricao']
    )
    preco_tabelado_multa = list(valores_multas_df[valores_multas_df['descricao'] == multa]['valor'])[0]
    st.write(f'O valor da multa escolhida é {preco_tabelado_multa}')
    # preco_tabelado_multa = st.number_input(label='Preço Tabelado da Multa') # TODO: Create function to get fines' prices by their name (?)
    data_vencimento = st.date_input(
        label='Data de Vencimento da Multa',
        value=date(2023,1,1)
    )
    data_pagamento_multa = st.date_input(label='Data de Pagamento da Multa')

    if st.button(label='Recalcular'):
        preco_recalculado_multa = recalculate_fine_price(
            due_date=data_vencimento,
            payment_dt=data_pagamento_multa,
            original_value=preco_tabelado_multa
        )
        st.markdown(f'### O valor da multa recalculado é {preco_recalculado_multa}')