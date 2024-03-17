# toweroffantasy.api

[toweroffantasy.api](https://api.toweroffantasy.info/redoc) was built with the intention to provide data from [Tower of Fantasy](https://www.toweroffantasy-global.com), an online Multiplayer MMORPG natively available in China and in development Globally.

Thanks to [Zakum](https://github.com/whotookzakum) who provided a subdomain, [FortOfFans](https://github.com/FortOfFans) who constantly provides game data, [Emi](https://github.com/eminentglory) who helps with the API backend, [Sova](https://github.com/Silyky) who gave permission to use his repository as an image database and others collaborators.

## How to run

> [!WARNING]
> Python version required: **3.12+**

### Steps

1. Install pdm (project manager) **`py -3.12 -m pip install pdm`**
2. Install dependecies **`pdm install --prod`** for essencials dependecies only (prod) or **`pdm install`** if you want to code or test
3. Run it using **`pdm run prod`** _(no access log)_ or **`pdm run dev`** _(access log, hot reload)_
