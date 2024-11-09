import requests


class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://api.github.com/"

    def searchRepo(self, searchQuery: str) -> dict[str, str]:
        self.ENDPOINT: str = f"{self.URL}/search/repositories?q={searchQuery}"
        self.RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        self.JSON_RESPONSE: dict = dict(self.RESPONSE.json())
        
        self.USEFULL_INFO: dict[str, str] = {}
        # TODO : set this up to return insights on the dict ( after implementing getInfo function)
        for index, item in enumerate(self.JSON_RESPONSE["items"]):
            self.USEFULL_INFO.update({str(index) : item["full_name"]})

        return self.USEFULL_INFO

    def searchUser(self, searchQuery: str) -> None:
        self.ENDPOINT: str = f"{self.URL}/search/users?q={searchQuery}"
        
    def getInfo(self, owner: str, repoName: str):
        self.ENDPOINT: str = f"{self.URL}/repos/{owner}/{repoName}"
        #"fullName" : "",
        #"license" : "",
        #"htmlUrl" : "",
        #"cloneUrl" : "",
        #"language" : "",
        #"forkCounts" : "",
        #"stars" : "",
        #"watchers" : "",
        #"description" : ""


if __name__ == "__main__":
    API: API_HANDLER = API_HANDLER()
    print(API.searchRepo("Neovim"))

