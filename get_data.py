import requests

def get_request(api_url):
    try:
        # GET request to the API
        response = requests.get(api_url)

        # Check if request is successful
        if response.status_code == 200:
            print("GET Request successful")
            with open("exoplanet_data.csv", "w", encoding="utf-8") as file:
                file.write(response.text)
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Endpoint
    api_url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,sy_snum,sy_pnum,sy_mnum,cb_flag,discoverymethod,disc_year,disc_facility,pl_orbper,pl_rade,pl_masse,pl_dens,st_age,sy_dist+from+ps&format=csv"

    get_request(api_url)
