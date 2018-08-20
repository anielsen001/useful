#!/bin/sh
#
# input ascii armored public key, output openssh format for
# authorized_keys file.
#
# ascii armormd is the format saved by putty

ssh-keygen -f $1 -i 
