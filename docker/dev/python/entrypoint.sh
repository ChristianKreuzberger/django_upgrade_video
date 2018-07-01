#!/bin/bash

# check who owns the working directory
USER_ID=$(stat -c "%u" $PWD)

# set the python run uid to the user id we just retrieved
PYTHON_RUN_UID=${PYTHON_RUN_UID:=${USER_ID}}
PYTHON_RUN_USER=${PYTHON_RUN_USER:=user}
PYTHON_RUN_GROUP=${PYTHON_RUN_GROUP:=user}

# test to see if the user already exists
PYTHON_RUN_USER_TEST=$(grep "[a-zA-Z0-9\-\_]*:[a-zA-Z]:${PYTHON_RUN_UID}:" /etc/passwd)


# Update the user to the configured UID and group
if [ -n "${PYTHON_RUN_USER_TEST}" ]; then
    echo "Update user '$PYTHON_RUN_USER'"

    usermod -l ${PYTHON_RUN_USER} $(id -un ${PYTHON_RUN_UID})
    usermod -u $PYTHON_RUN_UID -g $PYTHON_RUN_GROUP $PYTHON_RUN_USER

# Else create the user with the configured UID and group
else
    echo "Create user '$PYTHON_RUN_USER'"

    # Create the user with the corresponding group
    mkdir /home/$PYTHON_RUN_USER
    groupadd $PYTHON_RUN_GROUP
    useradd -u $PYTHON_RUN_UID -g $PYTHON_RUN_GROUP -d /home/$PYTHON_RUN_USER $PYTHON_RUN_USER
    chown $PYTHON_RUN_USER:$PYTHON_RUN_GROUP /home/$PYTHON_RUN_USER
fi

export HOME=/home/$PYTHON_RUN_USER



echo "Running command '$*'"
exec su -p - ${PYTHON_RUN_USER} -s /bin/bash -c "$*"
