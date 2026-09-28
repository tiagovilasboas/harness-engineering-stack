#!/usr/bin/env bash
# Ralph loop: long-horizon work that stops when the sensor passes.
#
# The plan file is the guide. The sensor command is the feedback.
# This script only orchestrates the loop; the agent does one work step
# per iteration, then the sensor decides whether the task closed.
#
# Usage:
#   TASK_FILE=task.md SENSOR="./sensor.sh" MAX_ITERS=5 ./ralph.sh
#
# A background watch loop is another policy: it keeps watching because
# you told it to, not because a task closed. Do not use this script
# for that. This loop ends. The sensor ends it.

set -u

TASK_FILE="${TASK_FILE:?set TASK_FILE to the plan file}"
SENSOR="${SENSOR:?set SENSOR to the verification command}"
MAX_ITERS="${MAX_ITERS:-5}"

iter=0
while [ "$iter" -lt "$MAX_ITERS" ]; do
  iter=$((iter + 1))
  echo "== ralph iteration $iter/$MAX_ITERS (plan: $TASK_FILE) =="
  # Agent work step happens here, driven by the plan file.
  if sh -c "$SENSOR"; then
    echo "sensor passed. task closed."
    exit 0
  fi
  echo "sensor refused. next iteration continues from the sensor output above."
done

echo "sensor never passed after $MAX_ITERS iterations. human decides."
exit 1
