FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./

# config
RUN mkdir -p /var/www \
    && apt-get update \
    && apt-get install -y \
        build-essential \
        python-dev \
        git \
        python3-pip \
    && pip3 install -U pip

RUN pip install --no-cache-dir -r requirements.txt

python -m spacy download en

COPY . .

CMD [ "python", "./run.py" ]