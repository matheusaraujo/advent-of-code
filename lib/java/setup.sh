#!/bin/bash

# java
apt-get update
apt-get install -y openjdk-21-jdk

# google-java-format
export GJF_VERSION=1.25.0
mkdir -p /opt/google-java-format
curl -L -o /opt/google-java-format/google-java-format-${GJF_VERSION}.jar \
    "https://github.com/google/google-java-format/releases/download/v${GJF_VERSION}/google-java-format-${GJF_VERSION}-all-deps.jar"
ln -sf /opt/google-java-format/google-java-format-${GJF_VERSION}.jar /usr/local/bin/google-java-format

# pmd source code analyzer
export PMD_VERSION=7.8.0
mkdir -p /opt/pmd
curl -L -o /opt/pmd/pmd-dist-${PMD_VERSION}-bin.zip \
    "https://github.com/pmd/pmd/releases/download/pmd_releases%2F${PMD_VERSION}/pmd-dist-${PMD_VERSION}-bin.zip"
unzip /opt/pmd/pmd-dist-${PMD_VERSION}-bin.zip -d /opt/pmd
ln -sf /opt/pmd/pmd-bin-${PMD_VERSION}/bin/pmd /usr/local/bin/pmd