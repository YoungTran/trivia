FROM nikolaik/python-nodejs:python3.7-nodejs13-alpine

COPY ./frontend /trivia42/frontend

WORKDIR /trivia42/frontend

RUN yarn

RUN yarn build

COPY ./backend /trivia42/backend

WORKDIR /trivia42/backend

RUN apk update && \
  apk add --virtual build-deps gcc python-dev musl-dev && \
  apk add postgresql-dev

RUN pip install -r requirements.txt
ENV FLASK_RUN_PORT=5000
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
EXPOSE 5000

CMD ["flask", "run", "--host","0.0.0.0", "--port", "5000"]
