# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.
f=open('r.txt','r')
print('Количество строк:',len(f.readlines()))
f.close()

f=open('r.txt','r')

for i in f.readlines():
    print('Элементов в строке:',len(i)-1)
f.close()