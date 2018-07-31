#!/bin/bash
# sends a GET request and displays only body of 200 response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2
