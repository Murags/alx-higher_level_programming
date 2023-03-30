#!/bin/bash
# shows Http methods 
curl -siL 0.0.0.0:5000/route_4 | sed -n '6'p | cut -b 8-
