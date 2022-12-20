#!/bin/bash
#takes URL as an argument and sends a GET request to the URL, shows body response
curl -sH "X-School-User-Id: 98" "$1"
