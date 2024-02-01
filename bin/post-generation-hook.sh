#!/usr/bin/env bash

SCRIPT_DIR=$(dirname "$0")
PROJECT_ROOT=$(realpath "${SCRIPT_DIR}/..")  # expects script in bin/
PATH=${PROJECT_ROOT}/venv/Scripts:$PATH  # expects python environment in venv/
command -v black >/dev/null 2>&1 || { echo >&2 "'black' required, but not found. Please read 'Local installation' section in ${PROJECT_ROOT}/CONTRIBUTING.md file. Aborting."; exit 1; }
command -v flake8 >/dev/null 2>&1 || { echo >&2 "'flake8' required, but not found. Please read 'Local installation' section in ${PROJECT_ROOT}/CONTRIBUTING.md file. Aborting."; exit 1; }
cd "${PROJECT_ROOT}" && black xero_python && flake8 xero_python

# python bin/get_yaml_value.py "${1}" "packageVersion" | xargs python ./bin/bumpversion.py

python ./bin/bumpversion.py $2
