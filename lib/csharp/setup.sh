#!/bin/bash

apt-get install -y software-properties-common
add-apt-repository ppa:dotnet/backports
apt-get update
apt-get install -y dotnet-sdk-9.0