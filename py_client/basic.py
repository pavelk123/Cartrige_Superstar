import requests


endpoint= 'http://localhost:8000/api'
#endpoint= 'http://localhost:8000/api/create_printer_producer'


get_response = requests.get(endpoint,params={'abc':123},json={"query":'Bye petuh'})
#get_response = requests.get(endpoint,params={'title':'Canon'})
print(get_response.json())