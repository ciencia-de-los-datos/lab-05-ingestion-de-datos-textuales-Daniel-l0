import os
import pandas as pd


# Definir la ruta de los directorios de entrenamiento y prueba
train_dir = 'train'
test_dir = 'test'

# Función para leer los archivos de texto y extraer los datos
def read_files(directory):
    data = []
    for sentiment in os.listdir(directory):
        sentiment_dir = os.path.join(directory, sentiment)
        # Verificar si es un directorio antes de intentar leerlo
        if os.path.isdir(sentiment_dir):
            for filename in os.listdir(sentiment_dir):
                with open(os.path.join(sentiment_dir, filename), 'r', encoding='latin-1') as file:  
                    try:
                        text = file.read()
                        data.append({'phrase': text, 'sentiment': sentiment})
                    except UnicodeDecodeError:
                        print(f"Error de decodificación en el archivo: {filename}")
    return data

# Leer los archivos de entrenamiento y prueba
train_data = read_files(train_dir)
test_data = read_files(test_dir)

# Convertir los datos en DataFrames
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

# Guardar los DataFrames en archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)
