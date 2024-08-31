import random
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

    # concat all resulting blocks from paginated responses
    blocks = []

    # handle pagination with has_more on this response object
    next_cursor = None
    has_more = True
    while has_more:
        resp = notion_client.blocks.children.list(block_id=page_id, start_cursor=next_cursor)
        
        has_more = resp['has_more']
        next_cursor = resp['next_cursor']

        results = resp['results']

        # need to get different types of blocks differently
        for r in results:
            type = r['type']
            if type == 'bulleted_list_item':
                text = r['bulleted_list_item']['rich_text'][0]['plain_text']
            else:
                print(f"found block type {type}, dropping it")
                continue
            
            text = text.strip()
            blocks.append(text)

    print(f"found {len(blocks)} blocks")
    # pprint(blocks)
    chosen_block = random.choice(blocks)
    print(f"chosen block: {chosen_block}")

if __name__ == "__main__":
    main()