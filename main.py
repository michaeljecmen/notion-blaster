import json
from pprint import pprint
from notion_client import Client

def main():
    with open("config.json") as f:
        config = json.load(f)

    api_key = config["notion_api_key"]
    notion_client = Client(auth=api_key)

    page_title = config["page_title"]
    resp = notion_client.search()
    pprint(resp)


if __name__ == "__main__":
    main()