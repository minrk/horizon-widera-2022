FROM ubuntu:21.10
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
            texlive-xetex \
            biber \
            git \
            python3
