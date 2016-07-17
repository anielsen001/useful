#!/usr/bin/env python
"""
Syntax:
moveMusic.py <search dir to replace> <dir with replacements>

Find *.m4a music on thumb drive remove and replace with *mp3
from another source


"""

import os,sys,glob,fnmatch,shutil

def find(pattern,path):
    """
    see http://stackoverflow.com/questions/1724693/find-a-file-in-python
    """
    result=[]
    for root,dirs,files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name,pattern):
                result.append(os.path.join(root,name))
    return result

def main():
    # get the inputs
    m4aDir = sys.argv[1]
    mp3Dir = sys.argv[2]

    print 'm4aDir = %s'%m4aDir
    print 'mp3Dir = %s'%mp3Dir

    # get a list of all the m4a music in the search dir
    m4aList = find('*m4a',m4aDir)

    count = 0 
    totalTodo = len(m4aList)
    
    for m4a in m4aList:

        # get the m4a directory
        m4afulldir = os.path.dirname(m4a)

        # generate the mp3 file name
        mp3name = os.path.splitext(os.path.basename(m4a))[0]+'.mp3'      
        print 'Replacing %s'%m4a
        print '     with %s'%mp3name

        # find the mp3
        try:
            mp3full = find(mp3name,mp3Dir)[0]
            print '    found %s'%mp3full
        except IndexError:
            # this is the case where we did not find a matching mp3 file
            print '  missing %s'%mp3name
            continue

        # generate the os commands to call
        mp3new = os.sep.join([m4afulldir,mp3name])
        print 'Copying %s -> %s'%(mp3full,mp3new)
        shutil.copyfile(mp3full,mp3new)

        # removing m4a file
        print 'Removing %s'%m4a
        os.remove(m4a)

        count+=1
        #if (count >100): break
        print '*** Done %d/%d'%(count,totalTodo)

if __name__=="__main__":
    main()
