FROM python:3.10
COPY ./ /mp-bot
COPY requirements.txt /mp-bot/requirements.txt
WORKDIR /mp-bot
RUN pip install -r requirements.txt
CMD [ "python", "./main.py" ]