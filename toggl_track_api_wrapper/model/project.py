from datetime import datetime

from toggl_track_api_wrapper.model.entity import TogglTrackRawEntity, TogglTrackEntityFetcher
from toggl_track_api_wrapper.model.workspace import TogglTrackWorkspace
from toggl_track_api_wrapper.model.client import TogglTrackClient

class TogglTrackProjectRaw(TogglTrackRawEntity):
    active: bool
    actual_hours: int
    actual_seconds: int
    at: str
    auto_estimates: bool
    billable: bool
    client_id: int
    color: str
    created_at: str
    currency: str
    current_period: str
    end_date: str
    estimated_hours: int
    estimated_seconds: int
    first_time_entry: str
    fixed_fee: int
    id: int
    is_private: bool
    name: str
    rate: int
    rate_last_updated: str
    recurring: bool
    recurring_parameters: str
    server_deleted_at: str
    start_date: str
    template: bool
    workspace_id: int


class TogglTrackProject:

    ENDPOINT = "projects"

    raw: TogglTrackProjectRaw
    active: bool
    actual_hours: int
    actual_seconds: int
    at: datetime
    auto_estimates: bool
    billable: bool
    client: TogglTrackClient
    color: str
    created_at: datetime
    currency: str
    current_period: str
    end_date: datetime
    estimated_hours: int
    estimated_seconds: int
    first_time_entry: str
    fixed_fee: int
    id: int
    is_private: bool
    name: str
    rate: int
    rate_last_updated: str
    recurring: bool
    recurring_parameters: str
    server_deleted_at: datetime
    start_date: datetime
    template: bool
    workspace: TogglTrackWorkspace

    def __init__(self, project_id) -> None:

        self.raw = TogglTrackProjectRaw(TogglTrackEntityFetcher.fetch_from_api(self.ENDPOINT, project_id))
        self.active = self.raw.active
        self.actual_hours = self.raw.actual_hours
        self.actual_seconds = self.raw.actual_seconds
        self.at = self.raw.at
        self.auto_estimates = self.raw.auto_estimates
        self.billable = self.raw.billable
        self.client = TogglTrackClient(self.raw.client_id)
        self.color = self.raw.color
        self.created_at = datetime.fromisoformat(self.raw.created_at)
        self.currency = self.raw.currency
        self.current_period = self.raw.current_period
        self.end_date = None if getattr(self.raw, 'end_date', None) is None else datetime.fromisoformat(self.raw.end_date)
        self.estimated_hours = None if getattr(self.raw, 'estimated_hours', None) is None else self.raw.estimated_hours
        self.estimated_seconds = None if getattr(self.raw, 'estimated_seconds', None) is None else self.raw.estimated_seconds
        self.first_time_entry = None if getattr(self.raw, 'first_time_entry', None) is None else self.raw.first_time_entry
        self.fixed_fee = self.raw.fixed_fee
        self.id = self.raw.id
        self.is_private = self.raw.is_private
        self.name = self.raw.name
        self.rate = self.raw.rate
        self.rate_last_updated = None if getattr(self.raw, 'rate_last_updated', None) is None else datetime.fromisoformat(self.raw.rate_last_updated)
        self.recurring = self.raw.recurring
        self.recurring_parameters = self.raw.recurring_parameters
        self.server_deleted_at = None if getattr(self.raw, 'server_deleted_at', None) is None else datetime.fromisoformat(self.raw.server_deleted_at)
        self.start_date = None if getattr(self.raw, 'server_deleted_at', None) is None else datetime.fromisoformat(self.raw.server_deleted_at)
        self.template = self.raw.template
        self.workspace = TogglTrackWorkspace(self.raw.workspace_id)

if __name__ == '__main__':
    print("In module products __package__, __name__ ==", __package__, __name__)
    p = TogglTrackProject(165499986)
    print(p.name) # 'My Workspace
    