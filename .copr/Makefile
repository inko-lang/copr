TOP := ${PWD}/build
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

srpm:
	bash ${ROOT_DIR}/../build.sh ${outdir}

.PHONY: srpm
