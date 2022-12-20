#!/bin/bash
#sends a request to a URL passed as an argument and displays status code of response
curl -s -o /dev/null -I --w "%{http_code}" "$1"
