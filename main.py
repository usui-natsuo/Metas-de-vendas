import pandas as pd
from twilio.rest import Client

# Informações de login Twilio (comentar o bloco abaixo caso não queira enviar SMS):
account_sid = input('Twilio account SID:')
auth_token = input('Twilio Token:')
client = Client(account_sid, auth_token)
sender = input('Send SMS from (Twilio Phone number):')
receiver = input('Send SMS to:')
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
            print(f'O(a) vendedor(a) {vendedor} bateu a meta com R${vendas:,.2f} em vendas em {mes}')

        # Enviar SMS:
        message = client.messages.create(
            to=receiver,
            from_=sender,
            body=f'O(a) vendedor(a) {vendedor} bateu a meta com R${vendas:,.2f} em vendas no mês de {mes}.')
        print(message.sid)