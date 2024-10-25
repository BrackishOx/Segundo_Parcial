from model import CalculadoraModel
    
def main():
    
    model = CalculadoraModel()

    expresion = input("Ingresa una expresión matemática: ")
    
    resultado = model.resolver_expresion(expresion)

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()

