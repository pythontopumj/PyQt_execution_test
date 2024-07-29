import pymysql

conn = pymysql.connect(host='localhost', user='root',password='root', db='bookdb', charset='utf8')
curs = conn.cursor()




def alloutput():
    sql = "SELECT * FROM newbook"
    curs.execute(sql)
    result=curs.fetchall()
    result_return=""
    for i in result:
        result_return+=str(i)
        result_return+="\n"   
    return result_return
    
def search(input):
    sql = "SELECT * FROM newbook WHERE bookname like'%{}%'".format(input)
    curs.execute(sql)
    result=curs.fetchall()
    result_return=""
    for i in result:
        result_return+=str(i)
        result_return+="\n"   
    return result_return

def add(input):
    sql = "INSERT INTO newbook VALUES('{}'})".format(input)
    curs.execute(sql)
    conn.commit()

def modify(input,input2):
    sql = "UPDATE FROM newbook SET pname='{}' WHERE bookname='{}'".format(input,input2)
    curs.execute(sql)
    conn.commit()

def delete(input):
    sql = "DELETE FROM newbook WHERE bookname LIKE'{}''".format(input)
    curs.execute(sql)
    conn.commit()