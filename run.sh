#!/bin/bash

output_csv='output.csv'
interval=${INTERVAL:-1}

function handle_sigint() {
    source ./venv/bin/activate
    python3 generate_graph.py
    exit 1
}

trap handle_sigint SIGINT

function echo_free_mem_status() {
    local date=$(date --iso-8601=seconds)
    local free_mem=$(free -h | awk '/^Mem:/{print $4}')
    echo "${date},${free_mem}"
}

echo 'date,free-mem' > ${output_csv}
while true; do
    echo_free_mem_status >> ${output_csv}
    sleep ${interval}
done
