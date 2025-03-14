# Proyecto 1 - Predicción del rendimiento estudiantil de alumnos de preparatoria en lengua portuguesa

Integrantes del equipo:

- Mónica Lizette Cardona Solís
- Marianna Montserrat Curiel Zambrano
- Fernando Mendoza Velasco

El dataset seleccionado surge a partir de un estudio que analiza el rendimiento estudiantil en educación media superior en dos escuelas portuguesas. Los atributos de los datos incluyen calificaciones estudiantiles, características demográficas, sociales y escolares, y se recopilaron mediante informes escolares y cuestionarios. Se muestran dos conjuntos de datos sobre el rendimiento en la asignatura de lengua portuguesa (POR). Dicho modelo fue hecho a partir de métodos de clasificación y regresión binaria o de cinco niveles. El atributo objetivo G3 que indica la calificación final del año escolar, por lo que la función objetivo fue deducida en base a este y a los demás atributos fuertemente relacionados con este.

## Dataset

Publicado por el usuario "Data-Science Sean" como [Student Performance Data Set](https://www.kaggle.com/datasets/larsen0966/student-performance-data-set) en Kaggle. Consultado el 10 de marzo de 2025, última actualización en 2020.

## Get Started

Aunque puede contribuirse al proyecto desde cualquier IDE, los siguientes pasos usan VS Code.

### 1. Clonar repositorio

Desde VS Code, abre la pestaña "source control" a la izquierda y presiona "Clonar repositorio". Luego, pega la URL de este repositorio:

![Clonar repositorio desde VS Code](img/clonar_github.png)

Después, elige la carpeta donde quieres guardar el repositorio.

También puedes clonar usando el siguiente comando:

```
git clone https://github.com/Frozen-Burrito/sim-matematica.git
```

Después de clonar, puedes abrir el repositorio en tu IDE de preferencia.

### 2. Configurar el entorno

Este proyecto usa Python para el análisis de datos y la optimización. Descarga e instala Python 3, si no lo tienes instalado ya.

Recomendamos usar un entorno virtual para instalar las dependencias. Para crear un nuevo entorno virtual, ejecuta el siguiente comando desde el directorio raíz del repositorio:

```
python -m venv /path/to/new/virtual/environment
```

Después, usa uno de los comandos de [esta tabla](https://docs.python.org/3/library/venv.html#how-venvs-work) para activar el entorno virtual.

Con el entorno virtual activo, ejecuta el siguiente comando desde el directorio raíz para instalar todos los paquetes usados por el proyecto:

```
pip install -r requirements.txt
```

### 3. Ejecutar el código

Todo el código del proyecto está en el Jupyter Notebook del archivo `ProyectoModulo1_CardonaM_CurielM_MendozaF.ipynb`. Para ejecutar el código en VS Code:

1. Abre el archivo con el Jupyter Notebook. 
2. Elige el kernel de Python.
    
    a. Presiona el botón **Elegir kernel**, en la esquina superior derecha.
  
    b. Presiona la opción **Elegir otro kernel**.
  
    c. Presiona la opción **Entornos de Python...**.
    
    d. En la lista, busca el entorno virtual que creaste y selecciónalo.

3. Presiona el botón con el ícono "play" para ejecutar el código. Puedes ejecutar una celda a la vez, o todas las celdas.

## Metodología
Se inició seleccionando un data set que incluyera previamente un documento CSV y la descripción de la mayoría de las variables presentadas. Una vez hecho eso, se realizó un análisis exploratorio de los datos, el cual consistió en entender las variables involucradas, visuzalizar algunos de los datos de forma gráfica y buscar correlaciones entre estos. Posteriormente se definió la variable objetivo la cual, para este caso, fue G3, que indica la calificación final de los estudiantes en la materia de lengua Portuguesa. Con esto y utilizando las relaciones encontradas entre las diferentes variables, se busco implementar la función objetivo excluyendo G1 y G2, que son las calificaciones de los primeros dos parciales. Para esto, se experimentó utilizando regresión lineal y clasificación binaria a través de regresión logística.

## Bibliografía

Amazon- (s.f.). ¿Qué es la regression lineal?. Obtenido de aws amazon: https://aws.amazon.com/es/what-is/linear-regression/ 

Cortez, P. (2020). Student Performance Data Set. Obtenido de Kaggle: https://www.kaggle.com/datasets/larsen0966/student-performance-data-set

Cortez, P., & Silva, A. (2008). Using data minig to predict secondary school student performance. University of Minho, 1-8.

Qlik. (s.f.). Puntuación de modelos de clasificación binaria. Obtenido de Qlik.com: https://help.qlik.com/es-ES/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/scoring-binary-classification.htm#:~:text=Los%20modelos%20de%20clasificaci%C3%B3n%20binaria,fuertes%20y%20d%C3%A9biles%20del%20modelo.

Shizuya, Y. (30 de April de 2024). Gentle introduction of Multiple linear regression. Obtenido de Medium: https://medium.com/intuition/gentle-introduction-of-multiple-linear-regression-e42fb21bbc8c