# [Ln-K](https://ln-k.cf) - A minimalist link shortner

A simple no-frills link shortner, made using the django web framework. Visit [Ln-k.cf](https://ln-k.cf/) to test it out now !


## API 

In order to generate a short url, send a POST request to `https://ln-k.cf/api` with the `url` parameter.

CURL
```bash
$ curl "https://ln-k.cf/api/" -d "url=https://google.com"

{"status_code": 200, "shorturl": "https://ln-k.cf/bndrc", "message": "Short URL Created Successfully !"}
```

Python
```python
import requests

longurl = "https://google.com"
r = requests.post("http://ln-k.cf/api/", data={"url":longurl})

shorturl = r.json()['shorturl']
print(shorturl)
```


