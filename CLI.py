import formatter
import argparse
import main


class CLI:
    def __init__(self) -> None:
        self.formatter: formatter.Formatter = formatter.Formatter()
        self.API: main.API_HANDLER = main.API_HANDLER()
        
        self.PARSER: argparse.ArgumentParser = argparse.ArgumentParser(description=
        "CLI Tool For Searching And Getting Insights Of Repositories/Users From Github")
        self.subparsers = self.PARSER.add_subparsers(title="commands", dest="command", required=True)

        self.searchRepoSubparser = self.subparsers.add_parser("searchRepo", help="Search For Repositories")
        self.searchRepoSubparser.add_argument("-q", "-query", type=str, action="store", 
                                              help="Specifies The Search Query", required=True)

        self.searchUserSubparser = self.subparsers.add_parser("searchUser", help="Search For Users")
        self.searchUserSubparser.add_argument("-q", "-query", type=str, action="store", 
                                              help="Specifies The Search Query", required=True)

        self.getInsightsSubparser = self.subparsers.add_parser("getInsights", help="Get Information For A Specific Repository")
        self.getInsightsSubparser.add_argument("-owner", type=str, action="store",
                                               help="Specifies The Owner Of The Repository", required=True)
        self.getInsightsSubparser.add_argument("-name", type=str, action="store",
                                               help="Specifies The Name Of The Repository", required=True)

        self.ARGS = self.PARSER.parse_args()

        if self.ARGS.command == "searchRepo":
            self.searchRepo()
        elif self.ARGS.command == "searchUser":
            self.searchUser()
        elif self.ARGS.command == "getInsights":
            self.getInsights()
    
    def searchRepo(self):
        search_query: str = str(self.ARGS.q)
        self.formatter.repoSearchFormatter(self.API.searchRepo(search_query))

    def searchUser(self):
        search_query: str = str(self.ARGS.q)
        self.formatter.userSearchFormatter(self.API.searchUser(search_query))

    def getInsights(self):
        repo_owner: str = str(self.ARGS.owner)
        repo_name: str = str(self.ARGS.name)
        self.formatter.infoFormatter(self.API.getInfo(repo_owner, repo_name))

if __name__ == "__main__":
    cli: CLI = CLI()

