#!/bin/bash
export ZULU_11_HOME="/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home"
export JAVA_HOME=$ZULU_11_HOME

export PATH=${JAVA_HOME}/bin:${PATH}

java -version
sleep 1

jconsole