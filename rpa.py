from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Obter a data e hora atual
dataAtual = datetime.now()

# Convertendo para String
dataConvertida = dataAtual.strftime('%Y-%m-%d')
horaAtual = dataAtual.strftime('%H:%M:%S')

print('Data atual: ', dataConvertida)
print('Hora atual: ', horaAtual)

# Entrando no site
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options = chrome_options)

driver.get("https://www.google.com.br/search?q=d%C3%B3lar")
sleep(2)

# Pegando o valor do dólar
dolar = driver.find_element(By.CSS_SELECTOR, ('.DFlfde.SwHCTb'))
dolar_site = dolar.text
dolar_site = float(dolar_site.replace(",","."))
print('Dólar: ', dolar_site)

# Fechando navegador
driver.quit()
