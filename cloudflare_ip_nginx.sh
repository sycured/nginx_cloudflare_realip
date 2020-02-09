#!/usr/bin/env bash

NOW="$(date +'%F %T')"
CFG_FILE="/etc/nginx/cloudflare.conf"

echo "# Created : "$NOW > $CFG_FILE && \
echo "" >> $CFG_FILE && \
echo "# IPv4" >> $CFG_FILE && \
curl https://www.cloudflare.com/ips-v4 | sed -e 's/^/set_real_ip_from /g' -e 's/$/;/g' >> $CFG_FILE && \
echo "" >> $CFG_FILE && \
echo "# IPv6" >> $CFG_FILE && \
curl https://www.cloudflare.com/ips-v6 | sed -e 's/^/set_real_ip_from /g' -e 's/$/;/g' >> $CFG_FILE && \
echo "real_ip_header CF-Connecting-IP;" >> $CFG_FILE && \
service nginx reload
