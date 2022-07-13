import pandas as pd
from twilio.rest import Client

# Para enviar os nomes dos vendedores que bateram a meta de vendas por SMS, descomente a linha a seguir e insira sua conta SID do twilio.com/console.
#account_sid = "###########"
# Descomente as linha abaixo e insira seu Token do twilio.com/console:
#auth_token  = "#####"
#client = Client(account_sid, auth_token)

# Abrir as seis planilhas de vendas:
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #Se as planilhas não estiverem na mesma pasta que o arquivo main.py, inserir o caminho completo na linha acima.

    # Criar um dataframe apenas com os vendedores que bateram a meta em cada mês:
    if (tabela_vendas['Vendas'] > 55000).any():
        bonus_df = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000]
        # Mudar o index das linhas para começar a contar do zero novamente:
        bonus_df.reset_index(drop=True, inplace=True)

        # Imprimir o nome, a venda e o mês de cada vendedor:
        for i in bonus_df.index:
            vendedor = bonus_df.iloc[i,0]
            vendas = bonus_df.iloc[i,1]
            print(f'O(a) vendedor(a) {vendedor} bateu a meta com R${vendas},00 em vendas em {mes}')

        # Para enviar o SMS, descomente as linhas abaixo e preencha o seu número Twilio (from) e o número recipiente (to)
#        message = client.messages.create(
#            to="+5511967679570",
#            from_="++17627603382",
#            body=f'O(a) vendedor(a) {vendedor} bateu a meta com R${vendas},00 em vendas no mês de {mes}.')
#        print(message.sid)