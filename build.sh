#!/bin/bash

#get highest tag number
VERSION=`git describe --abbrev=0 --tags`

#get number parts and increase last one by 1
VNUM1=$(echo "$VERSION" | cut -d"." -f1)
VNUM2=$(echo "$VERSION" | cut -d"." -f2)
VNUM3=$(echo "$VERSION" | cut -d"." -f3)
VNUM1=`echo $VNUM1 | sed 's/v//'`

# Check for #major or #minor in commit message and increment the relevant version number
MAJOR=`git log --format=%B -n 1 HEAD | grep '#major'`
MINOR=`git log --format=%B -n 1 HEAD | grep '#minor'`

if [ "$MAJOR" ]; then
    echo "Update major version"
    VNUM1=$((VNUM1+1))
    VNUM2=0
    VNUM3=0
elif [ "$MINOR" ]; then
    echo "Update minor version"
    VNUM2=$((VNUM2+1))
    VNUM3=0
else
    echo "Update patch version"
    VNUM3=$((VNUM3+1))
fi

#create new tag
NEW_TAG="$VNUM1.$VNUM2.$VNUM3"

git tag $NEW_TAG

docker build --no-cache --file Dockerfile.build --build-arg AGVERSION=$NEW_TAG --tag cpu_load_build .
docker run --rm -v $(pwd):/dist cpu_load_build
