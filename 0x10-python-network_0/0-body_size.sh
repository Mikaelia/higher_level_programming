#!/bin/bash
# returns size of response body
curl -sI 0.0.0.0:5000 | grep "Content-Length" | cut -d ' ' -f 2
