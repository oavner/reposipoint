import os

class AppConfig:
    """
    Configuration for the application.
    """

    def __init__(self):
        self.port = os.getenv("PORT", "80")
        self.host = os.getenv("HOST", "localhost")
        self.personal_access_token = os.getenv("GITHUB_PERSONAL_ACCESSTOKEN")
        self.api_url = os.getenv("GITHUB_API_URL", "https://api.github.com")

        if not self.personal_access_token:
            raise ValueError("GITHUB_PERSONAL_ACCESSTOKEN is not set")
