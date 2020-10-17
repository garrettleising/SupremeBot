# SupremeBot
#### Bot that utilizes Selenium to grab Supreme items

# Prerequisites

- install <a href="https://www.google.com/chrome/">Google Chrome</a>

- install <a href="https://chromedriver.chromium.org/downloads">chromedriver</a> and put it in the Drivers directory

- fill out the profile template given in Profiles directory

# Running Bot:

```
$cd SupremeBot
$pip install -r ./requirements.txt
$cd src
$python run.py
```

## Notes:

- The bot will only fetch items once it is exactly 07:59:25 Pacific Time when using Optimized Time Loop
- The bot will not click "process payment" and must be manually done 
- The template can be used as is for testing
