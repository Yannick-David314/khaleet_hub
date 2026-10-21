#!/usr/bin/env bash
'/Users/khaligula/githubfiles/khaleet_hub/.venv/bin/python' '/Users/khaligula/githubfiles/khaleet_hub/sync.py'
changes=$(git status --porcelain solutions synced.json)
if [ -z "$changes" ]; then
    echo 'Nothing changed. No changes to commit.'
    exit 0
fi