import requests

def get_distance(location1, location2):
    url = "https://distanceto.p.rapidapi.com/distance/route"

    payload = {
        "route": [
            {
                "country": "IND",
                "name": location1
            },
            {
                "country": "IND",
                "name": location2
            }
        ]
    }
    
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "34d900abadmsh45f8cb12323ccd9p1dd0d4jsnbf35c367191a",
        "X-RapidAPI-Host": "distanceto.p.rapidapi.com"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['route']['car']['distance']
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

result = get_distance("Margao", "Panjim")
print(result)
