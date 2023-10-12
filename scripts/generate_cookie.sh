#!/bin/bash

set -evx

#
# Generate a cookiecutter version of this repository
#
COOKIE=https://github.com/kiwi-lang/PythonTemplate.git

git config --global user.email "GithubAction@example.com"
git config --global user.name "GithubAction"

# remove the folders we do not want to copy
rm -rf .tox
rm -rf PythonTemplateExample.egg-info
rm -rf cifar10.lock
rm -rf PythonTemplateExample/__pycache__
rm -rf PythonTemplateExample/models/__pycache__
rm -rf PythonTemplateExample/tasks/__pycache__

# dest=$(mktemp -d)
dest=../PythonTemplateGen

# Get the latest version of the cookiecutter
# git clone $COOKIE $dest

# Copy the current version of our code in the cookiecutter
COOKIED=$dest/'{{cookiecutter.project_name}}'
mkdir -p $COOKIED

# Copy this repo to the cookie
rsync -av --progress . $COOKIED/                                \
    --exclude .git                                              \
    --exclude __pycache__

# The basic configs
cat > $dest/cookiecutter.json <<- EOM
{
    "project_name": "myproject",
    "github": "myusername",
    "author": "Anonymous",
    "email": "anony@mous.com",
    "description": "Python seed project for productivity",
    "copyright": "2021",
    "url": "http://github.com/test",
    "version": "0.0.1",
    "license": "BSD 3-Clause License",
    "_copy_without_render": [
        "dependencies",
        ".github"
    ]
}
EOM

# Remove the things we do not need in the cookie
rm -rf $COOKIED/scripts/generate_cookie.sh
rm -rf $COOKIED/.github/workflows/openpr.yaml
rm -rf $COOKIED/.git
 
# Find the instance of all the placeholder variables that
# needs to be replaced by their cookiecutter template

cat > mappings.json <<- EOM
    [
        ["TemplateExample", "project_name"],
        ["TemplateAuthor", "author"],
        ["TemplateLicense", "license"],
        ["TemplateEmail", "email"],
        ["TemplateDescription", "description"],
        ["1234", "copyright"],
        ["TemplateUrl", "url"],
        ["0.0.1", "version"],
        ["TemplateGithub", "github"],
        ["TemplateRepo", "github_repo"]
    ]
EOM

jq -c '.[]' mappings.json | while read i; do
    oldname=$(echo "$i" | jq -r -c '.[0]')
    newname=$(echo "$i" | jq -r -c '.[1]')

    echo "Replacing $oldname by $newname"
    find $COOKIED -type f -print0 | xargs -0 sed -i -e "s/$oldname/\{\{cookiecutter\.$newname\}\}/g"
done
rm -rf mappings.json

# Move project folder with its new name
rsync -av --remove-source-files --progress $COOKIED/TemplateExample/ $COOKIED/'{{cookiecutter.project_name}}'/

# Push the change
#   use the last commit message of this repository  for the  cookiecutter

PREV=$(pwd)
MESSAGE=$(git show -s --format=%s)

git checkout master
git checkout -b auto

# Copy back 
rsync -av --remove-source-files --progress $COOKIED .

if [ -n "$(git diff --exit-code)" ]; then
    git add --all
    git commit -m "$MESSAGE"
    git push origin auto

    if which gh &> /dev/null; then
        gh pr create -B master -H auto --title 'Auto Sync' --body 'Created by Github action'
    fi
else
    echo "Nothing to commit exit"
fi
