FROM python:3.10
COPY . /mp-bot
WORKDIR /mp-bot
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]