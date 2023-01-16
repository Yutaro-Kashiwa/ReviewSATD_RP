#!/bin/sh
rm -Rf /outputs/*
docker-compose build

docker-compose run --rm satd_review