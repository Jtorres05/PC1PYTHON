# 1.Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# 2.Obtener la extensión del archivo (parte después del último punto) y convertirla a minúsculas
extension = nombre_archivo.lower().split('.')[-1]

# 3.Determinar el tipo MIME correspondiente
if extension == 'gif':
    tipo_mime = 'image/gif'
elif extension == 'jpg' or extension == 'jpeg':
    tipo_mime = 'image/jpeg'
elif extension == 'png':
    tipo_mime = 'image/png'
elif extension == 'pdf':
    tipo_mime = 'application/pdf'
elif extension == 'txt':
    tipo_mime = 'text/plain'
elif extension == 'zip':
    tipo_mime = 'application/zip'
else:
    tipo_mime = 'application/octet-stream'

print("Tipo MIME:", tipo_mime)