from functions.download_functions import download_cars_by_brand
from functions.conversion_functions import convert_to_df

# download the cars from the RDW
cars_list = download_cars_by_brand("volvo")

# convert the list to a pandas DataFrame
convert_to_df(cars_list)

pass