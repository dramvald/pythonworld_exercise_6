# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и
# возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).


def season(x):
    months = {1: 'зима',
              2: 'зима',
              3: 'весна',
              4: 'весна',
              5: 'весна',
              6: 'лето',
              7: 'лето',
              8: 'лето',
              9: 'осень',
              10: 'осень',
              11: 'осень',
              12: 'зима'}
    if x in months:
        print(months[x])
    else:
        print('Не парвильно введен месяц')


season(int(input('Введиет номер месяца ')))
