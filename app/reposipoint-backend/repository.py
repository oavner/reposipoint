import requests
import base64 

class Repository:
    """
    Configuration for the repository.
    """

    def __init__(self, api_url, owner, personal_access_token, repo_name, description):
        self.api_url = api_url
        self.owner = owner
        self.request_headers = {
            "Authorization": f"Bearer {personal_access_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        self.repo_data = {
            "name": repo_name,
            "description": description,
            "auto_init": True, # Creates a README.md file
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
    
    def push_local_file(self, local_path, repo_path):
        """
        Adds a file to the repository.
        """

        with open(local_path, 'rb') as file:
            file_content = file.read()

            # Encode file content to base64
            file_content = base64.b64encode(file_content)
              
        response = requests.put(
            f"{self.api_url}/repos/{self.owner}/{self.repo_data['name']}/contents/{repo_path}",
            headers=self.request_headers,
            json={
                "message": f"Added file {repo_path}",
                "content": file_content.decode('utf-8')
            }
        )
        return response
    
    def add_branch_protection(self):
        """
        Adds branch protection to the main branch.
        """
        branch_protection_data = {
            "required_status_checks": {
                "strict": True,
                "contexts": [
                    "continuous-integration"
                ]
            },
            "enforce_admins": True,
            "required_pull_request_reviews": {
                "dismiss_stale_reviews": True,
                "require_code_owner_reviews": True
            },
            "restrictions": None 
        }

        response = requests.put(
            f"{self.api_url}/repos/{self.owner}/{self.repo_data['name']}/branches/main/protection",
            headers=self.request_headers,
            json=branch_protection_data
        )
        return response