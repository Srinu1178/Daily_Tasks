import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username = "root",
    password = 'Srinu@1178',
    database = 'college'
)

mycursor = connection.cursor()
# mycursor.execute("create database college")
# print("Database created")
# query="""
# CREATE TABLE students(
# id int auto_increment primary key,
# name varchar(20),
# age int,
# email varchar(20) unique,
# phone int
# );
# """
# mycursor.execute(query)

# mycursor.execute("ALTER TABLE students modify column phone bigint;")
# mycursor.execute("ALTER TABLE students auto_increment=101;")
# mycursor.execute("USE students;")
print("-"*10,"Student database System","-"*10)
while True:
    print("Menu")
    print("1. Add the student")
    print("2. Update the student")
    print("3. Delete the student")
    print("4. Display the students")
    print("5. Exit")
    choice = int(input("Enter your choice(1-5): "))
    if choice == 1:
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        email = input("Enter the mail id: ")
        phone = int(input("Enter the mobile no: "))
        query = """INSERT INTO students(name,age,email,phone) VALUES
        (%s,%s,%s,%s);"""
        values = (name,age,email,phone)
        mycursor.execute(query,values)
        connection.commit()
        print("Insert student data successful")
    elif choice == 2:
        stu_id = int(input("Enter your student id: "))
        value = int(input("Enter your age: "))
        query = '''UPDATE students set age =%s where id = %s;'''
        values = (value,stu_id)
        mycursor.execute(query,values)
        connection.commit()
    elif choice == 3:
        stu_id = int(input("Enter the id: "))
        query = '''DELETE FROM students where id = %s'''
        values = (stu_id,)
        mycursor.execute(query,values)
        connection.commit()
    elif choice == 4:
        query = '''SELECT * FROM students;s'''
        mycursor.execute(query)
        results = mycursor.fetchall()
        for data in results:
            print(data)
    elif choice == 5:
        break
    else:
        print("Invalid choice, please enter correct choice: ")

        
        
