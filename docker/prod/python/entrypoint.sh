#!/bin/bash

echo "Running command '$*'"
exec /bin/bash -c "$*"
