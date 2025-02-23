#!/bin/bash

docker build -t mpbot/1.0 -f Dockerfile .;
docker run mpbot/1.0;