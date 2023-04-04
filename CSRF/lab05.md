Lab # 5: CSRF where token is tied to non-session cookie

Vulnerable parameter - email change functionality

End Goal - exploit CSRF to change email address

Creds- 
    wiener:peter
    carlos:montoya

Analysis:
In order for a CSRF attack to be possible:
- A relevent action : change a user email
- cookie based session handling : session cookie
- No unpredictable request parameters 

Testing CSRF tokens and CSRF cookies:
1. check if the CSRF token is tied to the CSRF cookie
	-submit an unvalid CSRF token -: not wokring
	-submit valid CSRF token from another user -: not working
2. submit valid CSRF token and cookie from another user

attacker csrfKey: Tcp0mROFrcNF48JZCznmgLKEWKJ59IfM

In order to exploit this vulnerablity, we need to perform 2 things:

1. Inject a csrfKey cookie int he user's session(Http header injection)
2. Send a CSRF attack to the victim with a known csrf token
 
