#!/bin/sh

# first set up port forwarding
# ssh -L 5909:localhost:5909 -N -f user@host
# in the port specifier 5909, the last two digits refer
# to the vnc identifier and should be used at the end
# of localhost in the command below

vncviewer -encodings "copyrect hextile" localhost:9
