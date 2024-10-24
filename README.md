# Segundo_Parcial
# Perceptron Netlogo


# Calculadora basada en paradigmas de agentes
Interaccion de Agentes

Los agentes no se comunican entre sí de manera directa en cambio la interacción se gestiona a través de un modelo central este modelo es responsable de recibir la expresión matemática dividirla en partes y delegar las operaciones a los agentes correspondientes.

Por ejemplo, cuando se ingresa una expresión como "2 + 3 * 5", el modelo sigue los siguientes pasos:

Primero, se divide la expresión en sus componentes (números y operadores): ['2', '+', '3', '*', '5'].

Luego, el modelo distribuye las operaciones:
- El agente encargado de la suma se ocupará de procesar la operación '+', utilizando los números asignados.
- El agente de multiplicación realizará la operación '*', también con los números que le corresponden.

Cada agente trabaja de forma independiente. Resuelven su parte de la operación y envían los resultados al modelo central, que se encarga de combinarlos para obtener el resultado final. En el ejemplo "2 + 3 * 5", primero se ejecuta la multiplicación, lo que da como resultado 15. Posteriormente, se realiza la suma, obteniendo 17 como resultado final.

El **Modelo (CalculadoraModel)** actúa como el núcleo del sistema. Recibe la expresión, la desglosa en operaciones más simples, y asigna dichas operaciones a los agentes correspondientes. Finalmente, une los resultados parciales para obtener el cálculo completo.

Los **Agentes** son los responsables de ejecutar operaciones específicas. Cada uno de ellos se especializa en una operación matemática en particular, como suma, resta, multiplicación o división.


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
La herencia permite crear una nueva clase que comparte propiedades y métodos de otra clase En mi calculadora esto se ve así:

La clase Calculadora Cientifica hereda de Calculadora así que puede usar todas las operaciones básicas sin tener que reescribir el código.

 Calculadora Cientifica agrega nuevas funciones, como las trigonométricas (seno, coseno), lo que muestra cómo la herencia ayuda a crear clases más específicas a partir de clases más generales.
 
```
class CalculadoraCientifica : Calculadora() {
    fun seno(x: Double): Double {
        return Math.sin(x)
    }

   
}
```
3.Poliformismo
El polimorfismo permite que una clase tenga diferentes formas, lo que se traduce en la capacidad de usar el mismo nombre de método para hacer cosas diferentes. En la calculadora, esto se aplica así:

 La clase Calculadora puede tener varios métodos sumar que acepten distintos tipos de datos (como enteros y dobles), lo que significa que el mismo método puede funcionar para diferentes tipos.

 Aunque no lo implemente en este caso, se podría crear una interfaz que defina métodos como ejecutar(), y diferentes clases podrían implementar esto para realizar diferentes cálculos.
```
fun sumar(a: Int, b: Int): Int {
    return a + b
}

fun sumar(a: Double, b: Double): Double {
    return a + b
}
```
 
al hacer la calculadora científica en Kotlin El encapsulamiento ayuda a proteger los datos, la herencia permite reutilizar el código y agregar nuevas funciones,
y el polimorfismo facilita el uso de métodos con el mismo nombre para diferentes tipos. Estos principios hacen que el código sea más fácil de mantener y entender.
