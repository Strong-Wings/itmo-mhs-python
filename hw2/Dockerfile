FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-lang-cyrillic \
    texlive-pictures \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir latex-generator-skryzhankov

WORKDIR /app

COPY . .
RUN mkdir -p artifacts

CMD ["sh", "-c", "python main.py && pdflatex -interaction=nonstopmode -output-directory=artifacts artifacts/doc.tex"]
