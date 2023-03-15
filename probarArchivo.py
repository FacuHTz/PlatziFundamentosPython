import os
cwd = os.getcwd() # Obtener el directorio actual de trabajo (cwd)
files = os.listdir(cwd) # Obtener todos los archivos en ese directorio
print("Archivos en %r: %s" % (cwd, files))