# notion-blaster

use this utility to send messages on a regular cadence using contents pulled from your notion pages

I use it to text myself daily journaling prompts -- I maintain a notion page on my phone of journaling prompts, and every day I get a text with a new prompt. helps me journal

# setup
### get a notion api key
* go to https://www.notion.so/profile/integrations
* make a new integration
<img width="1226" alt="image" src="https://github.com/user-attachments/assets/75439a3a-36a5-4f24-9847-f3338dd473d4">
* copy the internal integration secret
<img width="957" alt="image" src="https://github.com/user-attachments/assets/3cc36b58-f14b-4f5f-9a78-27fa93010af5">
* give the integration access to the page you want it to read from:
<img width="1006" alt="image" src="https://github.com/user-attachments/assets/c51452b2-67a4-4fa6-8f4d-9b8f1f166875">


```
cp example_config.json config.json
```

then fill out the API key in `config.json` with the secret you copied from the notion site
