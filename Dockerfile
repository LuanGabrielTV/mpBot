FROM python:3.10
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
COPY . ./app
WORKDIR /app
CMD [ "python", "bot.py" ]