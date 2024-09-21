import mysql.connector as mysql

# Connect to MySQL
sql = mysql.connect(host='localhost', user='root', password='abc+1234')
cursor = sql.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS VHUB")
cursor.execute("USE VHUB")
cursor.execute("CREATE TABLE IF NOT EXISTS user_master (username VARCHAR(9) PRIMARY KEY,credentials VARCHAR(12) NOT NULL,FNAME VARCHAR(40),LNAME VARCHAR(40),DOB DATE,SEX CHAR(1),HOSTEL VARCHAR(3),ROOMNO VARCHAR(4),PHONE VARCHAR(15),EMERGENCY VARCHAR(15),EMAIL VARCHAR(100))")

# Schedule table
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS schedule (
#         SNO INT PRIMARY KEY AUTO_INCREMENT,
#         username VARCHAR(9),
#         SDATE DATE,
#         STIME TIME,
#         EDATE DATE,
#         ETIME TIME,
#         CAT CHAR(10),
#         DES CHAR(255),
#         EOR CHAR(50),
#         FOREIGN KEY (username) REFERENCES user_master(username))""")

def new_user(uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")


 # Check if the username exists
    cursor.execute("SELECT username FROM user_master WHERE username = %s", (uname,))
    if cursor.fetchone() is None:
        # Insert the new user data
        cursor.execute("""
            INSERT INTO user_master (username, credentials, FNAME, LNAME, DOB, SEX, HOSTEL, ROOMNO, PHONE, EMERGENCY, EMAIL) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email))
        
       
        
        sql.commit()
        return "New user created successfully with a default schedule!"
    else:
        return "User already exists."

def login(uname, cred):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute(f"SELECT username, credentials from user_master where username='{uname}'")
    result=cursor.fetchone()
    if result is not None:
        if cred== result[1]:
            return True
        else:
            return False
    
def vlx_sql_submitadd(item,selected,price,desc,timestamp):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")

    insert_query = "INSERT INTO olx (item, category, price, description, timestamp) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (item, selected, float(price), desc, timestamp))
    sql.commit()

def vlx_sql_submitsearch(item,selected):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    search_query = "SELECT * FROM olx WHERE item LIKE %s AND category = %s"
    cursor.execute(search_query, (f"%{item}%", selected))
    results = cursor.fetchall()
    return results
def faq_qa():
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute("SELECT questions, answers FROM faq")
    faqs = cursor.fetchall()
    return faqs
def contact_sql():
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute("SELECT hostel_type, title, name, email, phone FROM hostel_contacts")
    contacts = cursor.fetchall()
    return contacts
def travel_submit(destination,date,time,transport,people):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    query = "INSERT INTO travel_details (destination, travel_date, travel_time, transport, number_of_people) VALUES (%s, %s, %s, %s, %s)"
    values = (destination, date, time, transport, int(people))
    sql.commit()
    return True
def travel_check(destination,date):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    query = "SELECT * FROM travel_details WHERE destination = %s AND travel_date = %s "
    values = (destination, date)
    results = cursor.fetchall()
def forum_add(user,content):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute("INSERT INTO forum (user, content) VALUES (%s, %s)", (user, content))
    sql.commit() 
def forum_update():
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute("SELECT user, content, timestamp FROM forum")
    return cursor.fetchall()
def getname(user,pwd):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute(f"SELECT username, credentials,email from user_master where username='{user}'")
    result=cursor.fetchone()
    if result is not None:
        if pwd== result[1]:
            return result[2]
def getalldata(regno,email):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute(f"SELECT * from user_master where email='{email}' and username='{regno}'")
    result=cursor.fetchone()
    return result
def checkpass(regno,email,cred):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute(f"SELECT credentials from user_master where email='{email}' and username='{regno}'")
    result=cursor.fetchone()
    if result is not None:
        if cred==result[0]:
            return True
        else:
            return False
def changepass(new,regno):
    sql = mysql.connect(host='localhost', user='root', password='abc+1234')
    cursor = sql.cursor()
    cursor.execute("USE VHUB")
    cursor.execute(f"update user_master set credentials='{new}' where username='{regno}'")
    sql.commit()
def update_user_details(regno, new_details):
    try:
        sql = mysql.connect(host='localhost', user='root', password='abc+1234')
        cursor = sql.cursor()
        cursor.execute("USE VHUB")
        fname, lname = new_details['name'].split(maxsplit=1) if ' ' in new_details['name'] else (new_details['name'], "")

        query = f"UPDATE user_master SET fname = '{fname}', lname = '{lname}', dob = '{new_details['dob']}', sex = '{new_details['gender']}', hostel = '{new_details['hostel']}', roomno = '{new_details['room']}', phone = '{new_details['phone']}', emergency = '{new_details['emergency_phone']}', email = '{new_details['email']}' WHERE username = '{regno}'"
        
        cursor.execute(query)
        
        sql.commit()
        return cursor.rowcount > 0 
    except Exception as e:
        print(f"Database error: {str(e)}")
        return False



    



# def add_to_schedule(uname,sdate,stime,edate,etime,category,description):
#      # Add a default schedule for the new user
#     cursor.execute("""
#         INSERT INTO schedule (username, SDATE, STIME, EDATE, ETIME, CAT, DES) 
#         VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """, (uname, sdate, stime, edate, etime, category, description))
    

# def display_schedule(username):
#     cursor.execute("""
#         SELECT SDATE, STIME, EDATE, ETIME, CAT, DES 
#         FROM schedule 
#         WHERE username = %s 
#         ORDER BY SDATE, STIME
#     """, (username,))
    
#     schedules = cursor.fetchall()
#     if schedules:
#         print(f"Schedules for {username}:")
#         for schedule in schedules:
#             print(f"Date: {schedule[0]}, Start Time: {schedule[1]}, End Date: {schedule[2]}, End Time: {schedule[3]}, Category: {schedule[4]}, Description: {schedule[5]}")
#     else:
#         print("No schedules found.")


# # # Example usage
# A = new_user('24BME0133', 'Arya@813', 'Swastik', 'Patnaik', '2006-08-17', 'M', 'Q', '1234', '1234567890', '7008976034', 'swasti.debesh2024@gmail.com')
# print(A)

# # Display the schedule
# display_schedule('24BME0133')
# add_to_schedule('24BME0133',)

# Close the cursor and connection
cursor.close()
sql.close()