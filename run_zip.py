
import os
import zipfile

zf = zipfile.ZipFile("authorizer.zip", "w")
os.chdir('src')
for dirname, subdirs, files in os.walk("."):
    #print(dirname)
    if dirname != '.' and not dirname.startswith('./requests'):  continue
    zf.write(dirname)
    for filename in files:
        if filename.endswith('.pyc'):    continue
        zf.write(os.path.join(dirname, filename))
zf.close()
