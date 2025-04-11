import requests


import json


class ResponseHandler:
    @staticmethod
    def handle(response: requests.Response,
               success_message: Optional[str] = None,
               display_json: bool = False) -> None:
        if response.ok:
            if success_message:
                print(f"✓ {success_message}")
            if display_json:
                print(json.dumps(response.json(), indent=2))
        else:
            try:
                error_msg = response.json().get("detail", response.text)
            except:
                error_msg = response.text
            print(f"✗ Error {response.status_code}: {error_msg}")