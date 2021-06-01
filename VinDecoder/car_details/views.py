from django.shortcuts import render
from django.http import HttpResponse
import requests
import json


def get_car_data(request, plate_or_vin):
    bad_input_response = {"plateNumber": "Enter Plate or VIN number !",
                          "vinNumber": "Enter Plate or VIN number !"}

    if len(plate_or_vin) < 5:
        return HttpResponse(bad_input_response)

    url = "https://api.laqo.hr/webshop/ace/api/v1/car/details"

    headers = {
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.77 Safari/537.36',
        'Content-Type': 'application/json',
    }

    payload = None

    if 4 < len(plate_or_vin) < 10:
        payload = json.dumps({
            "plateNumber": f"{plate_or_vin}"
        })

    elif len(plate_or_vin) > 9:
        payload = json.dumps({
            "vinNumber": f"{plate_or_vin}"
        })

    api_response = requests.request("POST", url, headers=headers, data=payload)
    json_response = json.loads(api_response.text)
    
    return render(request, "car_details/details.html", {"car_details": json_response})
