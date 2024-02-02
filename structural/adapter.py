class APIProvider:
    def get_data(self):
        return "Data from API"


class DatabaseConnector:
    def fetch_data_from_database(self):
        return "Data from Database"


class Adapter:
    def __init__(self, api_provider: APIProvider):
        self.api_provider = api_provider

    def fetch_data(self):
        api_data = self.api_provider.get_data()
        formatted_data = f"Converted data: {api_data}"
        return formatted_data



api_provider = APIProvider()
adapter = Adapter(api_provider)
database_data = adapter.fetch_data()
print(database_data)