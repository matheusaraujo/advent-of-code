#/bin/bash

apt-get clean
rm -rf /var/lib/apt/lists/*

echo "alias aoc='/usr/local/aoc/main.sh'" >> /home/vscode/.bashrc
echo '/usr/local/aoc/tree.sh' >> /home/vscode/.bashrc