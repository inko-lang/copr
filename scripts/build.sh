#!/usr/bin/env bash

set -e

top="${PWD}/build"

if ! command -v spectool
then
    dnf --quiet --assumeyes install rpmdevtools
fi

spectool --define "_topdir ${top}" -gR *.spec

if [[ -d sources ]]
then
    cp -r sources/* "${top}/SOURCES"
fi

rpmbuild --define "_topdir ${top}" -bs *.spec
mv "${top}"/SRPMS/*.src.rpm "${1}"
