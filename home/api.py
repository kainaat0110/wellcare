import requests

url = "https://random-quote-generator2.p.rapidapi.com/randomQuote"

headers = {
	"X-RapidAPI-Key": "5ec58a8951msh6037fd61df3ce40p154017jsn35c800320e1b",
	"X-RapidAPI-Host": "random-quote-generator2.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)