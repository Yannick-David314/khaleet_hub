#!/usr/bin/env bash
cd "$(dirname "$0")" || exit 1
timestamp=$(date '+%Y-%m-%d %H:%M:%S') # time committed
echo "=== $timestamp ===" 
'.venv/bin/python' './sync.py'
if [ "$?" -ne 0 ]; then # this line checks if the exit code from syncing was not 0: if it failed, in short
    echo 'Sync failed. Not committing'
    osascript -e 'display notification "Sync failed: cookies may be stale. See sync.log" with title "khaleet"'
    exit 1
fi
changes=$(git status --porcelain solutions synced.json) # this is like a machine-friendly version of the git status of solutions and synced.json
if [ -n "$changes" ]; then # this line checks if 'changes' is non-empty; basically something happened with git status so there were changes
    git add solutions synced.json # run the following git commands; part of your usual committing cycle
    git commit -m "sync solutions $timestamp"
else
    echo 'Nothing changed. No changes to commit.'
fi

git push || osascript -e 'display notification "Could not push. Poor internet" with title "khaleet"'
