#!/bin/bash
# sends a get request with a header variable and displays response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
