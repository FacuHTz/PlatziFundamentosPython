import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXY"
num = "0123456789"
simbolos = "!#$%&'()*+,-./[]"
base = minus + mayus + num + simbolos
longitud = 12
for _ in range(10):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    password_encriptado = generate_password_hash(password)
    print(f"{password} => {password_encriptado}")
