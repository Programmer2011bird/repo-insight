import requests


class API_HANDLER:
    def __init__(self) -> None:
        self.URL: str = "https://api.github.com/"

    def searchRepo(self, searchQuery: str) -> dict[int, dict[str, str]]:
        self.ENDPOINT: str = f"{self.URL}/search/repositories?q={searchQuery}"
        self.RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        self.JSON_RESPONSE: dict = dict(self.RESPONSE.json())
        
        self.USEFULL_INFO: dict[int, dict[str, str]] = {}
        
        for index, item in enumerate(self.JSON_RESPONSE["items"]):
            
            try:
                self.INSIGHTS: dict[str, str] = {
                    "fullName" : item["full_name"],
                    "license" : item["license"]["name"],
                    "htmlUrl" : item["html_url"],
                    "cloneUrl" : item["clone_url"],
                    "language" : item["language"],
                    "forkCounts" : item["forks_count"],
                    "stars" : item["stargazers_count"],
                    "watchers" : item["watchers_count"],
                    "description" : item["description"]
                }

            except TypeError or KeyError:
                self.INSIGHTS: dict[str, str] = {
                    "fullName" : item["full_name"],
                    "license" : "null",
                    "htmlUrl" : item["html_url"],
                    "cloneUrl" : item["clone_url"],
                    "language" : item["language"],
                    "forkCounts" : item["forks_count"],
                    "stars" : item["stargazers_count"],
                    "watchers" : item["watchers_count"],
                    "description" : item["description"]
                }

            self.USEFULL_INFO.update({index : self.INSIGHTS})

        return self.USEFULL_INFO

    def searchUser(self, searchQuery: str) -> dict[int, dict[str, str]]:
        self.ENDPOINT: str = f"{self.URL}/search/users?q={searchQuery}"
        self.RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        self.JSON_RESPONSE: dict = dict(self.RESPONSE.json())
        
        self.USEFULL_INFO: dict[int, dict[str, str]] = {}

        for index, item in enumerate(self.JSON_RESPONSE["items"]):
            self.USEFULL_INFO[index] = {
                "htmlUrl" : item["html_url"],
                "score" : item["score"],
                "reposUrl" : item["repos_url"],
                "reposCount" : str(len(requests.get(item["repos_url"]).json()))
            }


        return self.USEFULL_INFO

    def getInfo(self, owner: str, repoName: str) -> dict[str, str]:
        self.ENDPOINT: str = f"{self.URL}/repos/{owner}/{repoName}"
        self.RESPONSE: requests.Response = requests.get(self.ENDPOINT)
        self.JSON_RESPONSE: dict = dict(self.RESPONSE.json())

        print(self.JSON_RESPONSE)

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
