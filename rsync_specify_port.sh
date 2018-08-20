# this is an example command t use rsync while specifying the
# ssh port to use
rsync -ravP --progress -e "ssh -p ${port}" ${user}@${host}:${from_path} ${to_path}
