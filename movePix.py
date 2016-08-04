#!/usr/bin/env python
#
# This script reads the EXIF meta data from an image
# and then copies the image to a directory for the date
# in which in the image was collected. If the destination
# file already exists (based on name) nothing is done.
#
# syntax:
# ./movePix <dir to copy to> <file name> [<more file names>]
#
# use with find like this:
# (find /media/0000-3562 -iname  "*jpg" -print0 | xargs -0 ../code/movePix.py /mnt/syn/photo ) | tee copy.log
#
# if the photo was taken on 2011-04-23 the file will be
# copied to <dir to copy to>/2011-04-23/<file name>
#
# The format of our panasonic camera is:
# image['Exif.Photo.DateTimeOriginal']=2011-04-23 19:45:39
# The date/time value is a datetime object
#
# Update: 2016-04-30
# the pyexiv2 library seems to have changed with 0.3.2. There is no longer
# an Image method. Instead there is an ImageMetadata method
#
# Aaron Nielsen
# Original: 12 January 2012
#
# Updated for test

import pyexiv2
import datetime

import os,sys

def copyPhotoTo(infile,outdirBase):
    try:
        #image=pyexiv2.Image(infile)
        image = pyexiv2.ImageMetadata(infile)
        image.read()
    except IOError:
        print 'ERROR: ' + infile + ' could not be read'
        return None

    # no longer returns a datetime object
    #dto=image['Exif.Photo.DateTimeOriginal']
    #photoDate=dto.date().isoformat()

    try:
        #In [24]:  str(image['Exif.Photo.DateTimeOriginal'])
        #Out[24]:  '<Exif.Photo.DateTimeOriginal [Ascii] = 2016:03:27 15:30:19>'
        dateTimeStr = str(image['Exif.Photo.DateTimeOriginal']).split('=')[-1][1:-1]
        photoDate = dateTimeStr.split()[0].replace(':','-')
    except KeyError:
        # this occurs if the key Exif.Photo.DateTimeOriginal is not set in the file
        # in this case, we will try to parse the filename instead
        # IMG_20151220_174219.jpg is the example I have
        photoDateFromName = os.path.basename(infile).split('_')[1]
        photoDate = photoDateFromName[0:4] + '-' +\
                    photoDateFromName[4:6] + '-' +\
                    photoDateFromName[6:]

    # photoDate needs to have the format YYYY-MM-DD
    outdir=os.sep.join([outdirBase,photoDate])

    # make the output directory if it does not exist
    if not os.access(outdir,os.W_OK):
        os.makedirs(outdir)

    # create the destination filename
    infileBase=infile.split(os.sep)[-1]
    destinFile=os.sep.join([outdir,infileBase])

    # check if the destination file already exists
    if os.access(destinFile,os.F_OK):
        print destinFile + ' exists not copying.'
        return None

    # generate the os command to copy the file
    oscmd='cp \"%s\" \"%s\"' %( infile, destinFile )
    print oscmd
    os.system(oscmd)

    return None

if __name__=="__main__":

    infiles=sys.argv[2:]
    outdir=sys.argv[1]

    count = 0
    total = len(infiles)

    for infile in infiles:
        count += 1
        print " %d/%d %s to %s" %(count,total,infile,outdir)
        copyPhotoTo(infile,outdir)

    
