from mesa import Agent

class OperacionAgente(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    
    def calcular(self, *args):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class SumaAgente(OperacionAgente):
    def calcular(self, a, b):
        return a + b

class RestaAgente(OperacionAgente):
    def calcular(self, a, b):
        return a - b

class MultiplicacionAgente(OperacionAgente):
    def calcular(self, a, b):
        return a * b

class DivisionAgente(OperacionAgente):
    def calcular(self, a, b):
        if b == 0:
            return float('inf')  # Devolver infinito para divisiones por cero
        return a / b

class PotenciaAgente(OperacionAgente):
    def calcular(self, base, exponente):
        return base ** exponente
