FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY . .

RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev \
  && apk add --no-cache libxslt \
  && python setup.py install \
  && apk del .build-deps

RUN rm -r ./*

RUN addgroup -S nitter \
  && adduser -S nitter -G nitter

USER nitter

ENTRYPOINT ["python"]
CMD ["-m", "nitter"]
