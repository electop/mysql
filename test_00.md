These scopes are incompatible with AAR
         (Android ARchive) packages and will cause a build with AAR packages to fail.
#3695dd #e7f5fd
```code
"settings": [
  {
    "id": "myOauthSetting",
    "name": "Authenticate with the third party service",
    "description": "Tap to set",
    "type": "OAUTH",
    " urlTemplate : "https://accounts.artik.cloud/authorize?
prompt=login&client_id=2134rwer34&response_type=code
&redirect_uri=https%3A%2F%2Fapi.smartthings.com
%2Foauth%2Fcallback", "
  }
]
```
