import mysql.connector 
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

mydb = mysql.connector.connect(
   host="localhost",
   user="root", 
   password="Nikhil@11", 
   database="petroltry"
)

c = mydb.cursor()

def create_table(): 
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS Owners (
            Owner_id varchar(10) NOT NULL,
            Owner_Name varchar(20) NOT NULL,
            Contact_NO char(10) NOT NULL,
            DOB date DEFAULT NULL,
            Gender char DEFAULT NULL,
            Address varchar(255) DEFAULT NULL,
            Partnership int(5) NOT NULL,
            PRIMARY KEY(Owner_id)
        )''')

        c.execute('''CREATE TABLE IF NOT EXISTS Petrolpump (
            Registration_No varchar(10) NOT NULL,
            Owner_id varchar(10) NOT NULL,
            Petrolpump_Name varchar(50) NOT NULL,
            Company_Name varchar(30) DEFAULT NULL,
            Opening_Year int(5) DEFAULT NULL,
            State varchar(30) DEFAULT NULL,
            City varchar(40) NOT NULL,
            PRIMARY KEY(Registration_No),
            FOREIGN KEY (Owner_id) REFERENCES Owners(Owner_id)
        )''')

        c.execute('''CREATE TABLE IF NOT EXISTS Employee (
            Employee_ID varchar(10) NOT NULL,
            Emp_Name varchar(30) NOT NULL,
            Emp_Gender char DEFAULT NULL,
            Designation varchar(10) DEFAULT NULL,
            DOB date DEFAULT NULL,
            Salary int(20) DEFAULT NULL,
            Emp_Address varchar(255) NOT NULL,
            Email_ID varchar(100) NOT NULL,
            Petrolpump_No varchar(10) DEFAULT NULL,
            Manager_ID varchar(10) DEFAULT NULL,
            PRIMARY KEY(Employee_ID)
        )''')

        c.execute('''CREATE TABLE IF NOT EXISTS Customer (
            Customer_Code varchar(10) NOT NULL,
            C_Name varchar(30) NOT NULL,
            Phone_No char(10) DEFAULT NULL,
            Email_ID varchar(100) DEFAULT NULL,
            Gender char DEFAULT NULL,
            City varchar(50) DEFAULT NULL,
            Age int(3) DEFAULT NULL,
            PRIMARY KEY(Customer_Code)
        )''')

        c.execute('''CREATE TABLE IF NOT EXISTS Invoice (
            Invoice_No varchar(10) NOT NULL,
            Date date NOT NULL,
            Payment_Type varchar(20) NOT NULL,
            Fuel_Amount float(15) DEFAULT NULL,
            Fuel_Type varchar(15) DEFAULT NULL,
            Discount int(5) DEFAULT NULL,
            Total_Price float(10) NOT NULL,
            Customer_Code varchar(10) NULL,
            PRIMARY KEY(Invoice_No)
        )''')

        c.execute('''CREATE TABLE IF NOT EXISTS Tanker (
            Tanker_ID varchar(10) NOT NULL,
            Capacity float(10) DEFAULT NULL,
            pressure float(10) DEFAULT NULL,
            Fuel_ID varchar(10) NOT NULL,
            Fuel_Amount float(15) DEFAULT NULL,
            Fuel_Name varchar(20) DEFAULT NULL,
            Fuel_Price float(5) NOT NULL,
            Petrolpump_No varchar(10) DEFAULT NULL,
            PRIMARY KEY(Tanker_ID)
        )''')

        logging.info("Tables created successfully.")

    except mysql.connector.Error as err:
        logging.error("Error while creating tables: %s", err)

create_table()

# Adding petrol pump details
def add_Petrolpump_data( Registration_No, Owner_id, Petrolpump_Name, Company_Name, Opening_Year, State, City):
    c.execute('INSERT INTO Petrolpump (Registration_No, Owner_id, Petrolpump_Name, Company_Name, Opening_Year, State, City) VALUES (%s,%s,%s,%s,%s,%s,%s)', ( Registration_No, Owner_id, Petrolpump_Name, Company_Name, Opening_Year, State, City))
    mydb.commit()

# Adding owners
def add_Owners_data(Owner_id, Owner_Name, Contact_NO, DOB, Gender, Address, Partnership):
    c.execute('INSERT INTO Owners (Owner_id, Owner_Name, Contact_NO, DOB, Gender, Address, Partnership) VALUES (%s,%s,%s,%s,%s,%s,%s)', (Owner_id, Owner_Name, Contact_NO, DOB, Gender, Address, Partnership))
    mydb.commit()

# Adding employee details
def add_Employee_data(Employee_ID, Emp_Name, Emp_Gender, Designation, DOB, Salary, Emp_Address, Email_ID, Petrolpump_No, Manager_ID):
    c.execute('INSERT INTO Employee (Employee_ID, Emp_Name, Emp_Gender, Designation, DOB, Salary, Emp_Address, Email_ID, Petrolpump_No, Manager_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (Employee_ID, Emp_Name, Emp_Gender, Designation, DOB, Salary, Emp_Address, Email_ID, Petrolpump_No, Manager_ID))
    mydb.commit()

# Adding customer details
def add_Customer_data(Customer_Code, C_Name, Phone_No, Email_ID, Gender, City, Age):
    c.execute('INSERT INTO Customer (Customer_Code, C_Name, Phone_No, Email_ID, Gender, City, Age) VALUES (%s,%s,%s,%s,%s,%s,%s)', (Customer_Code, C_Name, Phone_No, Email_ID, Gender, City, Age))
    mydb.commit() 

# Adding invoice data
def add_Invoice_data(Invoice_No, Date, Payment_Type, Fuel_Amount, Fuel_Type, Discount, Total_Price, Customer_Code):
    c.execute('INSERT INTO Invoice (Invoice_No, Date, Payment_Type, Fuel_Amount, Fuel_Type, Discount, Total_Price, Customer_Code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (Invoice_No, Date, Payment_Type, Fuel_Amount, Fuel_Type, Discount, Total_Price, Customer_Code))
    mydb.commit()

# Adding tanker data
def add_Tanker_data(Tanker_ID, Capacity, pressure, Fuel_ID, Fuel_Amount, Fuel_Name, Fuel_Price, Petrolpump_No):
    c.execute('INSERT INTO Tanker (Tanker_ID, Capacity, pressure, Fuel_ID, Fuel_Amount, Fuel_Name, Fuel_Price, Petrolpump_No) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (Tanker_ID, Capacity, pressure, Fuel_ID, Fuel_Amount, Fuel_Name, Fuel_Price, Petrolpump_No))
    mydb.commit()






#to view the owner id to be used in the petrolpump table
# def view_only_Owner_id():
#     try:
#         c.execute("SELECT Owner_id FROM Owners")
#         data = c.fetchall()
#         print(data)
#         # Extract the first element from each tuple in the result
#         owner_ids = [row[0] for row in data]
#         return owner_ids
#     except mysql.connector.Error as err:
#         logging.error("Error fetching Owner IDs: %s", err)
#         return None

def view_only_Owner_id():
    try:
        c.callproc("only_view_only_Owner_id")
        data = c.stored_results()
        owner_ids=[]
        for d in data:
            m=d.fetchall()
            for n in m:
                owner_ids.append(n[0])
       
        return owner_ids
        # Extract the first element from each tuple in the result
        
    except mysql.connector.Error as err:
        logging.error("Error fetching Owner IDs: %s", err)
        return None

def view_all_Petrolpump_data():
    c.execute('SELECT * FROM Petrolpump')
    data = c.fetchall()
    return data

def view_all_Owners_data():
    c.execute('SELECT * FROM Owners')
    data = c.fetchall()
    return data

def view_all_Employee_data():
    c.execute('SELECT * FROM Employee')
    data = c.fetchall()
    return data

def view_all_Customer_data():
    c.execute('SELECT * FROM Customer')
    data = c.fetchall()
    return data

def view_all_Invoice_data():
    c.execute('SELECT * FROM Invoice')
    data = c.fetchall()
    return data


def view_all_Tanker_data():
    c.execute('SELECT * FROM Tanker')
    data = c.fetchall()
    return data

# View only Registration Numbers
def view_only_Registration_No():
    try:
        c.execute("SELECT Registration_No FROM Petrolpump")
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching registration numbers: %s", err)
        return None

# View only Owner Names
def view_only_Owner_Name():
    try:
        c.execute("SELECT Owner_Name FROM Owners")
        data = c.fetchall()
       
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching owner names: %s", err)
        return None

# View only Employee IDs
def view_only_Employee_ID():
    try:
        c.execute("SELECT Employee_ID FROM Employee")
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching employee IDs: %s", err)
        return None

# View only Customer Codes
def view_only_Customer_Code():  
    try:
        c.execute("SELECT Customer_Code FROM Customer")
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching customer codes: %s", err)
        return None

# View only Invoice Numbers
def view_only_Invoice_No():
    try:
        c.execute("SELECT Invoice_No FROM Invoice")
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching invoice numbers: %s", err)
        return None

# View only Tanker IDs
def view_only_Tanker_ID():
    try:
        c.execute("SELECT Tanker_ID FROM Tanker")
        data = c.fetchall()
        
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching tanker IDs: %s", err)
        return None


# Function to get all information about a Petrolpump
def get_all_info_Petrolpump(selected_Petrolpump):
    try:
        c.execute('SELECT * FROM Petrolpump WHERE Registration_No="{}"'.format(selected_Petrolpump))
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching petrolpump information: %s", err)
        return None

# Function to get all information about an Owner
def get_all_info_Owners(selected_Owners): 
    try:
        c.execute('SELECT * FROM Owners WHERE Owner_id="{}"'.format(selected_Owners))
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching owner information: %s", err)
        return None

# Function to get all information about an Employee
def get_all_info_Employee(selected_Employee):
    try:
        c.execute('SELECT * FROM Employee WHERE Employee_ID="{}"'.format(selected_Employee))
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching employee information: %s", err)
        return None

# Function to get all information about a Customer
def get_all_info_Customer(selected_Customer):
    try:
        c.execute('SELECT * FROM Customer WHERE Customer_Code="{}"'.format(selected_Customer))
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching customer information: %s", err)
        return None

# Function to get all information about an Invoice
def get_all_info_Invoice(selected_Invoice):
    try:
        c.execute('SELECT * FROM Invoice WHERE Invoice_No="{}"'.format(selected_Invoice))
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching invoice information: %s", err)
        return None

# Function to get all information about a Tanker
def get_all_info_Tanker(selected_Tanker):
    try:
        c.execute('SELECT * FROM Tanker WHERE Tanker_ID="{}"'.format(selected_Tanker))
        data = c.fetchall()
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching tanker information: %s", err)
        return None


# Function to edit Petrolpump data
def edit_Petrolpump_data(new_Owner_id,new_Petrolpump_Name, new_Company_Name, new_Opening_Year, new_State, new_City, Registration_No):
    try:
        c.execute("UPDATE Petrolpump SET Owner_id=%s, Petrolpump_Name=%s, Company_Name=%s, Opening_Year=%s, State=%s, City=%s WHERE Registration_No=%s", (new_Owner_id,new_Petrolpump_Name, new_Company_Name, new_Opening_Year, new_State, new_City, Registration_No))
        mydb.commit()
        data = view_all_Petrolpump_data()
        return data
    except mysql.connector.Error as err:
        logging.error("Error editing petrolpump data: %s", err)
        return None

# 333333

# Function to edit Owner data
def edit_Owners_data(new_Owner_Name,new_Contact_NO, new_DOB, new_Gender, new_Address, new_Partnership, Owner_id):
    try:
        c.execute("UPDATE Owners SET Owner_Name=%s, Contact_NO=%s, DOB=%s, Gender=%s, Address=%s, Partnership=%s WHERE Owner_id=%s", (new_Owner_Name,new_Contact_NO, new_DOB, new_Gender, new_Address, new_Partnership, Owner_id))
        mydb.commit()
        data = view_all_Owners_data()
        return data
    except mysql.connector.Error as err:
        logging.error("Error editing owner data: %s", err)
        return None

# Function to edit Employee data
def edit_Employee_data(new_Emp_Name, new_Emp_Gender, new_Designation, new_DOB, new_Salary, new_Emp_Address, new_Email_ID, new_Petrolpump_No, new_Manager_ID, Employee_ID):
    try:
        c.execute("UPDATE Employee SET Emp_Name=%s, Emp_Gender=%s, Designation=%s, DOB=%s, Salary=%s, Emp_Address=%s, Email_ID=%s, Petrolpump_No=%s, Manager_ID=%s WHERE Employee_ID=%s", (new_Emp_Name, new_Emp_Gender, new_Designation, new_DOB, new_Salary, new_Emp_Address, new_Email_ID, new_Petrolpump_No, new_Manager_ID, Employee_ID))
        mydb.commit()
        data = view_all_Employee_data()
        return data
    except mysql.connector.Error as err:
        logging.error("Error editing employee data: %s", err)
        return None

# Function to edit Customer data
def edit_Customer_data(new_C_Name, new_Phone_No, new_Email_ID, new_Gender, new_City, new_Age, Customer_Code):
    try:
        c.execute("UPDATE Customer SET C_Name=%s, Phone_No=%s, Email_ID=%s, Gender=%s, City=%s, Age=%s WHERE Customer_Code=%s", (new_C_Name, new_Phone_No, new_Email_ID, new_Gender, new_City, new_Age, Customer_Code))
        mydb.commit()
        data = view_all_Customer_data()
        return data
    except mysql.connector.Error as err:
        logging.error("Error editing customer data: %s", err)
        return None

# Function to edit Invoice data
def edit_Invoice_data(new_Date, new_Payment_Type, new_Fuel_Amount, new_Fuel_Type, new_Discount, new_Total_Price, new_Customer_Code, Invoice_No):
    try:
        c.execute("UPDATE Invoice SET Date=%s, Payment_Type=%s, Fuel_Amount=%s, Fuel_Type=%s, Discount=%s, Total_Price=%s, Customer_Code=%s WHERE Invoice_No=%s", (new_Date, new_Payment_Type, new_Fuel_Amount, new_Fuel_Type, new_Discount, new_Total_Price, new_Customer_Code, Invoice_No))
        mydb.commit()
        data = view_all_Invoice_data()
        return data
    except mysql.connector.Error as err:
        logging.error("Error editing invoice data: %s", err)
        return None

# Function to edit Tanker data
def edit_Tanker_data(new_Capacity, new_pressure, new_Fuel_ID, new_Fuel_Amount, new_Fuel_Name, new_Fuel_Price, new_Petrolpump_No, Tanker_ID):
    try:
        c.execute("UPDATE Tanker SET Capacity=%s, pressure=%s, Fuel_ID=%s, Fuel_Amount=%s, Fuel_Name=%s, Fuel_Price=%s, Petrolpump_No=%s WHERE Tanker_ID=%s", (new_Capacity, new_pressure, new_Fuel_ID, new_Fuel_Amount, new_Fuel_Name, new_Fuel_Price, new_Petrolpump_No, Tanker_ID))
        mydb.commit()
        data = view_all_Tanker_data()
        return data
    except mysql.connector.Error as err:
        logging.error("Error editing tanker data: %s", err)
        return None


# Function to delete Petrolpump data
def delete_data_Petrolpump(selected_Petrolpump):
    try:
        c.execute('DELETE FROM Petrolpump WHERE Registration_No="{}"'.format(selected_Petrolpump))
        mydb.commit()
    except mysql.connector.Error as err:
        logging.error("Error deleting petrolpump data: %s", err)

# Function to delete Owner data
def delete_data_Owners(selected_Owners):
    try:
        c.execute('DELETE FROM Owners WHERE Owner_Name="{}"'.format(selected_Owners))
        mydb.commit()
    except mysql.connector.Error as err:
        logging.error("Error deleting owner data: %s", err)

# Function to delete Employee data
def delete_data_Employee(selected_Employee):
    try:
        c.execute('DELETE FROM Employee WHERE Employee_ID="{}"'.format(selected_Employee))
        mydb.commit()
    except mysql.connector.Error as err:
        logging.error("Error deleting employee data: %s", err)

# Function to delete Customer data
def delete_data_Customer(selected_Customer):
    try:
        c.execute('DELETE FROM Customer WHERE Customer_Code="{}"'.format(selected_Customer))
        mydb.commit()
    except mysql.connector.Error as err:
        logging.error("Error deleting customer data: %s", err)

# Function to delete Invoice data
def delete_data_Invoice(selected_Invoice):
    try:
        c.execute('DELETE FROM Invoice WHERE Invoice_No="{}"'.format(selected_Invoice))
        mydb.commit()
    except mysql.connector.Error as err:
        logging.error("Error deleting invoice data: %s", err)

# Function to delete Tanker data
def delete_data_Tanker(selected_Tanker):
    try:
        c.execute('DELETE FROM Tanker WHERE Tanker_ID="{}"'.format(selected_Tanker))
        mydb.commit()
    except mysql.connector.Error as err:
        logging.error("Error deleting tanker data: %s", err)

#invoicebackup

def view_all_invoice_backup():
    c.execute('SELECT * FROM invoice_backup ')
    data = c.fetchall()
    return data



# database.py

def execute_query(query):
    try:
        c.execute(query)
        mydb.commit()
        logging.info("Query executed successfully.")
    except mysql.connector.Error as err:
        mydb.rollback()
        logging.error("Error executing query: %s", err)



