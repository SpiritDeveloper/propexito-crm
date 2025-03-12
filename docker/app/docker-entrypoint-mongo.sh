#!/bin/bash

# Wait until mongo logs that it's ready (or timeout after 30s)
eval "$(grep ^MONGO_DB_HOST= .env)"
eval "$(grep ^MONGO_DB_PORT= .env)"

HOST=${MONGO_DB_HOST:-'localhost'}
PORT=${MONGO_DB_PORT:-27017}

COUNTER=0
while !(nc -z $HOST $PORT) && [ $COUNTER -le 30 ] ; do
    sleep 2
    COUNTER=$((COUNTER+2))
    echo "Waiting for mongo to initialize... ($COUNTER seconds so far)"
done

if [ $COUNTER -ge 30 ]
then
    echo 'Unstarted mongo service'
    return
fi

echo 'Service MongoDB started..'

echo 'Excecuted Create user in mongo..'
python3 docker/db/docker-entrypoint-db.py
