#!/bin/bash

curl -Lo go1.23.4.linux-amd64.tar.gz https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
tar -C /usr/local -xvzf go1.23.4.linux-amd64.tar.gz
rm go1.23.4.linux-amd64.tar.gz

echo "GOROOT=/usr/local/go" >> /home/vscode/.bashrc
echo "GOPATH=/root/go" >> /home/vscode/.bashrc
echo "PATH=\$PATH:/usr/local/go/bin:\$GOPATH/bin" >> /home/vscode/.bashrc

