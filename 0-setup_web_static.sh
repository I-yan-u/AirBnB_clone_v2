#!/usr/bin/env bash
# Installs Nginx if not installed
#+ Creates folders /data/web_static/shared
#+	and /adta/releases/test if not exists
#+ /data/web_static/current linked to
#+ /data/web_static/releases/test/
#+ Creates an /data/web_static/releases/test/index.html
#+ Configures Nginx to serve /data/web_static/current/
#+	to hbnb_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
echo "<html><head></head><body>Yay!!!</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo sed -i -e '$i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/; \n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
