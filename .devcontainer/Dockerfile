FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# general dependencies
RUN apt-get update && \
    apt-get install -y \
    pandoc \ 
    inotify-tools \ 
    bc \ 
    time

# c dependencies
RUN apt-get install -y \
    clang clang-format clang-tidy

# csharp dependencies
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:dotnet/backports && \
    apt-get update && \
    apt-get install -y dotnet-sdk-9.0

# go dependencies
RUN curl -Lo go1.23.4.linux-amd64.tar.gz https://go.dev/dl/go1.23.4.linux-amd64.tar.gz && \
    tar -C /usr/local -xvzf go1.23.4.linux-amd64.tar.gz && \
    rm go1.23.4.linux-amd64.tar.gz
ENV GOROOT=/usr/local/go
ENV GOPATH=/root/go
ENV PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

# java dependencies
RUN apt-get update && \
    apt-get install -y openjdk-21-jdk

# javascript dependencies
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y \
    nodejs && \
    npm install -g eslint prettier

# perl dependencies
RUN apt-get install -y \
    perl libperl-critic-perl cpanminus

# python dependencies
RUN apt-get install -y \
    pip pylint isort black

# cleanup
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up the alias for aoc-dx
RUN echo "alias aoc='/workspaces/advent-of-code/lib/main.sh'" >> /home/vscode/.bashrc

# Add a welcome message
RUN echo '/workspaces/advent-of-code/lib/tree.sh' >> /home/vscode/.bashrc

# Start the shell with the updated .bashrc
CMD ["/bin/sh", "-c", "source /home/vscode/.bashrc && exec /bin/sh"]

# csharp additional dependencies (needs user vscode)
USER vscode
RUN dotnet tool install -g csharpier