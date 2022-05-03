import os

X_RAPIDAPI_HOST = "api-football-v1.p.rapidapi.com"#os.envxiron.get("X_RAPIDAPI_HOST")
X_RAPIDAPI_KEY = "5ba265a165msh53a2d69e9a39774p1216ccjsn55c3104b0b9f"#os.environ.get("X_RAPIDAPI_KEY")

class BaseClient:
    def __init__(self) -> None:
        self.base_url = f"https://{X_RAPIDAPI_HOST}"
        self.headers = {
            "x-rapidapi-host": X_RAPIDAPI_HOST,
            "x-rapidapi-key": X_RAPIDAPI_KEY,
        }
