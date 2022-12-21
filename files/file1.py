#Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность
with open('input.txt', 'w') as i:
    i.write('4 3')
with open ('input.txt', 'r') as i:
    x=i.readline().split()
    y = int(x[0]) - int (x[1])
with open('output.txt','w')as k:
    k.write(str(y))
