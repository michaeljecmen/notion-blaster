import json
from pprint import pprint
from notion_client import Client

def main():
    with open("config.json") as f:
        config = json.load(f)

    api_key = config["notion_api_key"]
    notion_client = Client(auth=api_key)

    page_title = config["page_title"]
    resp = notion_client.search(query=page_title)
    if len(resp['results']) == 0:
        print(f"page \"{page_title}\" not found, see readme to grant your api key access to this page")
        exit(1)

    page = resp['results'][0]
    found_title = page['properties']['title']['title'][0]['plain_text']
    page_id = page['id']
    print(f"page found with title \"{found_title}\" and id {page_id}")

    # resp = notion_client.pages.retrieve(page_id=page_id)
    # pprint(resp)

    resp = notion_client.blocks.retrieve(block_id=page_id)
    pprint(resp)



if __name__ == "__main__":
    main()