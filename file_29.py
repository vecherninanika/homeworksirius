from datetime import timedelta
from datetime import date

def func(notes, date):
    file = open ('file_2809', 'a')
    for i in notes:
        file.write(str(date) + '\n')
        date += timedelta(days=1)
        file.write(i)
    file.close()

notes_1 = ['Es dia uno de nuestro viaje\n', 'Ya estamos muy lejos de Daidu\n', 'LLegamos a Koryo en dos dias\n']
date_1 = date(2022, 5, 18)

func(notes_1, date_1)

