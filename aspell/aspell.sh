#!/bin/bash

# simple wrapper to run aspell on TeX files from the current proposal

set -e

DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
REPL=${DIR}/aspell.en.prepl
PWS=${DIR}/aspell.en.pws

aspell -c -t -d en_GB --personal=${PWS} --repl=${REPL} $1

