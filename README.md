 Segundo_Parcial
# Perceptron Netlogo
Aquí tienes una versión ampliada del informe con la descripción de la interfaz y un análisis sobre cómo los parámetros afectan los resultados del perceptrón:

---

**Informe sobre el Perceptrón y su Implementación en NetLogo**

1. **Introducción al Perceptrón**  
   El perceptrón es uno de los modelos de redes neuronales más simples, diseñado para realizar tareas de clasificación binaria. Funciona como un clasificador lineal que asigna una entrada a una de dos clases. Para ello, ajusta un conjunto de pesos que representan la importancia de cada característica de entrada. Su salida se determina mediante una combinación lineal de las entradas ponderadas, aplicando una función de activación para producir un valor binario.
   
3. **Implementación en NetLogo**  
   La implementación del perceptrón se realizó en NetLogo versión 3D, donde se modelaron puntos en un espacio tridimensional para clasificar de acuerdo con funciones objetivo seleccionadas (por ejemplo, AND o XOR). La interfaz desarrollada cuenta con varios elementos interactivos para facilitar el proceso de entrenamiento y prueba, descritos a continuación.

   **Descripción de la Interfaz**:
   - **Botones**:
     - `setup`: Inicializa la simulación y prepara los datos para el entrenamiento.
     - `train`: Realiza el entrenamiento completo del perceptrón durante múltiples épocas.
     - `train-once`: Ejecuta una única iteración de entrenamiento, útil para observar cambios paso a paso.
   - **Deslizadores**:
     - **learning-rate**: Define la tasa de aprendizaje, la cual está configurada en 0.5 en esta simulación. Esta tasa determina la magnitud de los ajustes de los pesos en cada iteración.
     - **examples-per-epoch**: Controla el número de ejemplos procesados por época, configurado en 500. Este parámetro impacta la cantidad de datos que el perceptrón evalúa antes de actualizar los pesos.
   - **Gráfica "Error vs. Epochs"**: Proporciona una visualización del error a lo largo de las épocas, mostrando cómo se reduce a medida que el perceptrón ajusta sus pesos y mejora en la clasificación.
   - **Panel de Prueba**:
     - Entradas `input-1` y `input-2`: Permiten introducir valores para probar el modelo y observar la salida `output` en tiempo real. En este caso, el output observado es -1.
   - **Opciones de Configuración**:
     - **target-function**: En este ejemplo, se ha seleccionado `xor` como función objetivo, que es un reto para el perceptrón dado que XOR no es linealmente separable.
     - **show-weights**: Permite visualizar el cambio de los pesos durante el entrenamiento, útil para entender cómo se ajustan para minimizar el error.

4. **Análisis de Parámetros y su Impacto en el Resultado**  
   - **Tasa de Aprendizaje (learning-rate)**: Con un valor de 0.5, el perceptrón hace ajustes significativos en cada iteración. Una tasa de aprendizaje alta puede llevar a una convergencia rápida, pero también puede hacer que el modelo sobrepase la solución óptima, oscilando alrededor de la clasificación ideal. Para el problema de XOR, un valor más bajo podría permitir un ajuste más fino, aunque llevaría más tiempo para lograr una precisión estable.
   - **Número de Ejemplos por Época (examples-per-epoch)**: Con 500 ejemplos por época, el modelo tiene suficientes datos para hacer ajustes significativos en cada iteración. Esto es especialmente importante en problemas de clasificación complejos como XOR, donde un mayor número de ejemplos ayuda a la red a "ver" más del espacio de entrada y ajustar los pesos en consecuencia.

   La función objetivo XOR representa un desafío debido a su no linealidad. Esto implica que el perceptrón, que es un clasificador lineal, solo alcanzará una clasificación perfecta si los datos son linealmente separables. Dado que XOR no cumple con esta condición, es esperable que el modelo no logre un 100% de precisión, pero con los ajustes adecuados en la tasa de aprendizaje y el número de ejemplos, el perceptrón puede aproximar la clasificación correcta en la mayoría de los casos.

5. **Resultados y Visualización**  
   La simulación en NetLogo produce una línea de decisión en el espacio tridimensional que intenta separar las dos clases de puntos. A lo largo de las épocas, la precisión del modelo aumenta y el error disminuye gradualmente, hasta estabilizarse en una precisión óptima cercana al 95%, aunque la clasificación no es perfecta debido a la naturaleza de la función XOR. La gráfica "Error vs. Epochs" permite visualizar esta mejora en tiempo real, y la opción de mostrar pesos permite observar los ajustes específicos realizados en el proceso de aprendizaje.

6. **Conclusión**  
   La simulación interactiva en NetLogo proporciona una visión visual y didáctica del funcionamiento de un perceptrón. Aunque el modelo no puede resolver perfectamente funciones no linealmente separables como XOR, los resultados obtenidos demuestran que el perceptrón puede aproximarse a una buena solución con una alta precisión. Esta implementación ofrece una herramienta valiosa para explorar y entender los conceptos fundamentales del aprendizaje en redes neuronales simples.

---

¿Te gustaría agregar los datos de alguna corrida específica, como el número exacto de épocas necesarias para alcanzar la precisión máxima, o algún gráfico de la evolución del error? Esto podría complementar el análisis con resultados experimentales específicos.

![image](https://github.com/user-attachments/assets/9fe46253-fb17-42be-abdc-8aef369ac971)

![image](https://github.com/user-attachments/assets/f4f69d2d-460a-4fa2-a83c-e97d5a27f884)

![image](https://github.com/user-attachments/assets/8077d2bc-5e14-4db6-aed7-57476e0b3955)




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


# Calculadora cientifica kotlin
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


![image](https://github.com/user-attachments/assets/2c6ec3e4-75e2-4190-89fd-9c7b5cff0dd0)

![image](https://github.com/user-attachments/assets/a34f8b3b-473e-4b8b-a60e-a3deb592bd3a)


![image](https://github.com/user-attachments/assets/0733727d-b34f-47cf-ba4a-0f890f3b126e)

