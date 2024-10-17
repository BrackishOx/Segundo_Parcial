# Segundo_Parcial

# Calculadora_cientifica
1.Encapsulamiento
El encapsulamiento es sobre mantener los detalles internos de una clase ocultos y permitir que se acceda a ellos de manera controlada. En la calculadora:
 Metodos Privados:Cree una clase llamada Calculadora, donde guardé las operaciones básicas (suma, resta, etc.) como métodos privados. Esto significa que no se pueden modificar directamente desde fuera de la clase.

Metodos Publicos: Los métodos que permiten hacer las operaciones son públicos, así que cualquiera puede usarlos sin tener que entender cómo funcionan por dentro.
Esto asegura que la lógica de la calculadora permanezca segura y se pueda cambiar sin afectar a los usuarios.

```open class Calculadora {
    fun sumar(a: Double, b: Double): Double {
        return a + b
    }

```
2.Herencia
La herencia permite crear una nueva clase que comparte propiedades y métodos de otra clase. En mi calculadora, esto se ve así:

La clase Calculadora Cientifica hereda de Calculadora, así que puede usar todas las operaciones básicas sin tener que reescribir el código.

 Calculadora Cientifica agrega nuevas funciones, como las trigonométricas (seno, coseno), lo que muestra cómo la herencia ayuda a crear clases más específicas a partir de clases más generales.
 
```
class CalculadoraCientifica : Calculadora() {
    fun seno(x: Double): Double {
        return Math.sin(x)
    }

    // Otras funciones científicas...
}
```
