FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update

# javascript dependencies
RUN apt-get install -y \
    nodejs npm

# perl dependencies
RUN apt-get install -y \
    perl libperl-critic-perl cpanminus

# python dependencies
RUN apt-get install -y \
    pip pylint isort black

# general dependencies
RUN apt-get install -y \
    pandoc inotify-tools

# cleanup
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up the alias for aoc-dx
RUN echo "alias aoc='/workspaces/advent-of-code/lib/main.sh'" >> /home/vscode/.bashrc

# Add a welcome message
RUN echo '/workspaces/advent-of-code/lib/tree.sh' >> /home/vscode/.bashrc

# Start the shell with the updated .bashrc
CMD ["/bin/sh", "-c", "source /home/vscode/.bashrc && exec /bin/sh"]