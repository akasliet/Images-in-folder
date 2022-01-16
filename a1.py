get_ipython().magic('reset -sf')
import os
import numpy as np

# Getting the current work directory (cwd)
thisdir = os.getcwd()
# r=root, d=directories, f = files
i=0
for r, d, f in os.walk(thisdir):
    
    for file in f:  
        i=i+1
        if file.endswith(".JPG"):
            
            print(os.path.join(r, file),"\n")
print(i)
            

