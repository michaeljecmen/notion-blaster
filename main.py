import json
from notion import choose_block_from_page
from gmail import send_gmail

SUBJECT = "today's journaling prompt"

def main():
    with open("config.json") as f:
        config = json.load(f)

    message = choose_block_from_page(config["notion_api_key"], config["page_title"])
    send_gmail(config["sender_email"], config["sender_password"], config["receiver_email"], SUBJECT, message)

if __name__ == "__main__":
    main()
