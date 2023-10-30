from API.travel_functions import api_login, retrieve_travel_info


# DISCLAIMER
# Need to create a creds.py file within the API folder with the following keys and your own unique values
# api_key: ADD YOUR API KEY HERE
# api_secret: ADD YOUR API SECRET


if __name__ == "__main__":
    headers = api_login()
    api_response = retrieve_travel_info("SYD", "BKK", "2023-12-02", "2023-12-03", headers)
    print(api_response)