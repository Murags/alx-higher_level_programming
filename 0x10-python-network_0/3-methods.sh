#!/bin/bash
# shows Http methods 
curl -sI -X OPTIONS "$1" | awk -v RS='\r?\n' '/^Allow: / {gsub(/^Allow: /,""); print}'
