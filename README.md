# Segundo_Parcial

#Calculadora-Cientifica
Informe sobre la Aplicación de los Principios de Programación Orientada a Objetos en la Implementación de una Calculadora Científica en Kotlin
Introducción
La Programación Orientada a Objetos (POO) es un paradigma de programación que utiliza "objetos" para modelar datos y comportamientos. En este informe, se detallan los principios de POO que se aplicaron en el desarrollo de una calculadora científica en Kotlin, incluyendo encapsulamiento, herencia y polimorfismo.

1. Encapsulamiento
El encapsulamiento es el principio de ocultar los detalles internos de una clase y proporcionar una interfaz clara para interactuar con esos datos. Este principio se aplica en la calculadora de la siguiente manera:

Clases y Métodos Privados: En la clase base Calculadora, se definen métodos y atributos como privados o protegidos para evitar que otros objetos accedan y modifiquen el estado interno de la calculadora directamente. Por ejemplo, las operaciones de suma, resta, multiplicación y división están encapsuladas dentro de métodos que manejan la lógica sin exponer detalles innecesarios.

Métodos Públicos: Se proporcionan métodos públicos para realizar operaciones matemáticas, lo que permite a los usuarios de la clase interactuar con la calculadora sin necesidad de conocer su implementación interna. Esto asegura que la lógica de la calculadora se mantenga intacta y se pueda cambiar sin afectar el uso externo.

kotlin
Copiar código
open class Calculadora {
    fun sumar(a: Double, b: Double): Double {
        return a + b
    }

    // Otros métodos de operaciones...
}
2. Herencia
La herencia permite que una clase derive de otra, reutilizando su código y extendiendo su funcionalidad. En la calculadora, se aplica de la siguiente manera:

Clase Derivada: La clase CalculadoraCientifica hereda de la clase Calculadora, lo que le permite acceder a todos los métodos y propiedades de la clase base. Esto elimina la necesidad de duplicar código para las operaciones básicas y permite extender la funcionalidad con nuevas operaciones científicas.

Extensión de Funcionalidad: CalculadoraCientifica añade métodos adicionales, como funciones trigonométricas (seno, coseno) y logaritmos, que no están presentes en la clase base. Esto ilustra cómo la herencia puede ser utilizada para crear una jerarquía de clases que comparten comportamientos comunes y extienden la funcionalidad.

kotlin
Copiar código
class CalculadoraCientifica : Calculadora() {
    fun seno(x: Double): Double {
        return Math.sin(x)
    }

    // Otras funciones científicas...
}
3. Polimorfismo
El polimorfismo permite que una clase tenga múltiples formas, lo que se traduce en la capacidad de usar una interfaz común para diferentes tipos de datos. En la implementación de la calculadora, se aplica de la siguiente manera:

Sobrecarga de Métodos: La clase Calculadora puede tener métodos sobrecargados para realizar operaciones que acepten diferentes tipos de argumentos. Por ejemplo, se pueden definir métodos sumar que acepten tanto enteros como dobles, permitiendo que la misma operación se ejecute de manera adecuada según el tipo de dato.

Uso de Interfaces: Aunque en este caso no se implementa, el uso de interfaces podría permitir que diferentes clases implementen métodos de cálculo de manera diferente, proporcionando una forma de polimorfismo. Por ejemplo, se podría crear una interfaz Operaciones que defina métodos como ejecutar(), y distintas clases podrían implementar esta interfaz para realizar diferentes tipos de operaciones.

kotlin
Copiar código
fun sumar(a: Int, b: Int): Int {
    return a + b
}

fun sumar(a: Double, b: Double): Double {
    return a + b
}
Conclusiones
En conclusión, la implementación de la calculadora científica en Kotlin demuestra claramente cómo se aplican los principios de la Programación Orientada a Objetos. A través del encapsulamiento, se protege el estado interno de los objetos; la herencia permite la reutilización de código y la extensión de la funcionalidad; y el polimorfismo ofrece flexibilidad y reutilización de métodos en diferentes contextos. Estos principios no solo facilitan el desarrollo y mantenimiento del código, sino que también promueven un diseño más limpio y modular.

