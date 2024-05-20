#!/bin/sh

# Initialize the database
sqlite3 database.db < init_db.sql

# Keep the container running
exec "$@"
