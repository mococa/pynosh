#!/bin/bash
LOCATION="`pwd`"
PORT=8000
URL=""
TITLE="My pynosh app"
while getopts l:p:u:t: flag
do
    case "${flag}" in
        l) LOCATION=${OPTARG};;
        p) PORT=${OPTARG};;
        u) URL=${OPTARG};;
        t) TITLE=${OPTARG};;
    esac
done
cd $(dirname ${BASH_SOURCE[0]})
tmp=$(mktemp)
    jq --arg location "$LOCATION" --arg port "$PORT" --arg title "$TITLE" '.port = $port| .folderPath = $location| .isLocal = true| .windowTitle = $title' ./manifest.json > "$tmp" && mv "$tmp" manifest.json
if [[ ! -z $URL ]]; then
tmp=$(mktemp)
    jq ".url = \"$URL\"| .isLocal = false" ./manifest.json > "$tmp" && mv "$tmp" manifest.json
fi


