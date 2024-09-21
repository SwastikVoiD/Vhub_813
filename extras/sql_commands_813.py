import mysql.connector as mysql
sql = mysql.connect(host="localhost",user="root",password="manager",database="Vhub")
# if sql.is_connected():
#     print(True)
# else:
#     print(False)
cursor = sql.cursor()

def new_user(unm,fnm,lnm,ph,eml,pwd,lev):
    try:
        cursor.execute("INSERT INTO user_master VALUES({},{},{},{},{},{},{})".format(unm,fnm,lnm,pwd,lev,ph,eml))
        success= True 
    except:
        success= False
    finally:
        return success

def login(unm,pwd):
    cursor.execute("SELECT uname, pwd FROM user_master WHERE uname={}".format(unm))
        