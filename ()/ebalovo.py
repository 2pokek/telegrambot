#Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.
a=input('Введите слово: gJbJHjJ')
b=['e','y','u','i','o','a','E','Y','U','I','O','A']
c=0
d=0
v=0
g=0
y=0
z=0
for i in a:
    if i.isupper()==True:
        c += 1
        d = d * 0
        if c // 2 != 0:
           v+=1
    else:
        d += 1
        c = c * 0
        if d // 2 != 0:
            g+=1
for p in a:
    if b.count(p):
        y+=1
    else:
        z+=1
print(v)
print(g)
print(len(a))
print(y)
print(z)