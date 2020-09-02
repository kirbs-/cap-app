#!/bin/bash
set -e

# Setup database
flask db upgrade

flask run --host=0.0.0.0 