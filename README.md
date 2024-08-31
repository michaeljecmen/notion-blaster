# notion-blaster

use this utility to send messages on a regular cadence using contents pulled from your notion pages

I use it to text myself daily journaling prompts -- I maintain a notion page on my phone of journaling prompts, and every day I get a text with a new prompt. helps me journal

# setup
### get a notion api key
* go to https://www.notion.so/profile/integrations
* make a new integration
* copy the internal integration secret

```
cp example_config.json config.json
```

then fill out the API key in `config.json` with the secret you copied from the notion site