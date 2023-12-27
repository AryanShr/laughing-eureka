import requests

url = "https://distanceto.p.rapidapi.com/distance/route"

payload = { "route": [
		{
			"country": "IND",
			"name": "Margao"
		},
		{
			"country": "IND",
			"name": "Panjim"
		}
	] }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "34d900abadmsh45f8cb12323ccd9p1dd0d4jsnbf35c367191a",
	"X-RapidAPI-Host": "distanceto.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())