#!/bin/sh

# WARNING: This file is created by the Configuration Wizard.
# Any changes to this script may be lost when adding extensions to this configuration.

# --- Start Functions ---

usage()
{
	echo "Need to set SERVER_NAME and ADMIN_URL environment variables or specify"
	echo "them in command line:"
	echo "Usage: $1 SERVER_NAME {ADMIN_URL}"
	echo "for example:"
	echo "$1 managedserver1 http://ip-172-31-42-151.ca-central-1.compute.internal:7001"
}

# --- End Functions ---

# *************************************************************************
# This script is used to start a managed WebLogic Server for the domain in
# the current working directory.  This script can either read in the SERVER_NAME and
# ADMIN_URL as positional parameters or will read them from environment variables that are 
# set before calling this script. If SERVER_NAME is not sent as a parameter or exists with a value
# as an environment variable the script will EXIT. If the ADMIN_URL value cannot be determined
# by reading a parameter or from the environment a default value will be used.
# 
#  For additional information, refer to "Administering Server Startup and Shutdown for Oracle WebLogic Server"
# *************************************************************************

#  Set SERVER_NAME to the name of the server you wish to start up.

DOMAIN_NAME="wl_server"

ADMIN_URL="http://ip-172-31-42-151.ca-central-1.compute.internal:7001"

#  Set WLS_USER equal to your system username and WLS_PW equal  

#  to your system password for no username and password prompt 

#  during server startup.  Both are required to bypass the startup

#  prompt.

WLS_USER=""
export WLS_USER

WLS_PW=""
export WLS_PW

#  Set JAVA_OPTIONS to the java flags you want to pass to the vm. i.e.: 

#  set JAVA_OPTIONS=-Dweblogic.attribute=value -Djava.attribute=value

#  set JAVA_VM=-server

JAVA_VM=""

#  Set SERVER_NAME and ADMIN_URL, they must be specified before starting

#  a managed server, detailed information can be found in

#  Administering Server Startup and Shutdown for Oracle WebLogic Server

if [ "$1" = "" ] ; then
	if [ "${SERVER_NAME}" = "" ] ; then
		usage $0
		exit
	fi
else
	SERVER_NAME="$1"
	shift
fi

if [ "$1" = "" ] ; then
	if [ "${ADMIN_URL}" = "" ] ; then
		usage $0
		exit
	fi
else
	ADMIN_URL="$1"
	shift
fi

# Export the admin_url whether the user specified it OR it was sent on the command-line

ADMIN_URL="${ADMIN_URL}"
export ADMIN_URL

SERVER_NAME="${SERVER_NAME}"
export SERVER_NAME

DOMAIN_HOME="/u01/fmw/Oracle/Middleware/Oracle_Home/user_projects/domains/wl_server"

if [ "$1" = "" ] ; then
	#  Call Weblogic Server with our default params since the user did not specify any other ones
	${DOMAIN_HOME}/bin/startWebLogic.sh nodebug noderby
else
	#  Call Weblogic Server with the params the user sent in INSTEAD of the defaults

	${DOMAIN_HOME}/bin/startWebLogic.sh $*

fi

