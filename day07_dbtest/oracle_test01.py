import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp")

# print(cursor)

for item in cursor:
    print(item[1],item[5])

conn.close()