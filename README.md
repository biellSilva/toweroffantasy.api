# api.toweroffantasy.info

**This [API](https://api.toweroffantasy.info/docs) was built with the intention of serving data from [Tower of Fantasy](https://www.toweroffantasy-global.com), an online Multiplayer MMORPG natively available in China and in development Globally.**

Thanks to [Zakum](https://github.com/whotookzakum) who provides a subdomain, [FortOfFans](https://github.com/FortOfFans) who constantly provides game data, [Emi](https://github.com/eminentglory) who helps with the API backend, [Sova](https://github.com/Silyky) who gave permission to use his repository as an image database and others collaborators.

## Packages used

* FastAPI
* Uvicorn
* Pydantic
* Python-Dotenv
* Python-Multipart
* Aiohttp

## Achievements

> **November 07, 2023** - API base goes live

## Routes

* **`/docs`**
* **`/simulacra`**
* **`/matrice`**
* **`/weapon`**
* **`/simulacra-v2`**
* **`/relic`**
* **`/food`**
* **`/item`**
* **`/assets`**

### Example of use

Let's say we made a request for one of the routes (except `/assets`), if we don't specify an ID using just `/route`, the return will be a dictionary containing all the information for that route

*status code: 200*

```json
{
   "object_id": {
	"keys": "values"
   },
   "object_id": {
	"keys": "values"
    }
}
```

But in case we only want a specific object, then we use **`/route/id`** but this route has a validation system, if the ID doesn't exist it returns error **404** (not found) or **423** (error validation on ID)

_status code: 200_

```json
{
   "key_1": "value_1",
   "key_2": "value_2"
}
```

### Language system
All routes also have a system to define which language should be returned, for this query params were used, in the request url you must pass **`/route?lang=possible_languages`**, can also be used in a route for a specific object **`/route/id?lang=possible_language`**

All possible languages are the folders name in **`/api/database`**

### /assets
All objects that have icons/assets are modified to facilitate their access
for example Ling Han object, the key "icon" has the value of **"/assets/UI/huanxing/lihui/linghan"** this is its path in the API, to facilitate "access" we are talking about you just needing to add the icon string in the API URI **"https://api.toweroffantasy.info/assets/UI/huanxing/lihui/linghan"**

<a href="url"><img src="https://api.toweroffantasy.info/assets/UI/huanxing/lihui/linghan" align="center" width="350"></a>


### Note
It's possible to use the [API Docs](https://api.toweroffantasy.info/docs) to check/learn on how to use, their returns and more

## Development checklist

* [X] simulacras
* [X] matrices
* [X] weapons
* [X] relics
* [X] foods
* [X] items
* [X] assets
* [ ] achievements
* [ ] currency
* [ ] outfits
