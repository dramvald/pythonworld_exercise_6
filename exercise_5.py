# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый
# год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на
# них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая
# будет на счету пользователя.

def bank(a, years):
    i = 0
    print("Внесено средств: "+str(a)+"р., сроком на "+str(years)+" лет")
    while i < years:

        i += 1
        a = a + ((a / 100) * 10)
        # print("Год " + str(i))
        # print("Размер вклада " + str(a))
    print("Сумма на счете, по окончанию " + str(i)+" лет: "+str(a)+'р.')


sum_ = int(input("Введите вносимую сумму "))
years_ = int(input("На какой срок хотите положить "))
bank(sum_, years_)
