usuarios = []
cuentas = []

usuario = {"nombre":"Angel","estado": "A"}
usuarios.append(usuario)


cuenta = {"nombre":"Angel","valor":400.00}
cuentas.append(cuenta)

def depositar():
   nombre = input("Introduce el nombre del usuario: ")
   monto = float(input("introduce el monto a depositar: "))
   for cuenta_guardada in cuentas:
      if(cuenta_guardada["nombre"] == nombre):
        cuenta_guardada["valor"] += monto

print(cuentas)
depositar()
print(cuentas)