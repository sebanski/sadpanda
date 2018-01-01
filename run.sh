#!/bin/bash
#
# a modern installer for docker on different clients 

# NOTE: a work in progress
OS_VERSION="linux" # sudo mname or something like that
#TODO: run a pick your os program
DOCKER_VERSION="3.7.1"

if [ [ -f $OS_VERSION == "linux" ] ] ; then
	useradd docker -g docker
	mkdir /usr/local/docker
	mkdir /usr/local/docker/docker
	wget https://docker.io./docker/download/latest -O /usr/local/docker/
	chown -R docker:docker /usr/local/docker
	ln -s /usr/local/docker/docker /usr/local/docker/docker-$DOCKER_VERSION
	echo <<
[Unit]

ExecStart=/usr/local/docker/docker/bin/dockerd -d -ZzZzZzZzZzZzZzZzZzZzZzZzZzZz 
	>> /usr/lib/systemd/system/dockerd.service	
; fi

if [ [ -f $OS_VERSION == "mac os x" ] ] ; then
		
	; 
fi



