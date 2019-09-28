FROM python:3.7.4-alpine
RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
  && echo 'Asia/Shanghai' >/etc/timezone
RUN pip install selenium pyyaml pytest requests pytest-repeat
CMD ["python3"]
