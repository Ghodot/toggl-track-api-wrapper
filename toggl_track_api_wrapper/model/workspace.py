from datetime import datetime

from toggl_track_api_wrapper.model.entity import TogglTrackRawEntity, TogglTrackEntityFetcher

class TogglTrackWorkspaceRaw(TogglTrackRawEntity):

    # TODO: Import all attributes
    name: str


class TogglTrackWorkspace:

    ENDPOINT = "workspaces"

    def __init__(self, workspace_id) -> None:

        self.raw = TogglTrackWorkspaceRaw(TogglTrackEntityFetcher.fetch_from_api(self.ENDPOINT, workspace_id))
        self.name = self.raw.name

if __name__ == '__main__':
    workspace = TogglTrackWorkspace(2496832)
    print(workspace.name) # 'My Workspace
