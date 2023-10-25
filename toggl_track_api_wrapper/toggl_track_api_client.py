import requests
import os

class TogglTrackApiClient:
    
    BASE_URL = "https://api.track.toggl.com/api/v9"

    def __init__(self, api_token:str) -> None:
        if api_token is not None:
            if not TogglTrackApiClient.test_api_token(api_token):
                raise ValueError("Invalid API token")
            os.environ['TOGGL_TRACK_API_TOKEN'] = api_token
        elif os.environ.get('TOGGL_TRACK_API_TOKEN') is not None:
            if not TogglTrackApiClient.test_api_token(os.environ.get('TOGGL_TRACK_API_TOKEN')):
                raise ValueError("Invalid API token from environment variable TOGGL_TRACK_API_TOKEN") 
        else:
            raise ValueError("No API token provided, and environment variable TOGGL_TRACK_API_TOKEN is not set")
    
    
    
    @staticmethod
    def test_api_token(api_token:str) -> bool:
        """Test if the api key is valid"""
        url = f"{TogglTrackApiClient.BASE_URL}/me"
        response = requests.get(url, auth=(api_token, "api_token"), timeout=10)
        return response.ok
    

if __name__ == "__main__":
    client = TogglTrackApiClient('*****')
    print(client.api_key)