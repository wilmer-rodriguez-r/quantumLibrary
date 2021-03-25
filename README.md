# Librería de Cuántica Básica
Esta librería consta de funciones que evalúa lo siguiente: 
- Calcular la probabilidad de que el sistema esté en una posición particular.
- Dados dos vectores ket, calcular la probabilidad de transitar del primero al segundo.
- Calcular la media y la varianza de un observable junto con su vector ket correspondiente al sistema.
- Probabilidad de que el sistema transite a alguno de los vectores propios después de la observación
- Considerar la dinámica de un sistema, calculando el vector final.

Además de estas funciones se solucionarán algunos problemas del libro, aplicando la librería y discutiremos otros puntos en este README.
## Comenzando 
En la carpeta del proyecto debes tener los siguientes archivos llamados:
* quantumLibrary.py
* quantumTest.py
* Ejercicio4.3.1.py
* Ejercicio4.3.2.py
* Ejercicio4.4.1.py
* Ejercicio4.4.2.py

Es importante que estos archivos se encuentren, ya que uno es la librería con todas las operaciones, y el otro contiene el test que más adelante ejecutaremos
para verificar que la librería funciona adecuadamente, además de unos ejercicios que discutiremos más adelante.
### Pre-requisitos
Debes tener instalado python y algún entorno de desarrollo interactivo(IDE). El IDE que recomiendo, con el cual fue hecho esta librería, es PyCharm.
### Instalación
1. Para instalar python solo debes ir al sitio web oficial de python.
2. Debes ir a la sección de "Downloads" y descargas la última versión que te recomienda. 
3. Una vez que lo tengas descargado, ejecutas el archivo y le das a instalar.
4. Para Pycharm debes hacer lo mismo, ir al sitio web y buscar la opción "descargar".
5. Ejecutas el archivo y aceptas términos y condiciones y le das en instalar.
6. Al tener descargado python, ejecutas Pycharm y abres la carpeta de la librería de complejos.
7. Verás que en un panel de la derecha de Pycharm tendrás todos los archivos de la carpeta que se usaran.
8. Si abres el archivo quantumLibrary.py podrás ver todas las operaciones que contiene la librería.
### Ejecutar el test
Para poder ejecutar el test debes ir al archivo denominado quantumTest.py y abrirlo con ayuda de Pycharm, se ejecuta el código presionando "ctrl + shift + f10".
### Análisis del Test
Con ayuda de la librería numpy y unittest el test consta del siguiente mecanismo:
1. Al ejecutar el test debera aparecer 5 checks, que corresponde a cada función de la librería.
2. Si por alguna razón votara Error, esto se debe al mal funcionamiento del código, si por el contrario saliera Failure, significa que algún caso de prueba no dio el resultado esperado, y si da OK, eso es porque el test ejecuto y los casos de prueba pasaron sin ningún inconveniente.
4. Cada función ejecuta un maximo de dos pruebas, estas pruebas son tomadas del ejemplo del libro, y los resultados esperados también son tomados del libro.
### Observaciones
Cabe aclarar para el buen funcionamiento de la librería, se deben ingresar los vectores columnas en su forma traspuesta para no tener ningún inconveniente con el funcionamiento de cada función.

Además de test de la librería, solucionaremos unos puntos establecidos en el libro con ayuda de nuestra librería, algunos de estos ejercicios también se usaron de caso de prueba en el test.

#### Ejercicio 4.3.1

Encontrar todos los posibles estados del sistema después de haber llevado a cabo la medición.

El sistema a considerar junto con su observable y el ket es:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\Omega&space;=&space;\frac{h}{2}&space;{0\&space;1\brack&space;1\0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Omega&space;=&space;\frac{h}{2}&space;{0\&space;1\brack&space;1\0}" title="\Omega = \frac{h}{2} {0\ 1\brack 1\0}" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi\rangle&space;=&space;|\uparrow\rangle&space;=&space;\begin{bmatrix}&space;1\\&space;0&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi\rangle&space;=&space;|\uparrow\rangle&space;=&space;\begin{bmatrix}&space;1\\&space;0&space;\end{bmatrix}" title="|\psi\rangle = |\uparrow\rangle = \begin{bmatrix} 1\\ 0 \end{bmatrix}" /></a></p>

Consideraremos los calculos sin la constante h/2. Como sabemos los vectores propios del vector son los estados posibles a los cuales el sistema puede transitar, con ayuda de numpy encontramos los siguientes vectores propios:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=v_1&space;=&space;\begin{bmatrix}&space;0.7071\\&space;-0.7071&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;\frac{\sqrt{2}}{2}\\&space;-\frac{\sqrt{2}}{2}&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v_1&space;=&space;\begin{bmatrix}&space;0.7071\\&space;-0.7071&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;\frac{\sqrt{2}}{2}\\&space;-\frac{\sqrt{2}}{2}&space;\end{bmatrix}" title="v_1 = \begin{bmatrix} 0.7071\\ -0.7071 \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{2}}{2}\\ -\frac{\sqrt{2}}{2} \end{bmatrix}" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=v_2&space;=&space;\begin{bmatrix}&space;0.7071\\&space;0.7071&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;\frac{\sqrt{2}}{2}\\&space;\frac{\sqrt{2}}{2}&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v_2&space;=&space;\begin{bmatrix}&space;0.7071\\&space;0.7071&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;\frac{\sqrt{2}}{2}\\&space;\frac{\sqrt{2}}{2}&space;\end{bmatrix}" title="v_2 = \begin{bmatrix} 0.7071\\ 0.7071 \end{bmatrix} = \begin{bmatrix} \frac{\sqrt{2}}{2}\\ \frac{\sqrt{2}}{2} \end{bmatrix}" /></a></p>

Estos serian los estados posibles después de haber llevado la medición. Puede encontrar el codigo en Ejercicio4.3.1.py.

#### Ejercicio 4.3.2

Encontrar la probabilidad con el que el sistema puede moverse a los vectores propios.

Con ayuda de la función quatumMeasuring de la librería de python nos da los siguientes resultados:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\langle&space;\psi|v_1\rangle|^2&space;=&space;0.5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\langle&space;\psi|v_1\rangle|^2&space;=&space;0.5" title="|\langle \psi|v_1\rangle|^2 = 0.5" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\langle&space;\psi|v_2\rangle|^2&space;=&space;0.5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\langle&space;\psi|v_2\rangle|^2&space;=&space;0.5" title="|\langle \psi|v_2\rangle|^2 = 0.5" /></a></p>

Puede corroborar este resultado usando la librería, ingresando el observable del anterior punto sin considerar la constante junto con el vector ket, y notara que da estos resultados. Puede encontrar este codigo en eel archivo Ejercicio4.3.2.py.

#### Ejercicio 4.4.1

Verifique que al multiplicar las siguientes matrices unitarias, la matriz resultante también es unitaria.

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=U_1&space;=&space;\begin{bmatrix}&space;0&space;&&space;1&space;\\&space;1&space;&&space;0&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U_1&space;=&space;\begin{bmatrix}&space;0&space;&&space;1&space;\\&space;1&space;&&space;0&space;\end{bmatrix}" title="U_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=U_2&space;=&space;\begin{bmatrix}&space;\frac{\sqrt{2}}{2}&space;&&space;\frac{\sqrt{2}}{2}&space;\\&space;\frac{\sqrt{2}}{2}&space;&&space;-\frac{\sqrt{2}}{2}&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U_2&space;=&space;\begin{bmatrix}&space;\frac{\sqrt{2}}{2}&space;&&space;\frac{\sqrt{2}}{2}&space;\\&space;\frac{\sqrt{2}}{2}&space;&&space;-\frac{\sqrt{2}}{2}&space;\end{bmatrix}" title="U_2 = \begin{bmatrix} \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} \end{bmatrix}" /></a></p>

Con ayuda de una función implementada para este problema llamada multmatrices, calcularemos la matriz resultante y junto a esto corroboraremos si esta es unitaria, la matriz resultante es:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=U_3&space;=&space;\begin{bmatrix}&space;0.7071&space;&-0.7071&space;\\&space;0.7071&space;&&space;0.7071&space;\end{bmatrix}=\begin{bmatrix}&space;\frac{\sqrt{2}}{2}&space;&-\frac{\sqrt{2}}{2}&space;\\&space;\frac{\sqrt{2}}{2}&\frac{\sqrt{2}}{2}&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U_3&space;=&space;\begin{bmatrix}&space;0.7071&space;&-0.7071&space;\\&space;0.7071&space;&&space;0.7071&space;\end{bmatrix}=\begin{bmatrix}&space;\frac{\sqrt{2}}{2}&space;&-\frac{\sqrt{2}}{2}&space;\\&space;\frac{\sqrt{2}}{2}&\frac{\sqrt{2}}{2}&space;\end{bmatrix}" title="U_3 = \begin{bmatrix} 0.7071 &-0.7071 \\ 0.7071 & 0.7071 \end{bmatrix}=\begin{bmatrix} \frac{\sqrt{2}}{2} &-\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2}&\frac{\sqrt{2}}{2} \end{bmatrix}" /></a></p>

Puede corroborar que esta matriz es unitaria, este ejercicio se encuentra en el codigo Ejercicio4.4.1.py.

#### Ejercicio 4.4.2

Calcular el vector final, después de tres clicks con la siguiente matriz unitaria junto con el vector ket:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=U&space;=\begin{bmatrix}&space;0&space;&&space;\frac{1}{\sqrt{2}}&space;&&space;\frac{1}{\sqrt{2}}&space;&&space;0\\&space;\frac{i}{\sqrt{2}}&space;&&space;0&space;&&space;0&space;&&space;\frac{1}{\sqrt{2}}&space;\\&space;\frac{1}{\sqrt{2}}&space;&&space;0&space;&&space;0&space;&&space;\frac{i}{\sqrt{2}}&space;\\&space;0&space;&&space;\frac{1}{\sqrt{2}}&space;&&space;-\frac{1}{\sqrt{2}}&space;&&space;0&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U&space;=\begin{bmatrix}&space;0&space;&&space;\frac{1}{\sqrt{2}}&space;&&space;\frac{1}{\sqrt{2}}&space;&&space;0\\&space;\frac{i}{\sqrt{2}}&space;&&space;0&space;&&space;0&space;&&space;\frac{1}{\sqrt{2}}&space;\\&space;\frac{1}{\sqrt{2}}&space;&&space;0&space;&&space;0&space;&&space;\frac{i}{\sqrt{2}}&space;\\&space;0&space;&&space;\frac{1}{\sqrt{2}}&space;&&space;-\frac{1}{\sqrt{2}}&space;&&space;0&space;\end{bmatrix}" title="U =\begin{bmatrix} 0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0\\ \frac{i}{\sqrt{2}} & 0 & 0 & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & 0 & 0 & \frac{i}{\sqrt{2}} \\ 0 & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} & 0 \end{bmatrix}" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi\rangle&space;=&space;\begin{bmatrix}&space;1\\&space;0\\&space;0\\&space;0&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi\rangle&space;=&space;\begin{bmatrix}&space;1\\&space;0\\&space;0\\&space;0&space;\end{bmatrix}" title="|\psi\rangle = \begin{bmatrix} 1\\ 0\\ 0\\ 0 \end{bmatrix}" /></a></p>

Al evaluar el vector final despues de los tres clicks, con ayuda de la función quatumDynamics, obtenemos el siguiente resultado:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi\rangle&space;=\begin{bmatrix}&space;0&space;\\&space;-0.7071&space;&plus;&space;0.7071i\\&space;0\\&space;0&space;\end{bmatrix}=\begin{bmatrix}&space;0&space;\\&space;-\frac{\sqrt{2}}{2}&space;&plus;&space;\frac{\sqrt{2}}{2}i\\&space;0\\&space;0&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi\rangle&space;=\begin{bmatrix}&space;0&space;\\&space;-0.7071&space;&plus;&space;0.7071i\\&space;0\\&space;0&space;\end{bmatrix}=\begin{bmatrix}&space;0&space;\\&space;-\frac{\sqrt{2}}{2}&space;&plus;&space;\frac{\sqrt{2}}{2}i\\&space;0\\&space;0&space;\end{bmatrix}" title="|\psi\rangle =\begin{bmatrix} 0 \\ -0.7071 + 0.7071i\\ 0\\ 0 \end{bmatrix}=\begin{bmatrix} 0 \\ -\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i\\ 0\\ 0 \end{bmatrix}" /></a></p>

Ahora pasados los ejercicios anteriores, vamos a discutir los siguientes ejercicios, explicando paso a paso sobre estos. Puede encontrar este codigo en el archivo Ejercicio4.4.2.

#### Ejercicio 4.5.2.

Nos piden determinar el vector estado de dos partículas por medio de su spin.
Consideremos que cuando hablamos del spin de una partícula podemos decir que posee un spin-up o un spin-down, es decir:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\uparrow\rangle&space;=&space;\begin{bmatrix}&space;1\\&space;0&space;\end{bmatrix}\&space;|\downarrow\rangle&space;=&space;\begin{bmatrix}&space;0\\&space;1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\uparrow\rangle&space;=&space;\begin{bmatrix}&space;1\\&space;0&space;\end{bmatrix}\&space;|\downarrow\rangle&space;=&space;\begin{bmatrix}&space;0\\&space;1&space;\end{bmatrix}" title="|\uparrow\rangle = \begin{bmatrix} 1\\ 0 \end{bmatrix}\ |\downarrow\rangle = \begin{bmatrix} 0\\ 1 \end{bmatrix}" /></a></p>

Si miramos el sistema de una partícula seria la siguiente combinación lineal:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi\rangle&space;=&space;c_1|\uparrow\rangle&space;&plus;&space;c_2|\downarrow\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi\rangle&space;=&space;c_1|\uparrow\rangle&space;&plus;&space;c_2|\downarrow\rangle" title="|\psi\rangle = c_1|\uparrow\rangle + c_2|\downarrow\rangle" /></a></p>

Donde <a href="https://www.codecogs.com/eqnedit.php?latex=c_1,&space;c_2&space;\&space;\epsilon&space;\&space;\mathbb{C}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_1,&space;c_2&space;\&space;\epsilon&space;\&space;\mathbb{C}" title="c_1, c_2 \ \epsilon \ \mathbb{C}" /></a>.

Esto seria considerando una particula, ahora bien pensemos que tenemos dos particulas con sus respectivos sistemas:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi_x\rangle&space;=&space;c_x_0|\uparrow\rangle&space;&plus;&space;c_x_1&space;|\downarrow\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi_x\rangle&space;=&space;c_x_0|\uparrow\rangle&space;&plus;&space;c_x_1&space;|\downarrow\rangle" title="|\psi_x\rangle = c_x_0|\uparrow\rangle + c_x_1 |\downarrow\rangle" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi_y\rangle&space;=&space;c_y_0|\uparrow\rangle&space;&plus;&space;c_y_1&space;|\downarrow\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi_y\rangle&space;=&space;c_y_0|\uparrow\rangle&space;&plus;&space;c_y_1&space;|\downarrow\rangle" title="|\psi_y\rangle = c_y_0|\uparrow\rangle + c_y_1 |\downarrow\rangle" /></a></p>

Ahora fusionando esto dos sistemas obtenemos la siguiente combinación lineal que se encuentra en <a href="https://www.codecogs.com/eqnedit.php?latex=\mathbb{C}^4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathbb{C}^4" title="\mathbb{C}^4" /></a>.

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi\rangle&space;=&space;c_x_0c_y_0|\uparrow\rangle&space;\otimes&space;|\uparrow\rangle&space;&plus;&space;c_x_1c_y_0|\downarrow\rangle&space;\otimes&space;|\uparrow\rangle&space;&plus;&space;c_x_0c_y_1|\uparrow\rangle&space;\otimes&space;|\downarrow\rangle&space;&plus;c_x_1c_y_1|\downarrow\rangle&space;\otimes&space;|\downarrow\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi\rangle&space;=&space;c_x_0c_y_0|\uparrow\rangle&space;\otimes&space;|\uparrow\rangle&space;&plus;&space;c_x_1c_y_0|\downarrow\rangle&space;\otimes&space;|\uparrow\rangle&space;&plus;&space;c_x_0c_y_1|\uparrow\rangle&space;\otimes&space;|\downarrow\rangle&space;&plus;c_x_1c_y_1|\downarrow\rangle&space;\otimes&space;|\downarrow\rangle" title="|\psi\rangle = c_x_0c_y_0|\uparrow\rangle \otimes |\uparrow\rangle + c_x_1c_y_0|\downarrow\rangle \otimes |\uparrow\rangle + c_x_0c_y_1|\uparrow\rangle \otimes |\downarrow\rangle +c_x_1c_y_1|\downarrow\rangle \otimes |\downarrow\rangle" /></a></p>

Consideremos lo anterior pero con tres particulas fusionandolos en un mismo sistema. Procediendo a evaluar el producto tensor con ayuda del resultado anterior obtenemos el siguiente sistema que se encuentra en <a href="https://www.codecogs.com/eqnedit.php?latex=\mathbb{C}^8" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathbb{C}^8" title="\mathbb{C}^8" /></a>.

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi\rangle&space;=&space;c_0|\uparrow\rangle\otimes|\uparrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;c_1|\downarrow\rangle\otimes|\uparrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;c_2|\downarrow\rangle\otimes|\downarrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;\\c_3|\downarrow\rangle\otimes|\downarrow\rangle\otimes|\downarrow\rangle&space;&plus;&space;c_4|\uparrow\rangle\otimes|\downarrow\rangle\otimes|\downarrow\rangle&space;&plus;&space;c_5|\uparrow\rangle\otimes|\uparrow\rangle\otimes|\downarrow\rangle&space;&plus;&space;\\&space;c_6|\uparrow\rangle\otimes|\downarrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;c_7|\downarrow\rangle\otimes|\uparrow\rangle\otimes|\downarrow\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi\rangle&space;=&space;c_0|\uparrow\rangle\otimes|\uparrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;c_1|\downarrow\rangle\otimes|\uparrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;c_2|\downarrow\rangle\otimes|\downarrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;\\c_3|\downarrow\rangle\otimes|\downarrow\rangle\otimes|\downarrow\rangle&space;&plus;&space;c_4|\uparrow\rangle\otimes|\downarrow\rangle\otimes|\downarrow\rangle&space;&plus;&space;c_5|\uparrow\rangle\otimes|\uparrow\rangle\otimes|\downarrow\rangle&space;&plus;&space;\\&space;c_6|\uparrow\rangle\otimes|\downarrow\rangle\otimes|\uparrow\rangle&space;&plus;&space;c_7|\downarrow\rangle\otimes|\uparrow\rangle\otimes|\downarrow\rangle" title="|\psi\rangle = c_0|\uparrow\rangle\otimes|\uparrow\rangle\otimes|\uparrow\rangle + c_1|\downarrow\rangle\otimes|\uparrow\rangle\otimes|\uparrow\rangle + c_2|\downarrow\rangle\otimes|\downarrow\rangle\otimes|\uparrow\rangle + \\c_3|\downarrow\rangle\otimes|\downarrow\rangle\otimes|\downarrow\rangle + c_4|\uparrow\rangle\otimes|\downarrow\rangle\otimes|\downarrow\rangle + c_5|\uparrow\rangle\otimes|\uparrow\rangle\otimes|\downarrow\rangle + \\ c_6|\uparrow\rangle\otimes|\downarrow\rangle\otimes|\uparrow\rangle + c_7|\downarrow\rangle\otimes|\uparrow\rangle\otimes|\downarrow\rangle" /></a></p>

Si miraramos n particulas, el sistema final estaría en  <a href="https://www.codecogs.com/eqnedit.php?latex=\mathbb{C}^{2^{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathbb{C}^{2^{n}}" title="\mathbb{C}^{2^{n}}" /></a>, quiere decir que el sistema crece de forma exponencial cuando se entrelazan los sistemas.

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\psi\rangle&space;=&space;c_0|\uparrow\rangle\otimes...|\uparrow\rangle&space;&plus;&space;...&space;&plus;&space;c_{2^{n}-1}|\downarrow\rangle\otimes...|\downarrow\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\psi\rangle&space;=&space;c_0|\uparrow\rangle\otimes...|\uparrow\rangle&space;&plus;&space;...&space;&plus;&space;c_{2^{n}-1}|\downarrow\rangle\otimes...|\downarrow\rangle" title="|\psi\rangle = c_0|\uparrow\rangle\otimes...|\uparrow\rangle + ... + c_{2^{n}-1}|\downarrow\rangle\otimes...|\downarrow\rangle" /></a></p>

#### Ejercicio 4.5.3

Ver si el siguiente estado es separable:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi\rangle&space;=&space;|x_0\rangle&space;\otimes&space;|y_1\rangle&space;&plus;&space;|x_1\rangle&space;\otimes|y_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi\rangle&space;=&space;|x_0\rangle&space;\otimes&space;|y_1\rangle&space;&plus;&space;|x_1\rangle&space;\otimes|y_1\rangle" title="|\phi\rangle = |x_0\rangle \otimes |y_1\rangle + |x_1\rangle \otimes|y_1\rangle" /></a></p>

Si expandiéramos, el sistema completo sería:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi\rangle&space;=&space;0*|x_0\rangle&space;\otimes&space;|y_0\rangle&space;&plus;|x_0\rangle&space;\otimes&space;|y_1\rangle&space;&plus;0*|x_0\rangle&space;\otimes&space;|y_1\rangle&plus;&space;|x_1\rangle&space;\otimes|y_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi\rangle&space;=&space;0*|x_0\rangle&space;\otimes&space;|y_0\rangle&space;&plus;|x_0\rangle&space;\otimes&space;|y_1\rangle&space;&plus;0*|x_0\rangle&space;\otimes&space;|y_1\rangle&plus;&space;|x_1\rangle&space;\otimes|y_1\rangle" title="|\phi\rangle = 0*|x_0\rangle \otimes |y_0\rangle +|x_0\rangle \otimes |y_1\rangle +0*|x_0\rangle \otimes |y_1\rangle+ |x_1\rangle \otimes|y_1\rangle" /></a></p>

Consideremos que este sistema esta entrelazado por los siguientes dos sistemas:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi_x\rangle&space;=&space;c_{x_{0}}|x_0\rangle&space;&plus;c_{x_{1}}|x_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi_x\rangle&space;=&space;c_{x_{0}}|x_0\rangle&space;&plus;c_{x_{1}}|x_1\rangle" title="|\phi_x\rangle = c_{x_{0}}|x_0\rangle +c_{x_{1}}|x_1\rangle" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi_y\rangle&space;=&space;c_{y_{0}}|y_0\rangle&space;&plus;c_{y_{1}}|y_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi_y\rangle&space;=&space;c_{y_{0}}|y_0\rangle&space;&plus;c_{y_{1}}|y_1\rangle" title="|\phi_y\rangle = c_{y_{0}}|y_0\rangle +c_{y_{1}}|y_1\rangle" /></a></p>

Ahora evaluaremos su producto tensor que estaria en el espacio <a href="https://www.codecogs.com/eqnedit.php?latex=\mathbb{C}^4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathbb{C}^4" title="\mathbb{C}^4" /></a>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi\rangle&space;=&space;c_{x_{0}}c_{y_{0}}|x_0\rangle\otimes|y_0\rangle&space;&plus;&space;c_{x_{1}}c_{y_{0}}|x_1\rangle\otimes|y_0\rangle&space;&plus;c_{x_{0}}c_{y_{1}}|x_0\rangle\otimes|y_1\rangle&plus;c_{x_{1}}c_{y_{1}}|x_1\rangle\otimes|y_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi\rangle&space;=&space;c_{x_{0}}c_{y_{0}}|x_0\rangle\otimes|y_0\rangle&space;&plus;&space;c_{x_{1}}c_{y_{0}}|x_1\rangle\otimes|y_0\rangle&space;&plus;c_{x_{0}}c_{y_{1}}|x_0\rangle\otimes|y_1\rangle&plus;c_{x_{1}}c_{y_{1}}|x_1\rangle\otimes|y_1\rangle" title="|\phi\rangle = c_{x_{0}}c_{y_{0}}|x_0\rangle\otimes|y_0\rangle + c_{x_{1}}c_{y_{0}}|x_1\rangle\otimes|y_0\rangle +c_{x_{0}}c_{y_{1}}|x_0\rangle\otimes|y_1\rangle+c_{x_{1}}c_{y_{1}}|x_1\rangle\otimes|y_1\rangle" /></a></p>

Como podemos ver este sistema y el que expandimos, podemos obtener las siguientes ecucaciones:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\begin{matrix}&space;c_{x_{0}}c_{y_{0}}&space;=&space;0\\&space;c_{x_{1}}c_{y_{0}}&space;=&space;0\\&space;c_{x_{0}}c_{y_{1}}&space;=&space;1\\&space;c_{x_{1}}c_{y_{1}}&space;=&space;1&space;\end{matrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{matrix}&space;c_{x_{0}}c_{y_{0}}&space;=&space;0\\&space;c_{x_{1}}c_{y_{0}}&space;=&space;0\\&space;c_{x_{0}}c_{y_{1}}&space;=&space;1\\&space;c_{x_{1}}c_{y_{1}}&space;=&space;1&space;\end{matrix}" title="\begin{matrix} c_{x_{0}}c_{y_{0}} = 0\\ c_{x_{1}}c_{y_{0}} = 0\\ c_{x_{0}}c_{y_{1}} = 1\\ c_{x_{1}}c_{y_{1}} = 1 \end{matrix}" /></a></p>

Como podemos ver la constante <a href="https://www.codecogs.com/eqnedit.php?latex=c_{y_{0}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{y_{0}}" title="c_{y_{0}}" /></a>, tiene que ser obligatoriamente igual a cero para que el sistema de ecuaciones tenga solución y consistencia.

Al solucionar este sistema de ecuaciones podemos ver que es de infinitas soluciones, ya que una variable queda libre.

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=\begin{matrix}&space;c_{y_{0}}&space;=&space;0\\&space;c_{y_{1}}&space;=\frac{1}{c_{x_{0}}}\\&space;c_{x_{1}}&space;=&space;c_{x_{0}}\\&space;c_{x_{0}}&space;=&space;c_{x_{0}}&space;\end{matrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{matrix}&space;c_{y_{0}}&space;=&space;0\\&space;c_{y_{1}}&space;=\frac{1}{c_{x_{0}}}\\&space;c_{x_{1}}&space;=&space;c_{x_{0}}\\&space;c_{x_{0}}&space;=&space;c_{x_{0}}&space;\end{matrix}" title="\begin{matrix} c_{y_{0}} = 0\\ c_{y_{1}} =\frac{1}{c_{x_{0}}}\\ c_{x_{1}} = c_{x_{0}}\\ c_{x_{0}} = c_{x_{0}} \end{matrix}" /></a></p>

Entonces podemos decir que el sistema si se puede separar porque existen soluciones al sistemas de ecuaciones, una posible solución seria:

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi_x\rangle&space;=&space;4|x_0\rangle&space;&plus;&space;4|x_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi_x\rangle&space;=&space;4|x_0\rangle&space;&plus;&space;4|x_1\rangle" title="|\phi_x\rangle = 4|x_0\rangle + 4|x_1\rangle" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi_y\rangle&space;=\frac{1}{4}|y_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi_y\rangle&space;=\frac{1}{4}|y_1\rangle" title="|\phi_y\rangle =\frac{1}{4}|y_1\rangle" /></a></p>

Esto se puede corroborar haciendo su producto tensor.

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi\rangle&space;=4*0|x_0\rangle\otimes|y_0\rangle&space;&plus;4*0|x_1\rangle\otimes|y_0\rangle&plus;4*\frac{1}{4}|x_0\rangle\otimes|y_1\rangle&plus;4*\frac{1}{4}|x_1\rangle\otimes|y_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi\rangle&space;=4*0|x_0\rangle\otimes|y_0\rangle&space;&plus;4*0|x_1\rangle\otimes|y_0\rangle&plus;4*\frac{1}{4}|x_0\rangle\otimes|y_1\rangle&plus;4*\frac{1}{4}|x_1\rangle\otimes|y_1\rangle" title="|\phi\rangle =4*0|x_0\rangle\otimes|y_0\rangle +4*0|x_1\rangle\otimes|y_0\rangle+4*\frac{1}{4}|x_0\rangle\otimes|y_1\rangle+4*\frac{1}{4}|x_1\rangle\otimes|y_1\rangle" /></a></p>

<p align="center"><a href="https://www.codecogs.com/eqnedit.php?latex=|\phi\rangle&space;=|x_0\rangle\otimes|y_1\rangle&plus;|x_1\rangle\otimes|y_1\rangle" target="_blank"><img src="https://latex.codecogs.com/gif.latex?|\phi\rangle&space;=|x_0\rangle\otimes|y_1\rangle&plus;|x_1\rangle\otimes|y_1\rangle" title="|\phi\rangle =|x_0\rangle\otimes|y_1\rangle+|x_1\rangle\otimes|y_1\rangle" /></a></p>

En conclusión, el sistema inicial que nos dieron si es separable, y puede separarse de infinitas formas.
### Construido con
* Python - Lenguaje de Programación
* Pycharm - IDE
* Git - Control de versiones
* GitHub - Aloja las versiones de Git
### Autores
* Wilmer Rodríguez
### Expresiones de Gratitud
Gracias a todo aquel que use esta librería, espero que les sea de ayuda.
