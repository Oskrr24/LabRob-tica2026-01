# Laboratorio 1 Robótica y Sist. Autónomos
ICI4150-2

- Integrantes:
    - Oscar Ruiz
    - Milovan Fuentes
    - Marcos Cádiz
    - Andrés García
    - Amaro Fibla

# Descripción del laboratorio

El objetivo de este laboratorio fue comprender el comportamiento cinemático de un robot móvil diferencial (para este caso e-puck) mediante simulación en Webots. Se controló el movimiento a través de las velocidades de los motores de las ruedas izquierda (Vl) y derecha (Vr) usando un controlador programado en Python.

Durante este laboratorio se analizarán preguntas de análisis y el robot se verá afectado a distintas pruebas propuestas por el mismo laboratorio, en donde analizaremos el movimiento y describiremos su trayectoria.

# Como ejecutar la simulación en Webots

Para ejecutar esta simulación, es necesario tener instalado Python en el dispositivo.

1. Abrir Webots
2. Cargar robot e-puck
    1. File → Open Sample World → robots → gctronic → e-puck → e-puck.wbt
3. En la carpeta donde se tienen los controladores del e-puck, crear una carpeta con el nombre “e-puckPY” y dentro cargar el archivo [e-puckPY.py](http://e-puckPY.py) que tiene el controlador.
    1. Esta carpeta por lo general se encuentra en la dirección *C:\Program Files\Webots\projects\robots\gctronic\e-puck\controllers*
4. Una vez cargado el archivo, en Webots en el Scene Tree, se buscará el nodo ‘controller “e-puck”’ en el apartado E-puck “e-puck”.
5. Se selecciona la opción y se selecciona “Select…” y buscamos el nombre de nuestra carpeta seguido de OK.
6. Seleccionamos Edit para visualizar el código y corremos la simulación para ver el movimiento recto (por defecto).
    1. Para cambiar a Trayectoria Curva o Rotación en el lugar, comentar las velocidades “1” y descomentar “2” o “3” seguido de recargar el mundo con la opción en la barra superior.
    2. Comentar y descomentar código a gusto para probar cosas.
7. Guardad si se modifica el archivo o si se desea continuar más tarde.

# Resultados obtenidos: Tareas

A continuación, se describen los comportamientos observados según la configuración de los actuadores.

### Movimiento recto: Vl = Vr

Durante este experimento, en donde ambas velocidades de ambas ruedas eran iguales, el robot e-puck avanzó en línea recta con velocidad constante, ver video “Recto” para su comprobación.

### Trayectoria Curva: Vl ≠ Vr

Para este segundo experimento, la rueda izquierda figuraba una velocidad mayor que la derecha, con valores Vl = 4.0 y Vr = 2.0. El resultado fue que el robot describe un arco hacia el lado de la rueda derecha (la más lenta), ver video “Curva” para su comprobación.

### Rotación

Para este tercer y último experimento,  la rueda izquierda figura con una velocidad positiva de 2.0 mientras que la rueda derecha con velocidad de -2.0, aquí podemos observar que el robot gira sobre su propio eje central sin desplazarse. Ver video “Rotacion” para su comprobación.

## Extensión

Para la extensión, se pide comparar la trayectoria ideal (una línea recta en este caso) con una trayectoria con variaciones (para este ejemplo, una serie de curvas).

1. Trayectoria Ideal (Línea Recta)
    
    La trayectoria ideal se logra cuando ambas ruedas tienen la misma velocidad (Vr = Vl), formando una línea uniforme recta.
    
    El robot mantiene un vector de empuje simétrico, al no existir diferencia de velocidad entre actuadores, la velocidad angular es cero.
    
    Para su verificación ver video LineaRecta.
    
2. Trayectoria con variaciones (Curvas)
    
    Esta trayectoria se logra cuando en un periodo de tiempo t las velocidades difieren en un valor de 1 (Vr = 3, Vl = 2) y pasado t el valor se invierte (Vr = 2, Vl = 3) repitiendo t cuando pase el ciclo de tiempo indicado en el código.
    
    Esto crea un movimiento curvo que alterna hacia la izquierda y hacia la derecha, forzando al robot a abandonar el eje recto.
    
    El resultado visual es una serie de curvas o “S” donde el robot oscila alrededor de una trayectoria central.
    
    Para su verificación ver video ExtensionS.
    

## Desafío

### Línea Recta

La línea recta se define por la igualdad absoluta de velocidades (Vr= Vl), dando como resultado rumbo constante. En términos cinemáticos, el centro del robot se desplaza sin rotación.

Para su verificación ver video LineaRecta.

### Curva

Para esta curva también tomamos como referencia la “S” mencionada en la trayectoria con variaciones, en donde (Vr ≠ Vl) y como resultado el robot cambia su radio de giro de forma continua, pasando de un giro de un lado a un giro hacia el lado opuesto.

Para su verificación ver video Curva.

### Circulo

Para lograr el circulo, se mantiene una diferencia constante fija entre las velocidades de las ruedas (Vr ≠ Vl) durante todo el recorrido. 

Como resultado el robot describe una trayectoria cerrada con un radio de curvatura constante, donde la rueda exterior recorre una distancia mayor que la interior en el mismo intervalo de tiempo. 

Para su verificación ver video Circulo.

### Cuadrado

Es una trayectoria compuesta que alterna tramos de traslación pura (Vr = Vl) con tramos de rotación puntual (Vr = -Vl).

Para lograr el resultado se requiere un control preciso del tiempo de ejecución para asegurar que cada giro sea de exactamente 90°. Es el experimento más sensible a las variaciones o "ruido" de los motores.

Para su verificación ver video Cuadrado.

## Preguntas de análisis

1. Que ocurre cuando ambas ruedas tienen la misma velocidad? 

R: Cuando ambas ruedas tienen la misma velocidad, el robot gira en una línea recta uniforme de manera constante.

2. Como cambia la trayectoria cuando las velocidades son diferentes? 

R: Al tener velocidades diferentes, el robot describe una trayectoria curva, este pivoteando hacia la rueda que tiene la velocidad más baja.

3. Que ocurre cuando una rueda gira en sentido opuesto a la otra? 

R: Cuando sucede eso, el robot gira entorno a su eje, la velocidad lineal es cero pero la velocidad angular es máxima.

4. Que tipo de movimiento permite dibujar un círculo?

R: Para dibujar un circulo, se requiere un movimiento con una diferencia de velocidad constante y sostenida entre ambas ruedas, generando un radio de giro fijo, y al mantenerse en el tiempo se cierra una trayectoria circular.
