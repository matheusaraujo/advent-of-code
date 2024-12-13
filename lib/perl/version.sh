#!/bin/bash

echo "[perl]"
perl --version | head -2 | tail -1

echo "[perltidy]"
perltidy --version | head -1

echo "[perlcritic]"
perlcritic --version

# TODO: @matheusaraujo, it should be done for all languages
