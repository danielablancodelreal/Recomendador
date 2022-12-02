# Recomendador
El recomendador creado utiliza pandas y regex para encontrar películas en función de 3 parámetros:
- Género: devuelve una película de ese género
- Año: devuelve una película estrenada ese año
- Puntuación: devuelve una película con una puntuación igual o superior
    
Según esos criterios se crea un dataframe con todas las películas los cumplen.
Se selecciona una película de este dataframe al azar y el usuario puede pedir que se generen recomendaciones hasta que encuentre una que le gusta.
