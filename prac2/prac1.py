
a = {'торт': ['тесто,яйцо,сахар,молоко', 200, 1000], 'пироженое': ['тесто,старое пироженое,сахар', 100, 3000],
     'маффин': ['я, ебу', 120, 5000]}
pr1=0
while True:
    k=input()
    if k == 'o':
        for key, values in a.items():
            print(key, values[0])
    elif k == 'p':
        for key, values in a.items():
            print(key, values[1])
    elif k == 'd':
        for key, values in a.items():
            print(key, values[2])
    elif k == 'a':
        for key, values in a.items():
            print(key, 'состав', values[0], key, 'цена', values[1], key, 'колво', values[2])
    elif k == 'b':
        m=input('name: ')
        n=int(input('how much: '))
        for key,values in a.items():
            if m == key and n<=values[2]:
                pr1 = pr1 + (n / 100) * values[1]
                a[m][2]-=n
                print('task completed: ', pr1)
            else:
                continue
    elif k == 'n':

        print('that would be: ' ,pr1)
        for key,values in a.items():
            if values[1] != 0:
                print(key , values[1])
        print('see u')
        break



