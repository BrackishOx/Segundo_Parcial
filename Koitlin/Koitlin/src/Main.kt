import java.lang.Math.pow
import java.lang.Math.toRadians
import kotlin.math.*
import java.util.Scanner

open class Calculadora {
    fun suma(a: Double, b: Double): Double = a + b
    fun resta(a: Double, b: Double): Double = a - b
    fun multiplicacion(a: Double, b: Double): Double = a * b
    fun division(a: Double, b: Double): Double {
        if (b == 0.0) throw IllegalArgumentException("No se puede dividir entre cero")
        return a / b
    }
}

class CalculadoraCientifica : Calculadora() {
    private var memoria: Double = 0.0

    fun seno(x: Double): Double = sin(x)
    fun coseno(x: Double): Double = cos(x)
    fun tangente(x: Double): Double = tan(x)

    fun potencia(base: Double, exponente: Double): Double = pow(base, exponente)

    fun raiz(x: Double): Double {
        if (x < 0) throw IllegalArgumentException("No se puede calcular la raíz de un número negativo")
        return sqrt(x)
    }

    fun logaritmo(x: Double): Double {
        if (x <= 0) throw IllegalArgumentException("El logaritmo no está definido para valores <= 0")
        return log10(x)
    }

    fun guardarEnMemoria(valor: Double) { memoria = valor }
    fun recuperarDeMemoria(): Double = memoria
    fun limpiarMemoria() { memoria = 0.0 }
}

fun main() {
    val calc = CalculadoraCientifica()
    val scanner = Scanner(System.`in`)

    println("Introduce la operación que deseas realizar (ejemplo: 'suma 3 4', 'raíz 16', 'logaritmo 100'):")

    val input = scanner.nextLine()
    val parts = input.split(" ")

    val operation = parts[0].lowercase()
    try {
        when (operation) {
            "suma" -> {
                val a = parts[1].toDouble()
                val b = parts[2].toDouble()
                println("Resultado: ${calc.suma(a, b)}")
            }
            "resta" -> {
                val a = parts[1].toDouble()
                val b = parts[2].toDouble()
                println("Resultado: ${calc.resta(a, b)}")
            }
            "multiplicacion" -> {
                val a = parts[1].toDouble()
                val b = parts[2].toDouble()
                println("Resultado: ${calc.multiplicacion(a, b)}")
            }
            "division" -> {
                val a = parts[1].toDouble()
                val b = parts[2].toDouble()
                println("Resultado: ${calc.division(a, b)}")
            }
            "seno" -> {
                val x = parts[1].toDouble()
                println("Resultado: ${calc.seno(toRadians(x))}")
            }
            "coseno" -> {
                val x = parts[1].toDouble()
                println("Resultado: ${calc.coseno(toRadians(x))}")
            }
            "tangente" -> {
                val x = parts[1].toDouble()
                println("Resultado: ${calc.tangente(toRadians(x))}")
            }
            "potencia" -> {
                val base = parts[1].toDouble()
                val exponente = parts[2].toDouble()
                println("Resultado: ${calc.potencia(base, exponente)}")
            }
            "raiz" -> {
                val x = parts[1].toDouble()
                println("Resultado: ${calc.raiz(x)}")
            }
            "logaritmo" -> {
                val x = parts[1].toDouble()
                println("Resultado: ${calc.logaritmo(x)}")
            }
            else -> {
                println("Operación no válida.")
            }
        }
    } catch (e: Exception) {
        println("Error: ${e.message}")
    } finally {
        scanner.close()
    }
}
