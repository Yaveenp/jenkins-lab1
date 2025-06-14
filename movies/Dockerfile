FROM python:3.14.0b2-alpine3.22

ENV APP_URL=$APP_URL

WORKDIR app

EXPOSE 80

COPY requirments.txt ../movies-api

RUN pip install -r requirments.txt

COPY movies.py ../movies-api 

RUN rm -f requirments.txt

CMD [ "python", "movies.py" ]