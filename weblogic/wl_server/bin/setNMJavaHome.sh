#!/bin/sh

# WARNING: This file is created by the Configuration Wizard.
# Any changes to this script may be lost when adding extensions to this configuration.

# *************************************************************************
#  This script is used to JAVA_HOME for NodeManager.
# *************************************************************************

BEA_JAVA_HOME=""
export BEA_JAVA_HOME

DEFAULT_BEA_JAVA_HOME=""
export DEFAULT_BEA_JAVA_HOME

SUN_JAVA_HOME="/u01/java/jdk1.8.0_202"
export SUN_JAVA_HOME

DEFAULT_SUN_JAVA_HOME="/u01/java/jdk1.8.0_202"
export DEFAULT_SUN_JAVA_HOME

if [ "${VM_TYPE}" = "JRockit" ] ; then
	JAVA_HOME="${BEA_JAVA_HOME}"
else
	if [ "${JAVA_VENDOR}" = "Sun" ] ; then
		JAVA_HOME="${SUN_JAVA_HOME}"
	else
		JAVA_VENDOR="Oracle"
		export JAVA_VENDOR
		JAVA_HOME="/u01/java/jdk1.8.0_202"
		VM_TYPE="HotSpot"
	fi
fi

JAVA_HOME="${JAVA_HOME}"
export JAVA_HOME

