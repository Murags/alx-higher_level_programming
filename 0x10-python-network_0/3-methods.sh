#!/bin/bash
# shows Http methods 
curl -siL -X OPTIONS "$1" | sed -n '6'p | cut -b 8-
