#!/bin/sh
#
# start the vnc server
# primarily a wrapper script to save  preferences for geometry
# and port
#
vncserver -geometry 1298x950 :9

# the vnc server config can be found in $HOME/.vnc
# for CentOS 6 (at least) the xstatup file actually starts the
# X session. I had to comment out lines at the end to get
# it to start an gnome-session

