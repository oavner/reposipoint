import requests

class Repository:
    """
    Configuration for the repository.
    """

    def __init__(self, api_url, personal_access_token, repo_name, description):
        self.api_url = api_url
        self.request_headers = {
            "Authorization": f"Bearer {personal_access_token}"
        }
        self.repo_data = {
            "name": repo_name,
            "description": description,
        }

    def create(self):
        """
        Creates a repository.
        """
        response = requests.post(
            f"{self.api_url}/user/repos",
            headers=self.request_headers,
            json=self.repo_data,
        )
        return response