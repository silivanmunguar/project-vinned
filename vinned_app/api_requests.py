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


# def deciodeVin_flat(vin):
#     format = "format=json"
#     url = str("https://vpic.nhtsa.dot.gov/api/vehicles/decodevinextended/" + vin + "?" + format)
#     response = requests.request("GET", url)
#     return (response)

    
