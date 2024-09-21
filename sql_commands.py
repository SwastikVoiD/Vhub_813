# import mysql.connector as mysql
# # Connect to MySQL
# sql = mysql.connect(host='localhost', user='root', password='manager')
# cursor = sql.cursor()

# # Create database and table if they do not exist
# cursor.execute("CREATE DATABASE IF NOT EXISTS VHUB")
# cursor.execute("USE VHUB")

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS user_master (
#         username VARCHAR(9) PRIMARY KEY,
#         credentials VARCHAR(12) NOT NULL,
#         FNAME VARCHAR(40),
#         LNAME VARCHAR(40),
#         DOB DATE,
#         SEX CHAR(1),
#         HOSTEL VARCHAR(3),
#         ROOMNO VARCHAR(4),
#         PHONE VARCHAR(15),
#         EMERGENCY VARCHAR(15),
#         EMAIL VARCHAR(100)
#     )
# """)

# def new_user(uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email):
#     # Check if the username exists
#     cursor.execute("SELECT username FROM user_master WHERE username = %s", (uname,))
#     if cursor.fetchone() is None:
#         # Insert the new user data
#         cursor.execute("""
#             INSERT INTO user_master (username, credentials, FNAME, LNAME, DOB, SEX, HOSTEL, ROOMNO, PHONE, EMERGENCY, EMAIL) 
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """, (uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email))
        
#         # Create a scheduler table for the new user
#         cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS {uname}_SCHEDULER (
#                 SNO INT PRIMARY KEY AUTO_INCREMENT,
#                 SDATE DATE,
#                 STIME TIME,
#                 EDATE DATE,
#                 ETIME TIME,
#                 CAT CHAR(10),
#                 DES CHAR(255),
#                 ORG CHAR(9) NOT NULL DEFAULT '{uname}'
#             )
#         """)
        
#         sql.commit()
#         return "New user created successfully!"
#     else:
#         return "User already exists."

# def login(uname, cred):
#     cursor.execute("SELECT username, credentials FROM user_master WHERE username = %s", (uname,))
#     result = cursor.fetchone()
#     if result is not None:
#         if cred == result[1]:
#             return True
#     return False

# # Example usage
# A = new_user('24BME0133', 'Arya@813', 'Swastik', 'Patnaik', '2006-08-17', 'M', 'Q', '1234', '1234567890', '7008976034', 'swasti.debesh2024@gmail.com')
# print(A)
# B = login('24BME0133','Arya@813')
# print(B)
# # Close the cursor and connection
# cursor.close()
# sql.close()


import mysql.connector as mysql

# Connect to MySQL
sql = mysql.connect(host='localhost', user='root', password='manager')
cursor = sql.cursor()

# Create database and table if they do not exist
cursor.execute("CREATE DATABASE IF NOT EXISTS VHUB")
cursor.execute("USE VHUB")

# User table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_master (
        username VARCHAR(9) PRIMARY KEY,
        credentials VARCHAR(12) NOT NULL,
        FNAME VARCHAR(40),
        LNAME VARCHAR(40),
        DOB DATE,
        SEX CHAR(1),
        HOSTEL VARCHAR(3),
        ROOMNO VARCHAR(4),
        PHONE VARCHAR(15),
        EMERGENCY VARCHAR(15),
        EMAIL VARCHAR(100)
    )
""")

# Schedule table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS schedule (
        SNO INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(9),
        SDATE DATE,
        STIME TIME,
        EDATE DATE,
        ETIME TIME,
        CAT CHAR(10),
        DES CHAR(255),
        EOR CHAR(50),
        FOREIGN KEY (username) REFERENCES user_master(username))""")

def new_user(uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email):
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


def add_to_schedule(uname,sdate,stime,edate,etime,category,description):
     # Add a default schedule for the new user
    cursor.execute("""
        INSERT INTO schedule (username, SDATE, STIME, EDATE, ETIME, CAT, DES) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (uname, sdate, stime, edate, etime, category, description))
    

def display_schedule(username):
    cursor.execute("""
        SELECT SDATE, STIME, EDATE, ETIME, CAT, DES 
        FROM schedule 
        WHERE username = %s 
        ORDER BY SDATE, STIME
    """, (username,))
    
    schedules = cursor.fetchall()
    if schedules:
        print(f"Schedules for {username}:")
        for schedule in schedules:
            print(f"Date: {schedule[0]}, Start Time: {schedule[1]}, End Date: {schedule[2]}, End Time: {schedule[3]}, Category: {schedule[4]}, Description: {schedule[5]}")
    else:
        print("No schedules found.")


# # Example usage
# A = new_user('24BME0133', 'Arya@813', 'Swastik', 'Patnaik', '2006-08-17', 'M', 'Q', '1234', '1234567890', '7008976034', 'swasti.debesh2024@gmail.com', 
#               '2024-09-21', '10:00:00', '2024-09-21', '11:00:00', 'Meeting', 'Team meeting in the conference room')
# print(A)

# # Display the schedule
display_schedule('24BME0133')
add_to_schedule('24BME0133',)

# Close the cursor and connection
cursor.close()
sql.close()
