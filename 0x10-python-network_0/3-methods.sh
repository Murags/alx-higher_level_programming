#!/bin/bash
# shows Http methods 
curl -sIL -X OPTIONS 0.0.0.0:5000/route_4 | sed -n '6'p | cut -b 8-
