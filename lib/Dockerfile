FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

COPY . /usr/local/aoc

RUN /usr/local/aoc/aoc/setup.sh
RUN /usr/local/aoc/c/setup.sh
RUN /usr/local/aoc/csharp/setup.sh
RUN /usr/local/aoc/go/setup.sh
RUN /usr/local/aoc/java/setup.sh
RUN /usr/local/aoc/javascript/setup.sh
RUN /usr/local/aoc/perl/setup.sh
RUN /usr/local/aoc/python/setup.sh
RUN /usr/local/aoc/aoc/post_setup.sh

CMD ["/bin/sh", "-c", "source /home/vscode/.bashrc && exec /bin/sh"]

# TODO: @matheusaraujo - move it somewhere else
USER vscode
RUN dotnet tool install -g csharpier
