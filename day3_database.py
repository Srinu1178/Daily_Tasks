import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
try:
    connection = mysql.connector.connect(
       host=os.environ.get("DB_HOST"),
       user=os.environ.get("DB_USER"),        # Note: mysql.connector uses 'user', not 'username'
       password=os.environ.get("DB_PASSWORD"),
       database=os.environ.get("DB_NAME")
    )

    mycursor = connection.cursor()

except mysql.connector.Error as e:
    print(f'database error: {e}')

mycursor.execute("SHOW TABLES")
tables = [table[0] for table in mycursor.fetchall()]
for i,table in enumerate(tables,start=1):
    print(f'{i}.{table}')

choice = int(input("Enter the choice: "))
table_name = tables[choice-1]
print(f'Selected table: {table_name}')

mycursor.execute(f"DESCRIBE {table_name}")
columns = mycursor.fetchall()
column_names = [column[0] for column in columns]

def add_student():
    insert_columns=[]
    values = []
    for column in columns:
        column_name = column[0]
        extra = column[5]
        data_type = column[1]
        if extra and "auto_increment" in extra.lower():
            continue
        if data_type.startswith('int'):
            value = int(input(f"Enter the {column_name}: "))
        elif data_type.startswith("decimal") or data_type.startswith("float"):
            value = float(input(f"Enter the {column_name}: "))
        elif data_type.startswith("date"):
            value = input(f"Enter the {column_name} (YYYY-MM-DD): ")
        else:
            value = input(f"Enter the {column_name}: ")
        insert_columns.append(column_name)
        values.append(value)
    sql = ", ".join(f'{column}' for column in insert_columns)
    placeholder = ', '.join(['%s']*len(values))
    query = f'''INSERT INTO `{table_name}`({sql})
    VALUES({placeholder})'''
    mycursor.execute(query,values)
    connection.commit()
    print("Insert the data successfully")


def search_data():
    retrieve = int(input("Enter how many fields: "))
    for i,column in enumerate(column_names,start=1):
        print(f'{i}.{column}')
    fields = input("Enter the what fields you want seperated by commas: ")
    if retrieve==len(fields):
        fields1 = fields.split(",")
        fields1 = [int(x.strip()) - 1 for x in fields.split(",")]
        search_column = None
        for column in columns:
            if column[3]=="PRI" and column[1]=='int':
                search_column = column[0]
                search = int(input(f"Enter the {search_column} for search: "))
                break
        selected_columns = [column_names[i] for i in fields1]
        sql = ", ".join(f"`{column}`" for column in selected_columns)
        query = f'''SELECT {sql} from `{table_name}`
        where `{search_column}` = %s;'''
        mycursor.execute(query, (search,))
        data = mycursor.fetchone()
        for col in selected_columns:
            print(col,end='->')
            print(" ")
        for d in data:
            print(d,end='->')
            print(" ")
    else:
        print("Expected selected field names")

def update_data():
    print(f'Column names in the {table_name}:')
    for i,c in enumerate(column_names,start=1):
        print(f'{i}. {c}')
    update_column = int(input("Enter which column to updated: "))
    unique_col = None
    value = None
    print(columns[0][0]==column_names[update_column-1])
    for column in columns:
        if column[0]==column_names[update_column-1]:
            if column[3]=="PRI":
                print(f"We can't update the primary key value")
        if column[0]==column_names[update_column-1] and column[1]=='int':
            value = int(input(f"Enter the new value for {column[0]}: "))
        elif column[0]==column_names[update_column-1] and column[1].startswith("float") or column[1].startswith("decimal"):
            value = float(input(f"Enter the new value for {column[0]}: "))
        elif column[0]==column_names[update_column-1] and column[1].startswith('datetime'):
            value = input(f'Enter the new value for {column[0]} (YYYY-MM-DD HH:MM:SS): ')
        elif column[0]==column_names[update_column-1] and column[0].startswith('date'):
            value = input(f'Enter the new value for {column[0]} (YYYY-MM-DD): ')
        elif column[0]==column_names[update_column-1]:
            value = input(f'Enter the new value for {column[0]}: ')
        
        if column[3]=="PRI":
            unique_col = column[0]
            search = int(input(f"Enter the value {unique_col} for update (which row to update): "))
    query = f'''UPDATE `{table_name}` SET `{column_names[update_column-1]}`= %s
    WHERE `{unique_col}` = %s;'''
    values = (value,search)
    mycursor.execute(query,values)
    connection.commit()
    print("Update data successful")

def delete_data():
    primary=None
    for column in columns:
        if column[3]=="PRI":
            primary=column[0]
            break
    value = int(input(f"Enter the {primary} id for deletion: "))

    query = f'''DELETE FROM `{table_name}` WHERE `{primary}`= %s;'''
    mycursor.execute(query,(value,))
    connection.commit()
    print("deletion successful")

def display_data():
    for column in column_names:
        print(column,end=" ")
    print()
    query = f'''SELECT * FROM `{table_name}`;'''
    mycursor.execute(query)
    result = mycursor.fetchall()
    for data in result:
        for d in data:
            print(d,end=" ")
        print()


            

while True:
    print("1. Add the data")
    print("2. Search Data")
    print("3. Update the Data")
    print("4. Delete the Data")
    print("5. Display the Data")
    print("6. Exit the menu")

    choice = int(input("Enter the choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        search_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        display_data()
    elif choice == 6:
        print("Exit the menu successful")
        break
    else:
        print("Invalid choice, try again")


mycursor.close()
connection.close()