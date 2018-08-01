#!/bin/bash

set -eo

python entrypoint.py --attempts $ATTEMPTS --sleep $SLEEP --user $RABBITMQ_USER --password $RABBITMQ_PASSWORD --host $RABBITMQ_HOSTNAME --port $RABBITMQ_MANAGEMENT_PORT