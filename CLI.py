import formatter
import argparse
import main


class CLI:
    def __init__(self) -> None:
        self.formatter: formatter.Formatter = formatter.Formatter()
        self.API: main.API_HANDLER = main.API_HANDLER()
        
        self.PARSER: argparse.ArgumentParser = argparse.ArgumentParser()
        self.PARSER.add_argument("searchRepo")
        self.PARSER.add_argument("-Q", "--query", required=True)
        
        self.ARGS = self.PARSER.parse_args()
        
        if self.ARGS.searchRepo == "searchRepo":
            search_query: str = str(self.ARGS.query)
            self.formatter.repoSearchFormatter(self.API.searchRepo(search_query))
            

if __name__ == "__main__":
    cli: CLI = CLI()

