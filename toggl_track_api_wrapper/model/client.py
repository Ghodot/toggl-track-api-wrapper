from datetime import datetime

from toggl_track_api_wrapper.model.entity import TogglTrackEntityFetcher, TogglTrackRawEntity

class TogglTrackClientRaw(TogglTrackRawEntity):
    archived: bool
    at: str
    id: int
    name: str
    server_deleted_at: str
    wid: int


class TogglTrackClient:
    ENDPOINT = "clients"

    def __init__(self, client_id: int) -> None:
        
        self.raw = TogglTrackClientRaw(TogglTrackEntityFetcher.fetch_from_api(self.ENDPOINT, client_id))
        self.archived = self.raw.archived
        self.at = datetime.fromisoformat(self.raw.at)
        self.id = self.raw.id
        self.name = self.raw.name
        self.server_deleted_at = None if getattr(self.raw, 'server_deleted_at', None) is None else datetime.fromisoformat(self.raw.server_deleted_at)
        self.wid = self.raw.wid
        