import mysql.connector


def connectToDB(dbname,password):
    user='root'
    host='localhost'
    password=password
    database=dbname

    conn=mysql.connector.connect(user=user,host=host,password=password,database=database,auth_plugin='mysql_native_password')
    return conn


def createTable(tablename,conn,column={}):
    if(len(column)==0):
        print("Invalid Input")
    else:
        create="CREATE TABLE "+ tablename +"("
        j=0
        for i in column:
            
            if(j<len(column)-1):
                create+=i + " " 
                create+=column[i]
                create+=','
            else:
                create+=i + " " 
                create+=column[i]
            j+=1
        create+=")"

        print(create)



def selectFromTable(tablename,conn,key='AND',attribute=[],where={}):
    if len(attribute)==0:
        users="SELECT * FROM "+tablename
    else:
        users="SELECT "
        for i in range(len(attribute)):
            if(i<len(attribute)-1):
                users+=attribute[i]
                users+=','
            else:
                users+=attribute[i]
        users+=" FROM "+tablename

    users+=' WHERE '
    if(len(where)>0):
        j=0
        for i in where:
            if(j<len(where)-1):
                users+="`"+i+"`"
                users+=" = '"
                users+=where[i]
                users+="' "+key+" "
            else:
                users+="`"+i+"`"
                users+=" = '"
                users+=where[i]
                users+="' "
            j+=1
    print(users)
    cursor = conn.cursor()
    cursor.execute(users)
    result=cursor.fetchall()
    for i in result:
        print(i)

def showTables(conn):
    show="SHOW TABLES"
    cursor = conn.cursor()
    cursor.execute(show)
    result=cursor.fetchall()
    return result

def updateTable(tablename,attribute,conn,where={},key=[]):
    update="UPDATE "+tablename+" SET "
    if(len(attribute)>0):
        j=0
        for i in attribute:
            if(j<len(attribute)-1):
                update+=i
                update+=" = '"
                update+=attribute[i]
                update+="' , "
            else:
                update+=i
                update+=" = '"
                update+=attribute[i]
                update+="' "
            j+=1
    update+='WHERE '
    if(len(where)>0):
        j=0
        for i in where:
            if(j<len(where)-1):
                update+="`"+i+"`"
                update+=" = '"
                update+=where[i]
                update+="' "+key+" "
            else:
                update+="`"+i+"`"
                update+=" = '"
                update+=where[i]
                update+="' "
            j+=1
    print(update)
    cursor = conn.cursor()
    cursor.execute(update)
    conn.commit()


def deleteTable(tablename, conn, where={}, key='AND'):
    delete="DELETE FROM "+tablename +" WHERE "
    
    if len(where)>0:
        j=0       
        for i in where:
            if(j<len(where)-1):
                delete+="`"+i+"`"
                delete+="='"
                delete+= where[i]
                delete+="' " +key+" "
            else:
                delete+="`"+i+"`"
                delete+="='"
                delete+= where[i]
                delete+="'"
            j+=1
            
    print(delete)
    cursor = conn.cursor()
    cursor.execute(delete)
    conn.commit()

conn=connectToDB('college','root')

h={'Address':'Nashik'}
p=['student_id','student_name']

w={'student_id':'4','student_name':'D'}
d={'Address':'Pune'}


'''deleteTable('student',w,'AND',conn)
selectFromTable('student',p,h,[],conn)


updateTable('student',w,d,'and',conn)
selectFromTable('student',p,h,[],conn'''

col={'A' : 'int', 'B': 'varchar(20)'}
createTable('ASD',conn,col)

