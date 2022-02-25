FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get -y install \
            --no-install-recommends \
            ca-certificates \
            make \
            texlive-latex-base \
            texlive-latex-recommended \
            texlive-latex-extra \
            texlive-fonts-recommended \
            texlive-bibtex-extra \
            git \
            python3
