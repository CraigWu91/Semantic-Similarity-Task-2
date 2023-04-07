FROM pypy:latest
WORKDIR /app
COPY . /app

COPY requirements.txt requirements.txt
COPY movies.txt movies.txt
RUN pip install -r requirements.txt

COPY . .

CMD python watch_next.py