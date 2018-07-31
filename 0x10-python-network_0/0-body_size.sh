#!/usr/bin/env bash
# returns content length of page
curl -sI 0.0.0.0:5000 | grep "Content-Length" | cut -d ' ' -f 2
