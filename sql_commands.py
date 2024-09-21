import mysql.connector as mysql

# Connect to MySQL
sql = mysql.connect(host='localhost', user='root', password='manager')
cursor = sql.cursor()

# Create database and table if they do not exist
cursor.execute("CREATE DATABASE IF NOT EXISTS VHUB")
cursor.execute("USE VHUB")

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

def new_user(uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email):
    # Check if the username exists
    cursor.execute("SELECT username FROM user_master WHERE username = %s", (uname,))
    if cursor.fetchone() is None:
        # Insert the new user data
        cursor.execute("""
            INSERT INTO user_master (username, credentials, FNAME, LNAME, DOB, SEX, HOSTEL, ROOMNO, PHONE, EMERGENCY, EMAIL) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (uname, cred, fname, lname, dob, sex, hostel, roomno, phone, emergency, email))
        
        # Create a scheduler table for the new user
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {uname}_SCHEDULER (
                SNO INT PRIMARY KEY AUTO_INCREMENT,
                SDATE DATE,
                STIME TIME,
                EDATE DATE,
                ETIME TIME,
                CAT CHAR(10),
                DES CHAR(255),
                ORG CHAR(9) NOT NULL DEFAULT '{uname}'
            )
        """)
        
        sql.commit()
        return "New user created successfully!"
    else:
        return "User already exists."

def login(uname, cred):
    cursor.execute("SELECT username, credentials FROM user_master WHERE username = %s", (uname,))
    result = cursor.fetchone()
    if result is not None:
        if cred == result[1]:
            return True
    return False

# Example usage
A = new_user('24BME0133', 'Arya@813', 'Swastik', 'Patnaik', '2006-08-17', 'M', 'Q', '1234', '1234567890', '7008976034', 'swasti.debesh2024@gmail.com')
print(A)
B = login('24BME0133','Arya@813')
print(B)
# Close the cursor and connection
cursor.close()
sql.close()

