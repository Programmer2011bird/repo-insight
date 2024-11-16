from colorama import Fore
import main


class Formatter:
    def __init__(self) -> None:
        pass

    def userSearchFormatter(self):
        pass

    def repoSearchFormatter(self, JSON_DICT: dict):
        print(JSON_DICT)
        for index in range(len(JSON_DICT)):
            print(f"{'-'*25} {index} {'-'*25}")
            self.infoFormatter(JSON_DICT[index])

    def infoFormatter(self, JSON_DICT: dict):
        self.OUTPUT_STR: str = f"""
Full Name : {JSON_DICT["fullName"]}
License : {JSON_DICT["license"]}
Html Url : {JSON_DICT["htmlUrl"]}
Clonse Url : {JSON_DICT["cloneUrl"]}
Language : {JSON_DICT["language"]}
Forks : {JSON_DICT["forkCounts"]}
Stars : {JSON_DICT["stars"]}
Watchers : {JSON_DICT["watchers"]}
Description : {JSON_DICT["description"]}
"""
        print(self.OUTPUT_STR)


if __name__ == "__main__":
    formatter: Formatter = Formatter()
    API: main.API_HANDLER = main.API_HANDLER()
    
    JSON_OUTPUT: dict = API.searchRepo("neovim")
    # formatter.infoFormatter(JSON_OUTPUT)
    formatter.repoSearchFormatter(JSON_OUTPUT)
