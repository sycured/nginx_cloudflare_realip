# nginx_cloudflare_realip
to obtain real ip when using cloudflare in front of nginx

# INSTALLATION

## Python 3 version

Copy the script file to /opt

    cp cloudflare_ip_nginx.py /opt/

Add this line at the end of the file `/etc/nginx/nginx.conf`

    include /etc/nginx/cloudflare.conf;

Add this line in the `/etc/crontab`

    0 2 * * * root /opt/cloudflare_ip_nginx.py

And finally, start it manually for the first time and restart nginx

    /opt/cloudflare_ip_nginx.py && service nginx restart

## Shell version

Copy the script file to /opt

    cp cloudflare_ip_nginx.sh /opt/

Add this line at the end of the file `/etc/nginx/nginx.conf`

    include /etc/nginx/cloudflare.conf;

Add this line in the `/etc/crontab`

    0 2 * * * root /opt/cloudflare_ip_nginx.sh

And finally, start it manually for the first time and restart nginx

    /opt/cloudflare_ip_nginx.sh && service nginx restart
