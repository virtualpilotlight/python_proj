# NOTE: There are no tricks or hidden details below–simply implement what is asked.
#
# We have a web application service that we need to monitor for errors.
# The web service will output logs in the format of one JSON object per line.
# They're always well-formed JSON documents.

# The format of a log line is as follows (it has been expanded for easier reading):
pretty_json = """{
  "date": 1487963801,
  "http": {
    "verb": "POST",
    "path": "/api/v2/ninja/attack",
    "headers": {
      "Accept-Encoding": "gzip,deflate",
      "Content-Type": "application/json",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Safari/537.36",
      "DNT": 1
    },
    "status": 200
  },
  "response_time": 452,
  "request_id": "ffadad35-baf4-464d-b564-9574a8aae9f2"
}"""

# Here is a sample log file
log_json = """{ "date": 1487963801, "http": { "verb": "POST", "path": "/api/v2/ninja/attack", "headers": { "Accept-Encoding": "gzip,deflate", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36", "DNT": 1 }, "status": 200 , "response_time": 452, "request_id": "ffadad35-baf4-464d-b564-9574a8aae9f2" }}
{ "date": 1487963802, "http": { "verb": "GET", "path": "/api/v2/ninja/user/profile", "headers": { "Accept-Encoding": "gzip,deflate", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36", "DNT": 1 }, "status": 200 , "response_time": 211, "request_id": "998c33ea-e6cf-4441-a3c3-5a36cc1cd936" }}
{ "date": 1487963811, "http": { "verb": "POST", "path": "/api/v2/samurai/attack", "headers": { "Accept-Encoding": "gzip,deflate", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0", "DNT": 1 }, "status": 200 , "response_time": 1122, "request_id": "3ff9f8c0-3b25-4027-8089-66d2ad2d7536" }}
{ "date": 1487963831, "http": { "verb": "GET", "path": "/api/v2/warrior/metadata", "headers": { "Accept-Encoding": "gzip,deflate", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0", "DNT": 1 }, "status": 403 , "response_time": 352, "request_id": "c481aee6-4e41-4e07-83ef-ed1c3e583f18" }}
{ "date": 1487963919, "http": { "verb": "POST", "path": "/api/v2/ninja/attack", "headers": { "Accept-Encoding": "gzip,deflate", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36", "DNT": 1 }, "status": 500 , "response_time": 58, "request_id": "ae8fa6a8-5917-4023-ba5c-220477cda665" }}
"""

# In order to monitor the status of our web service, we should:
#
# 1. The script should take in one argument as the log file to process:
#    ./monitor '/var/log/Ninja/web.log'
#    (For the purposes of this challenge, you can load the sample log file above
#    into a multiline string variable, and pass that into your code directly.)
#
# 2. For any HTTP status code that is in the 5XX series, it should trigger
#    an alert by sending a POST request
#    with the following URL parameters: `path` (include the HTTP request path),
#    and `useragent` (include the client's user agent).
#
# 3. Add a `--tail` flag to monitor the web.log file continuously for new changes.

import json
import requests




log_json["status"]

while json_obj["status"] >= 500 And < 600:
  POST "path": , "User-Agent"
#  pass