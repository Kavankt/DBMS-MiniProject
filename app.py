import streamlit as st
import pandas as pd

from create import *
from database import *
from delete import *
from read import *
from update import *

def main():
   st.title("Petrol Pump Management System")
   menu = ["PetrolPump", "Owners", "Employee", "Customer","Invoice", "Tanker","backup_invoice"]#
   choice = st.sidebar.selectbox("Tables", menu)

   create_table()
   
   if choice == "PetrolPump":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
         st.subheader("Enter Petrolpump Details:")
         create_for_Petrolpump()
      elif choice2 == "View":
         st.subheader("View the Petrolpump details:")
         read_for_Petrolpump()
      elif choice2 == "Update":
         st.subheader("Update petrolpump details:")
         update_for_Petrolpump()
      elif choice2 == "Remove":
         st.subheader("Delete petrolpump details:")
         delete_for_Petrolpump()

   elif choice == "Owners":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
            st.subheader("Enter Owners Details:")
            create_for_Owners()
      elif choice2 == "View":
            st.subheader("View Owners details:")
            read_for_Owners()
      elif choice2 == "Update":
            st.subheader("Update owner details:")
            update_for_Owners()
      elif choice2 == "Remove":
            st.subheader("Delete owner details:")
            delete_for_Owners()

   elif choice == "Employee":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
         st.subheader("Enter Employee Details:")
         create_for_Employee()
      elif choice2 == "View":
         st.subheader("View the Employee details:")
         read_for_Employee()
      elif choice2 == "Update":
         st.subheader("Update employee details:")
         update_for_Employee()
      elif choice2 == "Remove":
         st.subheader("Delete employee details:")
         delete_for_Employee()

   elif choice == "Customer":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter Customer Details:")
         create_for_Customer()
     elif choice2 == "View":
         st.subheader("View the Customer details:")
         read_for_Customer()
     elif choice2 == "Update":
         st.subheader("Update customer details:")
         update_for_Customer()
     elif choice2 == "Remove":
         st.subheader("Delete customer details:")
         delete_for_Customer()

   elif choice == "Invoice":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter Invoice Details:")
         create_for_Invoice()
     elif choice2 == "View":
         st.subheader("View the Invoice details:")
         read_for_Invoice()
     elif choice2 == "Update":
         st.subheader("Update invoice details:")
         update_for_Invoice()
     elif choice2 == "Remove":
         st.subheader("Delete invoice details:")
         delete_for_Invoice()

   elif choice == "Tanker":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter Tanker Details:")
         create_for_Tanker()
     elif choice2 == "View":
         st.subheader("View the Tanker details:")
         read_for_Tanker()
     elif choice2 == "Update":
         st.subheader("Update tanker details:")
         update_for_Tanker()
     elif choice2 == "Remove":
         st.subheader("Delete tanker details:")
         delete_for_Tanker()

   elif choice == "backup_invoice":
      st.subheader("View the invoice_backup:")
      read_for_invoice_backup()

   # elif choice == "Query":
   #    query = st.text_input("Enter Your Query:")
   #    if st.button("Run Query"):
   #       execute_query(query)

if __name__ == '__main__':
   main()
