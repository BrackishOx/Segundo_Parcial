import re
from mesa import Model
from mesa.time import BaseScheduler
from mesa.datacollection import DataCollector
from agentes import SumaAgente, RestaAgente, MultiplicacionAgente, DivisionAgente, PotenciaAgente

class CalculadoraModel(Model):
    def __init__(self):
        self.schedule = BaseScheduler(self)
        self.suma_agente = SumaAgente(1, self)
        self.resta_agente = RestaAgente(2, self)
        self.mult_agente = MultiplicacionAgente(3, self)
        self.division_agente = DivisionAgente(4, self)
        self.potencia_agente = PotenciaAgente(5, self)
        self.schedule.add(self.suma_agente)
        self.schedule.add(self.resta_agente)
        self.schedule.add(self.mult_agente)
        self.schedule.add(self.division_agente)
        self.schedule.add(self.potencia_agente)
        self.datacollector = DataCollector(agent_reporters={"Resultado": "resultado"})

    def step(self):
        self.schedule.step()

    def resolver_expresion(self, expresion):
        expresion = expresion.replace('^', '**')
        tokens = self.tokenizar_expresion(expresion)
        resultado = self.evaluar_tokens(tokens)
        return resultado

    def tokenizar_expresion(self, expresion):
        return re.findall(r'\d+|\*\*|[+*/()-]', expresion)

    def evaluar_tokens(self, tokens):
        salida = []
        operadores = []
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

        def aplicar_operacion(operador, a, b):
            if operador == '+':
                return self.suma_agente.calcular(a, b)
            elif operador == '-':
                return self.resta_agente.calcular(a, b)
            elif operador == '*':
                return self.mult_agente.calcular(a, b)
            elif operador == '/':
                return self.division_agente.calcular(a, b)
            elif operador == '**':
                return self.potencia_agente.calcular(a, b)

        for token in tokens:
            if token.isdigit():
                salida.append(int(token))
            elif token in precedencia:
                while (operadores and operadores[-1] != '(' and precedencia[operadores[-1]] > precedencia[token]):
                    op = operadores.pop()
                    b = salida.pop()
                    a = salida.pop()
                    resultado = aplicar_operacion(op, a, b)
                    salida.append(resultado)
                operadores.append(token)
            elif token == '(':
                operadores.append(token)
            elif token == ')':
                while operadores[-1] != '(':
                    op = operadores.pop()
                    b = salida.pop()
                    a = salida.pop()
                    resultado = aplicar_operacion(op, a, b)
                    salida.append(resultado)
                operadores.pop()

        while operadores:
            op = operadores.pop()
            b = salida.pop()
            a = salida.pop()
            resultado = aplicar_operacion(op, a, b)
            salida.append(resultado)

        return salida[0] if salida else None

if __name__ == "__main__":
    modelo = CalculadoraModel()
    
    while True:
        expresion = input("Ingresa una expresión matemática (o 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            print("Saliendo de la calculadora.")
            break
        resultado = modelo.resolver_expresion(expresion)
        print(f"Resultado de la expresión '{expresion}' es: {resultado}")
