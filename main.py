import requests


class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://api.github.com/"

    def searchRepo(self, searchQuery: str) -> dict[int, dict[str, str]]:
        self.ENDPOINT: str = f"{self.URL}/search/repositories?q={searchQuery}"
        self.RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        self.JSON_RESPONSE: dict = dict(self.RESPONSE.json())
        
        self.USEFULL_INFO: dict[int, dict[str, str]] = {}
        # TODO : set this up to return insights on the dict ( after implementing getInfo function)
        # for index, item in enumerate(self.JSON_RESPONSE["items"]):
            # self.USEFULL_INFO.update({str(index) : item["full_name"]})

        return self.USEFULL_INFO

    def searchUser(self, searchQuery: str) -> dict[int, dict[str, str]]:
        self.ENDPOINT: str = f"{self.URL}/search/users?q={searchQuery}"
        self.RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        self.JSON_RESPONSE: dict = dict(self.RESPONSE.json())
        
        self.USEFULL_INFO: dict[int, dict[str, str]] = {}
        # TODO : set this up to return insights on the dict ( after implementing getInfo function)

        for index, item in enumerate(self.JSON_RESPONSE["items"]):
            self.USEFULL_INFO[index] = {
                "htmlUrl" : item["html_url"],
                "score" : item["score"],
                "reposUrl" : item["repos_url"],
                "reposCount" : str(len(requests.get(item["repos_url"]).json()))
            }

        return self.USEFULL_INFO
        
    def getInfo(self, owner: str, repoName: str):
        self.ENDPOINT: str = f"{self.URL}/repos/{owner}/{repoName}"
        self.RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        self.JSON_RESPONSE: dict = dict(self.RESPONSE.json())

        try:
            self.INSIGHTS: dict[str, str] = {
                "fullName" : self.JSON_RESPONSE["full_name"],
                "license" : self.JSON_RESPONSE["license"]["name"],
                "htmlUrl" : self.JSON_RESPONSE["html_url"],
                "cloneUrl" : self.JSON_RESPONSE["clone_url"],
                "language" : self.JSON_RESPONSE["language"],
                "forkCounts" : self.JSON_RESPONSE["forks_count"],
                "stars" : self.JSON_RESPONSE["stargazers_count"],
                "watchers" : self.JSON_RESPONSE["watchers_count"],
                "description" : self.JSON_RESPONSE["description"]
            }
        
        except TypeError or KeyError:
            self.INSIGHTS: dict[str, str] = {
                "fullName" : self.JSON_RESPONSE["full_name"],
                "license" : "null",
                "htmlUrl" : self.JSON_RESPONSE["html_url"],
                "cloneUrl" : self.JSON_RESPONSE["clone_url"],
                "language" : self.JSON_RESPONSE["language"],
                "forkCounts" : self.JSON_RESPONSE["forks_count"],
                "stars" : self.JSON_RESPONSE["stargazers_count"],
                "watchers" : self.JSON_RESPONSE["watchers_count"],
                "description" : self.JSON_RESPONSE["description"]
            }

        return self.INSIGHTS


if __name__ == "__main__":
    API: API_HANDLER = API_HANDLER()
    print(API.getInfo("Programmer2011bird", "Programmer2011bird"))

