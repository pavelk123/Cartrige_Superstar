import requests

endpoint= 'http://localhost:8000/api/v1/catalog/cartrige/4'
#endpoint= 'http://localhost:8000/api/v1/catalog/cartrige/4/factory_printers'
endpoint= 'http://localhost:8000/api/v1/catalog/cartrige/'


#get_response = requests.get(endpoint,params={'abc':123},json={"query":'Bye petuh'})
get_response = requests.get(endpoint)

# get_response = requests.post(endpoint, json={'title':'Petro','email':'221sqqw@sdsd.df'})


print(get_response.json())