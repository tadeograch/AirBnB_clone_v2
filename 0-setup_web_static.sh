#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static
sudo apt-get install nginx
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
alias="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}"
sed -i "/server_name _/a $alias" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0