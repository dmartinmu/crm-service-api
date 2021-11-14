#!/bin/bash
set -e

# Execute update scripts
FILES=/db/sql_structure/*
for f in $FILES
do
  echo "Processing $f file..."
  psql -U "$POSTGRES_USER" -d crm -a -f $f
done

# Execute tests initialization scripts
FILES=/db/sql_test/*
for f in $FILES
do
  echo "Processing $f file..."
  psql -U "$POSTGRES_USER" -d crm -a -f $f
done


