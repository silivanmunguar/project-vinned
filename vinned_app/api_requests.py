import requests
import environ

env = environ.Env()
environ.Env.read_env()



def getVinInfo(vin):
    url = env("BASE_URL") + vin
    headers = {
        "Accept":"application/json",
        "Authorization": env("AUTH_KEY")
    }
    response = requests.get(url, headers=headers)
    #CHECK
    # handle different reponse codes and make sure to 
    # check vin is valid before sending request
    return (response.json())



# def get_vin_info(vin):
#     url = "https://vindecoder.p.rapidapi.com/decode_vin"
#     querystring = {"vin":vin}
#     headers = {
# 	    "X-RapidAPI-Key": "6f059c07camshf4b9eb01d3197c8p124e0cjsn572a1159d1ba",
# 	    "X-RapidAPI-Host": "vindecoder.p.rapidapi.com"
#         }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     return (response.text)

# def deciodeVin_flat(vin):
#     format = "format=json"
#     url = str("https://vpic.nhtsa.dot.gov/api/vehicles/decodevinextended/" + vin + "?" + format)
#     response = requests.request("GET", url)
#     return (response)

    