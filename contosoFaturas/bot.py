

from botcity.core import DesktopBot
from botcity.maestro import *
import pandas as pd


def not_found(label):
    print(f"Element not found: {label}")


dados = pd.read_excel(r"C:\temp\Python\automacaoDesktop\files\Contoso+Coffee+Shop+Invoices.xlsx")
#print(dados)

bot = DesktopBot()
path_app = r"C:\Program Files (x86)\Contoso, Inc\Contoso Invoicing\LegacyInvoicingApp.exe"
bot.execute(path_app)
bot.wait(3000)

bot.maximize_window()
bot.wait(1000)

if not bot.find("invoices", matching=0.97, waiting_time=10000):
    not_found("invoices")
bot.click()


def cadastraFaturas(data, conta, contato, valor, status):

    if not bot.find( "novo_registro", matching=0.97, waiting_time=10000):
        not_found("novo_registro")
    bot.click()
    
    if not bot.find( "date", matching=0.97, waiting_time=10000):
        not_found("date")
    bot.click_relative(81, 3)
    bot.type_keys(['ctrl', 'a'])
    bot.paste(data)

    bot.tab()
    bot.paste(conta)
    bot.tab()
    bot.paste(contato)
    bot.tab()
    bot.paste(valor)

    coluna = status


    if not bot.find( "status_inicio", matching=0.97, waiting_time=10000):
        not_found("status_inicio")
    bot.click_relative(57, 5)

    if coluna == "Uninvoiced":
        if not bot.find( "uninvoiced", matching=0.97, waiting_time=10000):
            not_found("uninvoiced")
        bot.click_relative(81, 29)

    elif coluna == "Invoiced":
        if not bot.find( "invoiced", matching=0.97, waiting_time=10000):
            not_found("invoiced")
        bot.click_relative(75, 47)
    else:
        if not bot.find( "paid", matching=0.97, waiting_time=10000):
            not_found("paid")
        bot.click_relative(66, 71)
        
    if not bot.find( "salvar", matching=0.97, waiting_time=10000):
        not_found("salvar")
    bot.click()
    
    
    
    
    
    
for coluna in dados.itertuples():
    cadastraFaturas(str(coluna[1]), str(coluna[2]), str(coluna[3]), str(coluna[4]), str(coluna[5]))

bot.alt_f4()





