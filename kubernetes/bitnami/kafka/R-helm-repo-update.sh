#!/bin/sh
helm repo list
sleep 1
echo 'Updating ...'
helm repo update
