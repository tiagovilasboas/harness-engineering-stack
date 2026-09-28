# ralph-loop

Long work with a plan and a sensor that stops it. Planning without verification is a wish list. Verification without a plan is a background job.

## Shape

- Guide: the plan file (`TASK_FILE`). What the task means by done.
- Sensor: the command (`SENSOR`). Exit 0 closes the task. Anything else continues the loop.
- Control: `MAX_ITERS` bounds the loop. When the budget ends without a pass, a human decides.

## Run

```bash
cd examples/ralph-loop
printf '# Task\n- [ ] make sensor pass\n' > task.md
printf '#!/usr/bin/env bash\ntest -f done.txt\n' > sensor.sh
chmod +x ralph.sh sensor.sh

TASK_FILE=task.md SENSOR="./sensor.sh" MAX_ITERS=3 ./ralph.sh # refuses, exit 1
touch done.txt
TASK_FILE=task.md SENSOR="./sensor.sh" MAX_ITERS=3 ./ralph.sh # passes, exit 0
```

## Not this

A loop that watches a system 24/7 is a different policy with different guardrails. It never closes a task; it pages a human. Do not stretch this script into that.
