#!/bin/bash

sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:dotnet/backports
sudo apt-get update
sudo apt-get install -y dotnet-sdk-9.0