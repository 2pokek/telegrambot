# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.
import os

with open('txtx.txt', 'w') as a:
    a.write('tx\n')
    a.write('1337')
    a.write('txxxxxx\n')
    a.write('www')
a = open('txtx.txt', 'r')
print('колво строк: ', len(a.readline()))
a.close()
a = open('txtx.txt', 'r')
for i in a.readlines():
    print('elements: ', len(i) - 1)
a.close()
