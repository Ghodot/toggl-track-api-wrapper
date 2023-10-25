from abc import ABC
import os

import requests
from requests.auth import HTTPBasicAuth

class TogglTrackRawEntity(ABC):
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)


class TogglTrackEntityFetcher:

    import os
    os.environ['TOGGL_TRACK_API_TOKEN'] = '*****'

    WORKSPACE_ID = 2496832
    BASE_ENDPOINT = f'https://api.track.toggl.com/api/v9'
    ENDPOINT: str

    # TODO: Easiest solution to implement, there must be a better way
    API_TOKEN = os.environ.get('TOGGL_TRACK_API_TOKEN')

    @staticmethod
    def fetch_entities(endpoint, ignore_workspace=False):
        return TogglTrackEntityFetcher.fetch_from_api(endpoint, ignore_workspace)

    @staticmethod
    def fetch_from_api(endpoint, entity_id, ignore_workspace=False) -> dict:
        if ignore_workspace:
            url = f"{TogglTrackEntityFetcher.BASE_ENDPOINT}/{endpoint}"
        else:
            url = f"{TogglTrackEntityFetcher.BASE_ENDPOINT}/workspaces/{TogglTrackEntityFetcher.WORKSPACE_ID}/{endpoint}"

        if entity_id is not None:
            url = f"{url}/{entity_id}"

        # Ugly
        if endpoint == 'workspaces':
            url = f'https://api.track.toggl.com/api/v9/workspaces/{entity_id}'

        req = requests.get(url, auth=HTTPBasicAuth(os.environ['TOGGL_TRACK_API_TOKEN'], 'api_token'), timeout=30)

        if req.ok:
            return req.json()
        else:
            raise ValueError(f'Error while fetching entity {entity_id} from endpoint {endpoint} : {req.status_code} {req.reason}')
