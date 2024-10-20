#!/bin/bash

docker compose -f ./docker-compose/docker-compose.base.yml up --build --force-recreate --remove-orphans
