Dropbox2Flickr
===
## Overview

Batch job using docker that photo/movie in my dropbox camera-upload folder transfer to flickr.

## Requirement
- docker
    - see [dockerhub](https://hub.docker.com/r/morimop/dropbox2flickr/).
- pip module
    - `pip install flicker_api` https://github.com/alexis-mignon/python-flickr-api
    - `pip install dropbox` https://github.com/dropbox/dropbox-sdk-python

### Environments
- DROPBOX_API_KEY
    - Go to https://dropbox.com/developers/apps , create an app and generate an access token.

- FLICKR_API_KEY
- FLICKR_API_SECRET
    - Go to https://www.flickr.com/services/apps/create/apply/ , create a key and secret.

- FLICKR_ACCESS_KEY
- FLICKR_ACCESS_SECRET
    - see https://github.com/alexis-mignon/python-flickr-api/wiki/Flickr-API-Keys-and-Authentication

```
>>> import os
>>> import flickr_api
>>> flickr_api.set_keys(api_key = os.environ.get("FLICKR_API_KEY"), api_secret = os.environ.get("FLICKR_API_SECRET"))
>>> a = flickr_api.auth.AuthHandler() # creates a new AuthHandler object
>>> perms = "write"
>>> url = a.get_authorization_url(perms)
>>> print url # this is the url we need!
>>> a.set_verifier("the verifier code") # copy your oauth_verifier tag here!
>>> flickr_api.set_auth_handler(a) # set the AuthHandler for the session
```

## Note
- Target dropbox folder name is in Japanese, `カメラアップロード`
- It assumes that the `processed` sub-folder already exists in the target folder.

```
/
|-- カメラアップロード
   `-- processed
```

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[morimop](https://github.com/morimop)