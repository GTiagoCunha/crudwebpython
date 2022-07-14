import pyodbc

server = 'DESKTOP-FMVUDMT\SQLEXPRESS'
database = 'CRUD'
username = 'tyga'
password = '97113632'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()