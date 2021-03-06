#!/bin/bash

# reference link: https://www.rabbitmq.com/install-debian.html#supported-debian-distributions
sudo apt-get update
sudo apt-key adv --keyserver "hkps.pool.sks-keyservers.net" --recv-keys "0x6B73A36E6026DFCA"
wget -O - "https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc" | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y erlang-nox
echo "deb https://dl.bintray.com/rabbitmq/debian bionic main" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list
sudo apt-get update
sudo apt-get install -y rabbitmq-server

# start the service serever
sudo service rabbitmq-server start
