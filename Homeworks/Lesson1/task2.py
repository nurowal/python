""" 2.Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
    Используйте форматирование строк."""
TimeSeconds = int(input('Введите время в секундах :'))
hours = TimeSeconds//3600
minutes = (TimeSeconds-hours*3600)//60
seconds = TimeSeconds-hours*3600-minutes*60
if len(str(hours)) == 1:
    hours_str = '0'+str(hours)
else:
    hours_str = str(hours)
if len(str(minutes)) == 1:
    minutes_str = '0'+str(minutes)
else:
    minutes_str = str(minutes)
if len(str(seconds)) == 1:
    seconds_str = '0'+str(seconds)
else:
    seconds_str = str(seconds)
print(f'{hours_str}:{minutes_str}:{seconds_str}')