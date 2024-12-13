#!/bin/bash

source lib/aoc/langs.sh

sudo apt-get update
sudo apt-get install -y \
    pandoc \
    inotify-tools \
    bc \
    time