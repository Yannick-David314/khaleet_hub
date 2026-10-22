#!/usr/bin/env bash
cd "$(dirname "$0")" || exit 1
'.venv/bin/python' './sync.py'
if [ "$?" -ne 0 ]; then # this line checks if the exit code from syncing was not 0: if it failed, in short
    echo 'Sync failed. Not committing'
    exit 1
fi
changes=$(git status --porcelain solutions synced.json) # this is like a machine-friendly version of the git status of solutions and synced.json
timestamp=$(date '+%Y-%m-%d %H:%M:%S') # time committed
if [ -z "$changes" ]; then # this line checks if 'changes' is empty; basically nothing happened with git status so no changes
    echo 'Nothing changed. No changes to commit.'
    exit 0
fi
git add solutions synced.json # run the following git commands; your usual committing cycle
git commit -m "sync solutions $timestamp"
git push
