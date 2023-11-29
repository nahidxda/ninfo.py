import requests

url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"
number = input("Enter phone number: ")  # Assuming you get the phone number as input

headers = {
    "X-KM-User-AspId": "100012345612345",
    "X-KM-User-Agent": "ANDROID/1152",
    "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
    "X-KM-Accept-language": "bn",
    "X-KM-AppCode": "01",
}

params = {"msisdn": number}

response = requests.get(url, headers=headers, params=params)

print(response.text)
