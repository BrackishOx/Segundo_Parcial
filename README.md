 Segundo_Parcial
# Perceptron Netlogo

**El Perceptrón y su Implementación en NetLogo**

1. **Introducción al Perceptrón**  
   El perceptrón es una de las redes neuronales más sencillas, creada para resolver problemas de clasificación binaria (es decir, separar datos en dos grupos). Funciona como un clasificador que decide si una entrada pertenece a una clase o a otra, ajustando ciertos valores llamados “pesos” para darle más o menos importancia a cada característica de la entrada. La salida del perceptrón se calcula tomando una combinación de estas entradas ponderadas y pasándolas por una función que produce un valor binario (1 o -1, por ejemplo).

2. **Implementación en NetLogo**  
   En esta implementación, utilizamos NetLogo en su versión 3D para modelar puntos en un espacio tridimensional. La interfaz nos permite controlar el entrenamiento y probar el modelo de forma interactiva.

   **Descripción de la Interfaz**:
   - **Botones**:
     - `setup`: Inicializa la simulación y prepara los datos para comenzar el entrenamiento.
     - `train`: Realiza el entrenamiento completo, pasando varias veces por los datos.
     - `train-once`: Ejecuta una única iteración de entrenamiento, permitiendo ver los ajustes paso a paso.
   - **Deslizadores**:
     - **learning-rate**: Define cuánto se ajustan los pesos en cada paso. En este caso, está configurado en 0.5, lo cual permite cambios significativos en cada iteración.
     - **examples-per-epoch**: Controla cuántos ejemplos se procesan en cada ciclo de entrenamiento, configurado en 500, lo que permite usar muchos datos y hacer el aprendizaje más robusto.
   - **Gráfica "Error vs. Epochs"**: Muestra cómo el error disminuye a lo largo de las épocas, dando una visualización del aprendizaje del modelo.
   - **Panel de Prueba**:
     - Entradas `input-1` y `input-2`: Permiten probar el perceptrón con diferentes valores de entrada y ver la clasificación que produce (`output`).
   - **Opciones de Configuración**:
     - **target-function**: Aquí seleccionamos `xor` como la función objetivo, un caso complicado porque XOR no es linealmente separable (no se puede dividir con una simple línea o plano).
     - **show-weights**: Permite ver cómo cambian los pesos durante el entrenamiento, para entender mejor cómo el perceptrón se ajusta a los datos.

3. **Análisis de Parámetros y su Impacto en el Resultado**  
   - **Tasa de Aprendizaje (learning-rate)**: Con un valor de 0.5, el perceptrón hace ajustes grandes en cada iteración. Esto acelera el proceso, pero puede hacer que el modelo se “pase” de la solución óptima. Una tasa de aprendizaje más baja podría hacer el ajuste más preciso, aunque llevaría más tiempo para lograr buenos resultados.
   - **Número de Ejemplos por Época (examples-per-epoch)**: Con 500 ejemplos por época, el perceptrón tiene suficientes datos para aprender mejor en cada ciclo. Esto es particularmente útil en problemas difíciles como XOR, donde necesita “ver” muchos ejemplos para ajustarse adecuadamente.

   Elegir XOR como objetivo añade un desafío, ya que el perceptrón no puede resolver perfectamente problemas que no son linealmente separables. Sin embargo, puede aproximarse a una solución bastante buena ajustando sus pesos y sesgo.

4. **Resultados y Visualización**  
   En la simulación de NetLogo, el perceptrón trata de trazar una línea de decisión en el espacio tridimensional para separar las dos clases de puntos. A medida que entrena, la precisión del modelo aumenta y el error disminuye, estabilizándose cerca de un 95% de precisión. Aunque el perceptrón no logra clasificar perfectamente todas las entradas de XOR, se aproxima bastante. La gráfica “Error vs. Epochs” permite visualizar esta mejora, y ver cómo los pesos cambian durante el aprendizaje también ayuda a entender su proceso de ajuste.

5. **Conclusión**  
   La simulación en NetLogo proporciona una manera interactiva y visual de entender cómo funciona un perceptrón. Aunque este modelo es simple y tiene sus limitaciones (como la imposibilidad de resolver XOR perfectamente), la simulación muestra cómo puede aprender a clasificar datos con un alto grado de precisión en muchos casos. Esta implementación es una herramienta educativa valiosa para explorar y comprender los fundamentos del aprendizaje en redes neuronales.



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

