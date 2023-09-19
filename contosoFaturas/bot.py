
from botcity.core import DesktopBot
from botcity.maestro import *


def not_found(label):
    print(f"Element not found: {label}")



def cadastraFaturas():

    bot = DesktopBot()
    path_app = r"C:\Program Files (x86)\Contoso, Inc\Contoso Invoicing\LegacyInvoicingApp.exe"
    bot.execute(path_app)
    bot.wait(2000)
    bot.maximize_window()
    bot.wait(1000)
    
    if not bot.find( "invoices", matching=0.97, waiting_time=10000):
        not_found("invoices")
    bot.click()
    
    if not bot.find( "novo_registro", matching=0.97, waiting_time=10000):
        not_found("novo_registro")
    bot.click()
    
    
    


cadastraFaturas()




