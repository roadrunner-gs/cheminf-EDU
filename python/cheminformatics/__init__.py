import requests

class CheminformaticsSystem:
    def __init__(self, apiKey, RESTURL="http://gressling.net/v2/"):
        self.apiKey = apiKey
        self.RESTURL = RESTURL

    def connect(self):
        """Checks connection to the API by verifying if the status code is 200."""
        url = f"{self.RESTURL}api.php"
        query = {"apiKey": self.apiKey}
        response = requests.get(url, params=query)
        return response.status_code == 200

    def testAccess(self):
        """Retrieves data from the API if connection is successful."""
        if self.connect():
            url = f"{self.RESTURL}api.php"
            query = {"apiKey": self.apiKey}
            response = requests.get(url, params=query)
            return response.json()
        else:
            return "Connection failed"

    def testData(self):
        """Retrieves data from the API if connection is successful."""
        if self.connect():
            url = f"{self.RESTURL}api.php"
            query = {"apiKey": self.apiKey}
            response = requests.get(url, params=query)
            return response.json()
        else:
            return "Connection failed"
