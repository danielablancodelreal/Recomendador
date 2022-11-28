import pandas as pd
import re
import random

def extract():
    df = pd.read_csv('imdb_top_1000.csv',sep=',')
    return df

def transform(columna,entrada,df):
    df.drop(columns=[])
    data = []
    if columna == 'IMDB_Rating':                          #Se crea un df con todas las películas con la puntuación mínima introducida
        score = 2*int(entrada)-1
        for linea in range(0,len(df)):                      
            if df.loc[linea]['IMDB_Rating'] >= score:
                data.append(df.iloc[linea])
    else:                                                         #O con el año o género seleccionados, filtrando con regex
        for linea in range(0,len(df)):                      
            if re.search(entrada,str(df.loc[[linea],[columna]]),re.IGNORECASE):
                data.append(df.iloc[linea])

    data = pd.DataFrame(data)

    if len(data)==0:
        print('Invalid input.')
        exit(1)
    
    return data,columna,entrada,df

def load(data,columna,entrada,df):
    linea = random.randint(0,len(data)-1)          #Se elige una película de forma aleatoria entre las que cumplen los criterios
    nombre_pelicula = data.iloc[linea][1]
    year = data.iloc[linea][2]
    score = data.iloc[linea][6]
    director = data.iloc[linea][9]
    summary = data.iloc[linea][7]

    print('_________________________________________')

    print('\nName of the movie: ',nombre_pelicula)
    print('Year: ',year)
    print('Director: ',director)
    print('\nIMDB Score: ',score)
    print('Summary: ',summary,'\n')

    print('_________________________________________\n')

    repetir = input('Recommend another movie?\n·Yes\n·No\n')
    if repetir == 'yes' or repetir =='Yes' or repetir =='y' or repetir =='Y':
        data,columna,entrada,df = transform(columna,entrada,df)                 #Genera otra recomendación con los mismos parámetros
        load(data,columna,entrada,df)



if __name__ == "__main__":
    
    entrada = False
    while entrada == False:
        df = extract()
        print('1.Choose by genre\n2.Choose by release year\n3.Choose by rating')
        opcion = int(input('Choose an option (1, 2 o 3): '))
        if opcion == 1:
            print('\n· Crime\n· Drama\n· Action\n· Biography\n· History\n· Thriller\n· Adventure\n· War\n· Comedy\n· Animation\n· Romance')
            print('· Music\n· Sci-fi\n· Fantasy\n· Horror\n· Western\n· Sport\n· Family')
            entrada = str(input('\nChoose a genre: '))
            columna = 'Genre'
        elif opcion == 2:
            entrada = str(input('Release year: '))
            columna = 'Released_Year'
            if int(entrada) < 1920 or int(entrada)> 2020:
                print('Invalid year')
                exit(1)
        elif opcion == 3:
            print('\n1: ★ ☆ ☆ ☆ ☆ +\n2: ★ ★ ☆ ☆ ☆ +\n3: ★ ★ ★ ☆ ☆ +\n4: ★ ★ ★ ★ ☆ +\n5: ★ ★ ★ ★ ★ +\n')
            entrada = str(input('Minimum stars: '))
            columna = 'IMDB_Rating'
            if int(entrada) < 1 or int(entrada)> 5:
                print('Invalid rating')
                exit(1)
        else:
            print('Invalid option\n')
            exit(1)
    
    data,columna,entrada,df = transform(columna,entrada,df)
    load(data,columna,entrada,df)

