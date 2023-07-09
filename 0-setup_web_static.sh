#!/usr/bin/env bash
#Set Up server for web_static deployment.

sudo apt-get -y update;
#sudo apt-get -y upgrade;
sudo apt-get -y install nginx;

sudo mkdir -p /data/web_static/releases/test/;
sudo mkdir -p /data/web_static/shared/;

sudo chown -hR ubuntu:ubuntu /data;

echo "Working Perfectly" > /data/web_static/releases/test/index.html;

ln -sf /data/web_static/releases/test/ /data/web_static/current/;

sudo sed -i '7i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default;
sudo nginx -t;
sudo service nginx start;
