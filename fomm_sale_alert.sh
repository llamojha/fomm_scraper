#!/bin/bash

DATE=$(date +"%Y-%m-%d-%H%M")
TO="YOUR_EMAIL"
SIZE="S"

python fomm.py --size ${SIZE} > fomm.html

cat fomm.html |  /usr/bin/mail -a  "Content-type: text/html;"  -s "FOMM ON SALE - ${DATE}" -aFrom:SizedFOMMServer\<noreply@llamojha.com\> ${TO}
