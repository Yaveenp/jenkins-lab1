FROM python:3.14.0b2-alpine3.22

ENV APP_URL=$APP_URL

WORKDIR app

ENV WORKSPACE=$WORKSPACE

COPY requirments.txt .

RUN pip3 install -r requirments.txt

COPY /movies.py .

RUN rm -f requirments.txt

EXPOSE 80

CMD [ "python3", "movies.py" ]