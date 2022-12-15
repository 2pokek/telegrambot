import sqlite3

listik = [1, 2, 3, 'pew', 'curs', 'prog']
conn = sqlite3.connect("db.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT,col_1 INTEGER)''')

for i in listik:
    if type(i) == str:
        b = len(i)
        cursor.execute('''INSERT INTO tab_1(col_1)VALUES(?)''', (i,))
        cursor.execute('''INSERT INTO tab_2(col_1)VALUES(?)''', (int(b),))
        conn.commit()
    elif type(i) == int:
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab_2(col_1)VALUES(?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT INTO tab_1(col_1)VALUES('нечетное')''')
            conn.commit()
cursor.execute('''SELECT COUNT(*) as count FROM (tab_2)''')
p = cursor.fetchall()
if p[0][0]<=5:
    cursor.execute('''UPDATE tab_1 SET col_1='hello' WHERE id=1''')
else:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
cursor.execute('''SELECT col_1 FROM tab_2''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT col_1 from tab_1''')
c=cursor.fetchall()
print(c)
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»
