#Выведите общее время звучания всех песен.
#Создайте список песен, время звучаниях которых больше 5 минут
#Создайте новый словарь тех песен, в название которых состоит из одного слова
songsdict = {'World in My Eyes': 4.76,'Sweetest Perfection': 5.43,'Personal Jesus': 4.56,'Halo': 4.30,'Waiting for the Night': 6.07,'Enjoy the Silence': 4.6,'Policy of Truth': 4.88,'Blue Dress': 4.18,'Clean': 5.68}
a=sum(songsdict.values())
b=[]
v={}
for key,values in songsdict.items():
    if values>5:
        c=key
        b.append(c)
    else:
        continue
for key,values in  songsdict.items():
    if ' ' in key:
        continue
    else:
        v[key]=values




print(v)
print(b)
print(a)