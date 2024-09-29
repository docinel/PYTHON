import pytz
from datetime import datetime

data_hora = datetime.now(pytz.timezone('America/Sao_Paulo'))
print(data_hora)