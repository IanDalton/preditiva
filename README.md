# TODO
- [X] Mostrar de los directores cuantas otras obras dirigieron
- [x] Mostrar de los escritores cuantas otras obras escribieron
    - [] Sum of expirience
    - [X] avg of experience
- [x] Si no, ver si se puede hacer un one hot encoding de los directores y escritores
    - Muchos directores. Pide +1tb de ram
- [X] Ver si se puede hacer una columna que diga si estos escribieron antes o no
- [X] Paises de origen si hay
- [X] Cuantas companias producen la pelicula
- [X] Experiencia de las companias
- [X] Paises de la pelicula
- [X] "Experiencia" del pais
- [ ] Rating promedio del genero
- [ ] Rating promedio del pais
    - Estos podrian adaptarse a cantidad por genero
    - Mas que rating podria ser 
- [ ] Experiencia de directores por genero
- [X] Votos acumulados por director
- [X] Runtime promedio de los directores
- [X] runtime total de los directores
    - Se uso el promedio
- [X] Experiencia maxima del director mas experimentado
- [X] Experiencia minima del director menos experimentado
- [X] Corregir isAdult
- [X] Splitear bien el train y el test
    - Video tiene true y false. No se puede llenar de 0s
- [X] Promediar columnas
- [] Desvio standard de las cosas
- [] Mediana de las cosas
- [] Indicador de datos faltantes
- [] EndTailImputer
- [X] RareLabelEncoder
    - No sumo, tener en cuenta para optimizar memoria
- [] Leer feature-engine encoding
- [X] Transformaciones
- [X] Ver de implementar el pipeline. scikit learn
    - Developing scikit learn estimators
- [X] OOB predictions
    - Es solo para random forest
- [] Antiguedad
- [] Terminar de adaptar todo a pipeline
- [] Reducir el nro de columnas

 

# Modelos a probar

- [X] Auto-sklearn
    - Esta roto
- [X] Random Forest
- [X] XGBoost
    -[] Completar los missing with k-neareas neighbors
    -[] Feature scaling
    -[] Huber loss or Tukey loss
    -[] Feature selection
    
- [] LightGBM
    - Esta bueno, experimentar un poco mas
- [X] K-nearest neighbors regression
    - Malo 
- [X] Support Vector Machine regression
    - Lentisimo 
- [X] Red Neuronal regresion
- [X] K-means regression
    - Malo 



# preditiva
Realizar una “submission” a la siguiente competencia de Kaggle:
https://www.kaggle.com/competitions/tp2-predictivo-2023q2
El día del examen debe hacer una presentación de a lo sumo 10 minutos que incluya por
lo menos las siguientes secciones:
1. Modelo baseline. Describir el modelo usado como baseline (un modelo baseline es
un modelo que se puede entrenar rápidamente cuyo rendimiento sirve como punto
de referencia). ¿Qué features usa? ¿Qué rendimiento alcanza?
2. Selección de modelos. Describir la/s estrategia/s usada/s para probar y evaluar
modelos y sus posibles configuraciones. ¿Qué modelos probó? ¿Qué
configuraciones probó y cómo? ¿Por qué? (una configuración es, por ejemplo, un
conjunto de features, una manera específica de codificar features, o un conjunto
específico de hiperparámetros)
3. Descripción del modelo final. Describir el modelo final seleccionado. ¿Cómo llegó
a este modelo? ¿Qué features usa? ¿Qué rendimiento alcanza?
4. Limitaciones y posibles mejoras. Definir qué aspectos se pueden mejorar de tener
más tiempo o recursos disponibles.
El principal objetivo de la presentación es que usted demuestre que no obtuvo un resultado
de casualidad, ni se lo copió, sino que realmente entiende el funcionamiento de lo que su
código hace.
El día del examen también deberá enviar por mail uno o más links a un repositorio de
Github o una carpeta de Google Drive que contenga:
a. La presentación (PDF o PPT formato ITBA).
b. Una notebook o script que entrene y guarde el modelo final. Al ser ejecutado,
este archivo debe permitir replicar perfectamente el modelo final, dados los datos de
entrada. Debe excluir cualquier código que no sirva para realizar esto.
c. Una notebook o script que aplique el modelo final a los datos de test. Al ser
ejecutado, este archivo debe permitir replicar perfectamente el archivo enviado a la

competencia, dados los datos de entrada y el modelo final generado en b. Debe
excluir cualquier código que no sirva para realizar esto.
No es requisito entregar el código que realiza todas las pruebas necesarias para llegar al
modelo final, pero puede enviarlo en notebooks/scripts por separado si así lo desea.
Este examen es individual.
Excelencia: si usted aspira a un trabajo sobresaliente deberá tener de los mejores scores de
la comisión. Deberá tener un excelente entendimiento de la base, del trabajo realizado, del
algoritmo elegido y su superioridad respecto a otros posibles. Su presentación deberá ser
clara y precisa.
Sugerencias: ser conciso/a. Evitar entrar en detalles innecesarios. Usar imágenes, gráficos,
diagramas, etc. que sirvan para explicar lo que hicieron — si no sirven, no incluirlos. Se
puede incluir un anexo al final con información adicional que sirva para responder
eventuales preguntas o para entender mejor aspectos no esenciales.
