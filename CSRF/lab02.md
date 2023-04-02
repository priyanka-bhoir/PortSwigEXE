Lab #2 : CSRF where token validation depends on request method

Vulnerable paramter - email change functionaity

End Goal: exploit CSRF to change email address

Cred - wiener:peter

Analysis:

In order for a CSRF attack to be possible:
- A relevent action : change a user email
- cookie based session handling : session cookie
- No unpredictable request parameters : Request method can be changed to GET which does not require CSRF token

Testing CSRF Tokens:
1. change the request method from POST to GET
