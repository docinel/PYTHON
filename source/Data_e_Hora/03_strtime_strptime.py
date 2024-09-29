from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-09-30 12:30:00"
mascara_ptbr = "%d/%m/%Y %H:%M:%S"
mascara_eua = "%m/%d/%Y %I:%M:%S %p"

print(data_hora_atual.strftime(mascara_ptbr))
print(data_hora_atual.strftime(mascara_eua))
