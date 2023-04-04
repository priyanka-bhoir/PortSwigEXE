Lab #3: CSRF where token validation depends on token being present

Vulnerable Parameter - email change functionaity

End Goal - exploit CSRF to change email address

creds - wiener:peter


Analysis:

In order for a CSRF attack to be possible:
- A relevent action : change a user email
- cookie based session handling : session cookie
- No unpredictable request parameters : 


Testing CSRF tokens:

1. changed req method to post to get