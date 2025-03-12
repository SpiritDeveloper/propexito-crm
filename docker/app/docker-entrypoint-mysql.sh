#!/bin/sh

# Wait until MySQL is ready
while ! mysqladmin ping -h"db" -P"3307" --silent; 
do
    echo "Flask waiting for MySQL to be up..."
    sleep 1
done