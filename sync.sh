#!/usr/bin/env bash
'/Users/khaligula/githubfiles/khaleet_hub/.venv/bin/python' '/Users/khaligula/githubfiles/khaleet_hub/sync.py'
changes=$(git status --porcelain solutions synced.json)
timestamp=$(date '+%Y-%m-%d %H:%M:%S')
if [ -z "$changes" ]; then
    echo 'Nothing changed. No changes to commit.'
    exit 0
fi
git add solutions synced.json
git commit -m "sync solutions $timestamp"
git push
