import requests


class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://api.github.com/"

    def searchRepo(self, searchQuery: str):
        self.ENDPOINT: str = f"{self.URL}/search/repositories?q={searchQuery}"

    def searchUser(self, searchQuery: str):
        self.ENDPOINT: str = f"{self.URL}/search/users?q={searchQuery}"
        
    def getInfo(self, owner: str, repoName: str):
        self.ENDPOINT: str = f"{self.URL}/repos/{owner}/{repoName}"


if __name__ == "__main__":
    API_HANDLER()

