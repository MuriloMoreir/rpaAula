from datetime import datetime


# Obter a data e hora atual
dataAtual = datetime.now()

# Convertendo para String
dataConvertida = dataAtual.strftime('%Y-%m-%d')
horaAtual = dataAtual.strftime('%H:%M:%S')

print('Data atual: ', dataConvertida)
print('Hora atual: ', horaAtual)
print('Data atual: ', dataConvertida)
print('Hora atual: ', horaAtual)
