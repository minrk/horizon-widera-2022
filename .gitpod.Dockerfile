FROM gitpod/workspace-full

# Install LaTeX
RUN sudo apt-get -q update &&     sudo apt-get install -yq --no-install-recommends \
            ca-certificates \
            make \
            latexmk \
            texlive-latex-base \
            texlive-latex-recommended \
            texlive-latex-extra \
            texlive-fonts-recommended \
            texlive-bibtex-extra \
            texlive-xetex \
            biber \
            git \
            python3 &&     sudo rm -rf /var/lib/apt/lists/*
