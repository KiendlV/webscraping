import requests
import json

def weather_call():

	url = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q":"48.1764882,11.2508035"}

	headers = {
	"X-RapidAPI-Key": "01f825439bmshaaaac3b6218c71bp198cd1jsn058176e929ec",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	with open("archive.json", "w") as handle :
		json.dump(
		{"real" : realPart,
		"imag" : imaginaryPart,
		"dict" : dictionary},
		handle
		)

		with open("archive.json", "r") as handle :
		jsonObjectse = json.load(handle)

	print(response.json())
	#with ("weather_bruck.json", "w") as file:
	#	json.dump(response.json(), file)

