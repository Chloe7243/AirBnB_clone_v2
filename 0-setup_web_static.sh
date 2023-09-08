#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if [[ "$(type nginx > /dev/null; echo $?)" != '0' ]]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

sudo service nginx start
sudo mkdir -p "/data/web_static/releases/test" "/data/web_static/shared"
sudo bash -c "echo '<h1>Hello World!</h1>' > /data/web_static/releases/test/index.html"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
sudo chown -hR ubuntu:ubuntu "/data"

static_block="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
if [[ "$(grep -c 'location /hbnb_static {' '/etc/nginx/sites-available/default')" -lt '1' ]]; then
    sudo sed -i "/error_page 404 /a${static_block}" "/etc/nginx/sites-available/default"
fi
sudo service nginx restart
