#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument and
# displays the boyd of the response

curl -X DELETE "$1" -s