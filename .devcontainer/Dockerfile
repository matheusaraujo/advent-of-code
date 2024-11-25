FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update

# perl dependencies
RUN apt-get install -y perl libperl-critic-perl cpanminus

# python dependencies
RUN apt-get install pylint isort black -y

# cleanup
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*