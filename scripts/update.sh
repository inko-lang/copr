#!/usr/bin/env bash

# Usage: update.sh NAME VERSION HOOK
set -e

function info() {
    echo -e "\\033[1m\\033[32m>>>\\033[0m\\033[0m ${1}"
}

if [[ -v CI ]]
then
    info 'Configuring Git'
    git config --global user.email noreply@inko-lang.org
    git config --global user.name 'Inko bot'
    git config --global --add safe.directory '*'
fi

info 'Updating RPM spec'
sed -i "${1}.spec" -r -e "s/^Version:.+$/Version: ${2}/g"

info 'Committing changes'
git add "${1}.spec"
git commit -m "Update ${1} to version ${2}"

info 'Pushing changes'

for _ in {1..3}
do
    git push origin main && break
done

info 'Notifying Copr'
curl -X "${3}"
