import mysql.connector as smyql

sql = smyql.connect(host='localhost',user='root',password='abc+1234')
cursor = sql.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS VHUB")
cursor.execute("USE VHUB")
cursor.execute("CREATE TABLE IF NOT EXISTS user_master (username VARCHAR(9) PRIMARY KEY, credentials VARCHAR(12) NOT NULL, FNAME VARCHAR(40),LNAME VARCHAR(40),DOB DATE, SEX CHAR(1), HOSTEL VARCHAR(3), ROOMNO VARCHAR(4), PHONE VARCHAR(15), EMERGENCY VARCHAR(15), EMAIL VARCHAR(100))")
# cursor.execute("CREATE TABLE IF NOT EXISTS Hevents_master (ETYPE CHAR(10), HOSTEL CHAR(1), EDEC CHAR(255), HBLOCK CHAR(2),  )")
def new_user(uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email):
    try:
        
        # Check if the username exists
        cursor.execute("SELECT username FROM user_master WHERE username = %s", (uname,))
        if cursor.fetchone() is None:

            # Insert the new user data
            cursor.execute("INSERT INTO user_master (username, credentials, fname, lname, dob, sex, hostel, roomno, phone, emergency, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email))
            cursor.execute("CREATE TABLE {}_SCHEDULER (SDATE DATE, STIME TIME, EDATE DATE, ETIME TIME, CAT CHAR(10), DES CHAR(255), ORG CHAR(9) NOT NULL DEFAULT '{}'".format(uname,uname))
            
            # cursor.execute("CREATE TABLE %s_TIME_TABLE (SLOT)")
            # cursor.execute("CREATE TABLE %s_ ")
            sql.commit()
            return("New user created successfully!")
        else:
            return("User already exists.")

    except smyql.Error as err:
        print("Error:", err)

def login(uname, cred):
    cursor.execute("SELECT username, credentials from user_master where username='%s'",(uname,))
    if cursor.fetchon() is not None:
        A = cursor.fetchone()
        if cred== A[1]:
            return True
        else:
            return False