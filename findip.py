import requests
import argparse

parser = argparse.ArgumentParser(description="Programa feito para realizar consultas de ip")
parser.add_argument('--ip', type=str, required=True)

args = parser.parse_args()

r = requests.get(f'http://ip-api.com/json/{args.ip}')
data = r.json()

if data["status"] == "fail":
    print("Erro ao consultar ip")
else:
    print(f'''
Consulta realizada com sucesso!
Country: {data["country"]}
City: {data["city"]}
Latitude: {data["lat"]}
Longitude: {data["lon"]}
isp: {data["isp"]}
org: {data["org"]}
asn: {data["as"]}
''')




