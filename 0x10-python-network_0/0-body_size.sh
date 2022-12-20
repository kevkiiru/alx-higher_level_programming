#!/bin/bash
#takes in a URL sends a request to URL and displays the size of body of the response
curl "$1" | wc -c
