from datetime import datetime
from toggl_track_api_wrapper.model.entity import TogglTrackEntityFetcher, TogglTrackRawEntity

class TogglTrackTimeEntryRaw(TogglTrackRawEntity):

    at: str
    billable: bool
    description: str
    duration: int
    duronly: bool
    id: int
    project_id: int
    server_deleted_at: str
    start: str
    stop: str
    tag_ids: list[int]
    tags: list[str]
    task_id: int
    user_id: int
    workspace_id: int


class ToggleTrackTimeEntry:

    ENDPOINT = "time_entries"

    def __init__(self, time_entry_raw: TogglTrackTimeEntryRaw) -> None:

        self.raw = time_entry_raw
        self.at = datetime.fromisoformat(self.raw.at)
        self.billable = self.raw.billable
        self.description = self.raw.description
        self.duration = self.raw.duration
        self.duronly = self.raw.duronly
        self.id = self.raw.id
        self.project_id = self.raw.project_id
        self.server_deleted_at = None if self.raw.server_deleted_at is None else datetime.fromisoformat(self.raw.server_deleted_at)
        self.start = datetime.fromisoformat(self.raw.start)
        self.stop = None if getattr(self.raw, 'stop', None) is None else datetime.fromisoformat(self.raw.stop)
        self.tag_ids = self.raw.tag_ids
        self.tags = self.raw.tags
        self.task_id = self.raw.task_id
        self.user_id = self.raw.user_id
        self.workspace_id = self.raw.workspace_id

    @staticmethod
    def get_current_time_entry():
        return ToggleTrackTimeEntry(TogglTrackTimeEntryRaw(TogglTrackEntityFetcher.fetch_from_api('me/time_entries/current', None, ignore_workspace=True)))


if __name__ == '__main__':
    print("In module products __package__, __name__ ==", __package__, __name__)
    p = ToggleTrackTimeEntry.get_current_time_entry()
    print(p.description) # 'My Workspace