# Segundo_Parcial

# Calculadora basada en paradigmas de agentes
¿Cómo se comunican los agentes?
Respuesta corta: No se comunican directamente entre ellos. La comunicación entre los agentes y el sistema ocurre a través de un modelo central, que es el encargado de gestionar la expresión matemática y delegar las operaciones a cada agente correspondiente.

Cuando el usuario ingresa una expresión, por ejemplo, 2 + 3 * 5, el modelo lo procesa de la siguiente manera:

 El modelo divide la expresión en partes (números y operadores), en este caso: ['2', '+', '3', '*', '5'].
Distribución de operaciones:
Para el +, el agente suma se encarga de procesar la suma de los números que le asignan.
Para el *, el agente multiplicación procesa la multiplicación de los números asignados.
Resultados: Los agentes no hablan entre sí, sino que cada uno recibe una parte de la operación, la resuelve y le devuelve el resultado al modelo, que junta todos los resultados para obtener el valor final.
Por ejemplo, en la expresión 2 + 3 * 5, primero se resuelve 3 * 5 (usando el agente multiplicación), que devuelve 15, y luego se suma 2 + 15 (usando el agente suma), resultando en 17.

Modelo (CalculadoraModel): Es el cerebro de la calculadora. Recibe la expresión matemática, la descompone en operaciones más pequeñas, y asigna esas operaciones a los agentes. Luego, reúne los resultados parciales y calcula el resultado final.

Agentes: Son los encargados de hacer cálculos específicos. Cada agente es responsable de una sola operación:


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

    // Otras funciones científicas...
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
