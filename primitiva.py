
import requests
from requests.auth import HTTPBasicAuth


url = 'https://www.loteriasyapuestas.es/servicios/buscadorSorteos'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
params = {'game_id':'LAPR', 'celebrados':'true', 'fechaInicioInclusiva':'20200701','fechaFinInclusiva':'20200720'}

auth = HTTPBasicAuth('dsanchezsanc@uoc.edu','d1392an4Mtx23')
response = requests.get(url, params=params, headers=headers, auth = auth).json()
print(response)