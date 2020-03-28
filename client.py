import http.client
#from pprint import pprint

HOST = 'ga-ga-ga.ga'
connection = http.client.HTTPConnection(HOST, port=80)
connection.request('GET', '/')

result = connection.getresponse()
body_result = result.read().decode()

print(type(body_result), body_result)
#print(result.status, result.reason)