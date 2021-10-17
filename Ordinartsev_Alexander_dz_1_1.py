# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


# input duration
while 1:
    duration = int(input('Введите продолжительность в секундах: '))
    if duration >= 0:
        break
    else:
        print('Пожалуйста, введите положительно число')

# view, depending on the duration condition
if 60 / duration > 1:  # until a minute: <s> сек
    print(duration, 'сек')
elif 3600 / duration > 1:  # until an hour: <m> мин <s> сек
    print(duration // 60, 'мин', (duration - (duration // 60) * 60), 'сек')
elif 86400 / duration > 1:  # until days: <h> час <m> мин <s> сек
    print(duration // 3600, 'час', (duration // 60) % 60, 'мин', (duration - (duration // 60) * 60), 'сек')
else:  # another conditions: <d> дн <h> час <m> мин <s> сек
    print(duration // 86400, 'дн', duration // 3600 - ((duration // 86400) * 24), 'час', (duration // 60) % 60, 'мин',
          (duration - (duration // 60) * 60), 'сек')
