from typing import Any, Dict

X_RAPIDAPI_IMG_SEARCH_HOST = "bing-image-search1.p.rapidapi.com"

from notifier.src.api_clients.base_client import X_RAPIDAPI_KEY, BaseClient
from notifier.src.api_request import APIRequest


class ImagesSearchClient:
    def __init__(self) -> None:
        super().__init__()
        self.base_url = f"https://{X_RAPIDAPI_IMG_SEARCH_HOST}"
        self.headers = {
            "x-rapidapi-host": X_RAPIDAPI_IMG_SEARCH_HOST,
            "x-rapidapi-key": X_RAPIDAPI_KEY,
        }
        self.endpoint = "/images/search"
        self.request = APIRequest()

    def get_images(self, search_query: str) -> Dict[str, Any]:
        params = {"q": search_query}
        url = f"{self.base_url}{self.endpoint}"

        return self.request.get(url, params, self.headers)
