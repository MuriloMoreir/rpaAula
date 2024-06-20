from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import pandas as pd


# Obter a data e hora atual
dataAtual = datetime.now()

# Convertendo para String
dataConvertida = dataAtual.strftime('%Y-%m-%d %H:%M:%S')

print('Data e Hora atual: ', dataConvertida)

# Entrando no site
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options = chrome_options)

driver.get("https://www.google.com.br/search?q=d%C3%B3lar&sca_esv=e538a6082b46d93a&sca_upv=1&hl=pt-BR&sxsrf=ADLYWIIn2256gESQaJCnxeEcPG76Z9VcgA%3A1718852130869&source=hp&ei=IppzZrnVMpOv1sQP4tKk2Ac&iflsig=AL9hbdgAAAAAZnOoMiGVZGuEFKDBshlJMQ4RYH1aHkhW&ved=0ahUKEwi57reVl-mGAxWTl5UCHWIpCXsQ4dUDCBU&uact=5&oq=d%C3%B3lar&gs_lp=Egdnd3Mtd2l6IgZkw7NsYXIyDxAjGIAEGCcYigUYRhiCAjILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDAUjeBlAAWKYEcAB4AJABAJgBbqABgwSqAQMxLjS4AQPIAQD4AQGYAgWgApEEwgIKECMYgAQYJxiKBcICDhAuGIAEGLEDGIMBGIoFwgIREC4YgAQYsQMY0QMYgwEYxwHCAgsQLhiABBjRAxjHAZgDAJIHAzEuNKAHyyo&sclient=gws-wiz")
sleep(2)

# Pegando o valor do dólar
dolar = driver.find_element(By.CSS_SELECTOR, ('.DFlfde.SwHCTb'))
dolar_site = dolar.text
dolar_site = float(dolar_site.replace(",","."))
print('Dólar: ', dolar_site)
