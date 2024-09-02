# notion-blaster

use this utility to send messages on a regular cadence using contents pulled from your notion pages

I use it to text myself daily journaling prompts -- I maintain a notion page on my phone of journaling prompts, and every day I get a text with a new prompt. helps me journal

# setup
### format your notion page correctly
<img width="787" alt="image" src="https://github.com/user-attachments/assets/47814c85-c4fb-47f1-97f8-e98bd48495d0">

this image gives a pretty good explanation, but I only wrote this script to pull top-level bulleted list items from a notion page. this is what I want personally, because I also write other notes (responses, links, etc) in my journaling prompts page which I don't want included in my text blasts

### get a notion api key
* go to https://www.notion.so/profile/integrations
* make a new integration
<img width="1226" alt="image" src="https://github.com/user-attachments/assets/75439a3a-36a5-4f24-9847-f3338dd473d4">
* copy the internal integration secret
<img width="957" alt="image" src="https://github.com/user-attachments/assets/3cc36b58-f14b-4f5f-9a78-27fa93010af5">
* give the integration access to the page you want it to read from:
<img width="1006" alt="image" src="https://github.com/user-attachments/assets/c51452b2-67a4-4fa6-8f4d-9b8f1f166875">

### set up a sender email address
you'll need to follow [this tutorial](https://wpmailsmtp.com/docs/how-to-set-up-the-other-smtp-mailer-in-wp-mail-smtp/#app-passwords) to generate an app password for this program. for now this program only supports sending from gmail addresses (but email can be sent to any address)

![image](https://github.com/user-attachments/assets/545745ad-2b1b-4913-a7f0-3fcefcba8933)

when you've generated the app password, use that password (it should be a series of 16 characters) as the ```sender_password``` value in ```config.json``` instead of your actual email password you use to log in. 

this is necessary due to increased gmail security as of mid 2022.

### set up your config
```
cp example_config.json config.json
```

then fill out the API key in `config.json` with the secret you copied from the notion site
and fill out the `page_title` value with the title of the page you want to pull from.
make sure you actually granted your API key access to this page using the steps above


### install dependencies
```
pip install -r requirements.txt
```

# running the script
```
python3 main.py
```
