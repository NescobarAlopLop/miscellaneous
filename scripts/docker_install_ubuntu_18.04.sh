#!/bin/bash

# source link:  https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
sudo apt update
# prereq
sudo apt install apt-transport-https ca-certificates curl software-properties-common
# gpg key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update

#apt-cache policy docker-ce
sudo apt install docker-ce

# check service status, should be active by the end of the install
sudo systemctl status docker

# add docker user to sudoes
sudo usermod -aG docker ${USER}

# to ac
su - ${USER}
