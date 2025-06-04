import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random" 
    
    # requests.get(url)
    response = requests.get(url)
    data = response.json()
    print(data)
    
    if data["success"] and data["data"]:
        user = data["data"]
        
        username = user['login']['username']
        country = user['location']['country']
        return username, country
    else:
        print("Failed to fetch user data.")
        return None, None
    
    
def main():
    username, country = fetch_random_user()
    if username and country:
        print(f"Username: {username}, Country: {country}")
    else:
        print("No user data available.")
        
        
if __name__ == "__main__":
    main()