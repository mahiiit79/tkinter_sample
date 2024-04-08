import mysql.connector as mysql


def connect():
        database = mysql.connect(
            host = "localhost",
            user = "root",
            password="root123",
            database="market"
        )
        cursor = database.cursor()
        return database,cursor


def disconnect(db,cursor):
    db.close()
    cursor.close()


def save (name,model,count,price,serial,is_available):
    db,cursor = connect()
    sql_command = "INSERT INTO stuff (name,model,serial,count,price,is_available) VALUES (%s,%s,%s,%s,%s,%s)"
    data = [name,model,count,price,serial,is_available]
    cursor.execute(sql_command,data)
    db.commit()
    disconnect(cursor,db)


def edit(code,name,serial,model,count,price,is_available):
    db,cursor = connect()
    sql_command = "UPDATE stuff SET name =%s,serial = %s,model=%s,count=%s,price=%s,is_available = %s WHERE code=%s"
    data = [name,serial,model,count,price,is_available,code]
    cursor.execute(sql_command,data)
    db.commit()
    disconnect(cursor,db)


def remove(code):
    db,cursor= connect()
    sql_command ="DELETE FROM stuff WHERE code=%s "
    data = [code]
    cursor.execute(sql_command, data)
    db.commit()
    disconnect(db,cursor)


def  find_all():
    db,cursor = connect()
    sql_command = "SELECT * FROM stuff "
    cursor.execute(sql_command)
    stuff_list = cursor.fetchall()
    disconnect(db,cursor)
    return stuff_list if stuff_list else None


def find_by_code(code):
    db,cursor = connect()
    sql_command ="SELECT * FROM stuff WHERE code =%s"
    cursor.execute(sql_command,[code])
    stuff = cursor.fetchone()
    disconnect(db,cursor)
    return stuff if stuff else None


def find_by_name(name):
    db,cursor = connect()
    sql_command = "SELECT * FROM stuff WHERE name like %s"
    cursor.execute(sql_command,[name])
    stuff_list = cursor.fetchall()
    disconnect(db,cursor)
    return stuff_list if stuff_list else None

def find_by_count(count):
    db,cursor = connect()
    sql_command = "SELECT * FROM stuff WHERE count like %s"
    cursor.execute(sql_command,[count])
    stuff_list = cursor.fetchall()
    disconnect(db,cursor)
    return stuff_list if stuff_list else None

def find_by_price(min_price, max_price):
    db,cursor=connect()
    sql_command = "SELECT * FROM stuff WHERE price between %s AND %s"
    cursor.execute(sql_command,[min_price,max_price])
    stuff_list = cursor.fetchall()
    print(stuff_list)
    disconnect(db,cursor)
    return stuff_list if stuff_list else None


