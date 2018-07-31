#!/bin/bash
# sends a DELETE request
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
