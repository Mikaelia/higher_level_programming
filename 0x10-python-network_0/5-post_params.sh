#!/bin/bash
# sends a post with data and displays value of response
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
