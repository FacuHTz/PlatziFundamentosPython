# Esta funcion lee los archivos de la carpeta raíz donde esta abierto vscode, si hay una subcarpeta hay que especificarla

file=open('./ManejoArchivos/data1.txt', 'r')
# print(file)
lineas = file.readlines()
print(lineas)
file.close()

# Esta funcion lee los archivos de la carpeta raíz donde esta abierto vscode, si hay una subcarpeta hay que especificarla

# with open('./ManejoArchivos/data1.txt', 'r') as file_object:
#     contents = file_object.read()
#     print(contents.strip())

