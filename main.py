from setuptools.command.alias import alias

from cosas import Alumno, Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("---to String----")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)
    print("---PERRO---")
    perro1 = Perro("Pooddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" #set en notacion Pythonic
    print(vars(perro1))
    print(perro1)
    perro1.edad = 12
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)
main()