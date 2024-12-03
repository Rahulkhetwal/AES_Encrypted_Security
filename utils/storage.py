import json
import os

class StorageManager:
    FILE_PATH = "credentials.json"

    @staticmethod
    def store_credential(website, username, password):
        data = StorageManager.retrieve_credentials()
        data[website] = {"username": username, "password": password}
        with open(StorageManager.FILE_PATH, "w") as file:
            json.dump(data, file)

    @staticmethod
    def retrieve_credentials():
        if os.path.exists(StorageManager.FILE_PATH):
            try:
                with open(StorageManager.FILE_PATH, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                # If file is corrupted or empty, return an empty dictionary
                return {}
        # If file doesn't exist, return an empty dictionary
        return {}
