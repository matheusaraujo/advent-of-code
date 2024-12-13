#!/bin/bash

source lib/aoc/langs.sh

apt-get update
apt-get install -y \
    pandoc \
    inotify-tools \
    bc \
    time