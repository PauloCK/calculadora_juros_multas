# Título do PR

## Descrição

Adiciona o campo `abcd` à tabela `efgh`.

**OBS: aprovar [este](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gettyimages.com.br%2Ffotos%2From%25C3%25A1rio&psig=AOvVaw0XKZnER9PD3h0MdFRAVc-Y&ust=1685802285565000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMCDuIblpP8CFQAAAAAdAAAAABAD) PR antes**

## Tipo de Mudança

- [ ] Criação de Tabela
- [ ] Inclusão de Coluna
- [ ] Correção de Cálculo de Coluna
- [ ] Troca de Nome de Coluna
- [ ] Anonimização de Colunas

## Verificar:

- [ ] Nomes das colunas em inglês
- [ ] Snake case
- [ ] Troca de valores em branco por NULL
- [ ] Todos os alias são definidos usando AS ou todos os alias são definidos sem usar AS
- [ ] Nomes de funções e SELECT, FROM, etc. tudo em upper case ou tudo em lower case
- [ ] Particionamento, cluster e upsert_columns caso a tabela consuma mais de 5GB
- [ ] Está especificado de qual tabela cada campo vem se estiver usando JOIN
- [ ] Nomes descritivos de subqueries
- [ ] Sem comentários desnecessários