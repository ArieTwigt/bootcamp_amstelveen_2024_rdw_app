import requests


def download_cars_by_brand(brand):
    '''
    Function to download cars by brand from the RDW

    Input:
    * brand: The brand you want to import

    Output:
    * list of cars
    
    '''

    # uppercase the brand
    brand_upper = brand.upper()

    # compose the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # check if the response is valid
    if response.status_code != 200:
        print("Error")

    # get the data from the response
    data = response.json()

    return data