#!/bin/bash
# returns size of response body
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2
