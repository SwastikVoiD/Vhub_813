import mysql.connector as smyql

sql = smyql.connect(host='localhost',user='newuser',password='managerboi')
cursor = sql.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS VHUB")
cursor.execute("USE VHUB")
cursor.execute("CREATE TABLE IF NOT EXISTS user_master (username VARCHAR(9) PRIMARY KEY, credentials VARCHAR(12) NOT NULL, FNAME VARCHAR(40),LNAME VARCHAR(40),DOB DATE, SEX CHAR(1), HOSTEL VARCHAR(3), ROOMNO VARCHAR(4), PHONE VARCHAR(15), EMERGENCY VARCHAR(15), EMAIL VARCHAR(100))")
# cursor.execute("CREATE TABLE IF NOT EXISTS Hevents_master (ETYPE CHAR(10), HOSTEL CHAR(1), EDEC CHAR(255), HBLOCK CHAR(2),  )")
def new_user(uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email):
    try:
        
        # Check if the username exists
        cursor.execute(f"SELECT username FROM user_master WHERE username ='{uname}'")
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
    cursor.execute(f"SELECT username, credentials from user_master where username='{uname}'")
    result=cursor.fetchone()
    if result is not None:
        if cred== result[1]:
            return True
        else:
            return False
    
def vlx_sql_submitadd(item,selected,price,desc,timestamp):
    insert_query = "INSERT INTO olx (item, category, price, description, timestamp) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (item, selected, float(price), desc, timestamp))
    sql.commit()

def vlx_sql_submitsearch(item,selected):
    search_query = "SELECT * FROM olx WHERE item LIKE %s AND category = %s"
    cursor.execute(search_query, (f"%{item}%", selected))
    results = cursor.fetchall()
    return results
def faq_qa():
    cursor.execute("SELECT questions, answers FROM faq")
    faqs = cursor.fetchall()
    return faqs
def contact_sql():
    cursor.execute("SELECT hostel_type, title, name, email, phone FROM hostel_contacts")
    contacts = cursor.fetchall()
    return contacts
def travel_submit(destination,date,time,transport,people):
    query = "INSERT INTO travel_details (destination, travel_date, travel_time, transport, number_of_people) VALUES (%s, %s, %s, %s, %s)"
    values = (destination, date, time, transport, int(people))
    sql.commit()
    return True
def travel_check(destination,date):
    query = "SELECT * FROM travel_details WHERE destination = %s AND travel_date = %s "
    values = (destination, date)
    results = cursor.fetchall()
def forum_add(user,content):
    cursor.execute("INSERT INTO forum (user, content) VALUES (%s, %s)", (user, content))
    sql.commit() 
def forum_update():
    cursor.execute("SELECT user, content, timestamp FROM forum")
    return cursor.fetchall()