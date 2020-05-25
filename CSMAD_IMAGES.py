import os
import scipy.misc
import numpy as np
import bob.io.base                     # need to install BOB by IDIAP (https://www.idiap.ch/software/bob/)
import re
text_file = open("/media/shravan/Windows/CSMAD/protocols/pad/bonafide.lst", "r") # location of the bonafide/attack folders containing the HDF5 files
lines = text_file.readlines()
string = 'h5'
lines = [y for y in lines if string in y]
for i in range(len(lines)):
    f = bob.io.base.HDF5File(('/media/shravan/Windows/CSMAD/'+lines[i]).rstrip(), 'r')    #edit the location appropriately
    keys = f.keys(f)
    subs = '/color/'
    col = [x for x in keys if subs in x]
    vid_name = re.sub("A/|B/|C/|D/|E/|F/|G/|H/|I/|J/|K/|L/|M/|N/","",lines[i])
    vid_name = re.sub(".h5"," ",vid_name)
    vid_name = ('CSMAD/'+vid_name)
    os.mkdir(vid_name.rstrip())
    
    for j in range(len(col)):
        img_name = col[j].lstrip('data/sr300/color/')       #extracts only the RGB images/frames
        array = f.read(col[j])
        scipy.misc.imsave((((vid_name).rstrip()+'/'+img_name).rstrip()+'.jpg').rstrip(), array)
