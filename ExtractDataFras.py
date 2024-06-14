import os
from PyPDF2 import PdfReader
import pandas as pd

# Ruta de la carpeta que contiene los archivos PDF
folder_path = r"C:\Users\adria\Downloads\Facturas"

# Lista para almacenar los DataFrames de cada archivo
dfs = []

# Iterar sobre todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # Construir la ruta completa del archivo
        file_path = os.path.join(folder_path, filename)

        # Script para extraer información del PDF
        reader = PdfReader(file_path)
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        num_fra = []
        totales = []

        for line in text.split('\n'):
            if 'FACTURA N.º' in line:
                num = line.split('FACTURA N.º')[1].strip()
                num_fra.append(num)
            if 'TOTAL ' in line:
                tot = line.split('TOTAL')[1].strip()
                totales.append(tot)
        totales = totales[1] if totales else None

        # Crear el DataFrame y añadirlo a la lista
        data = {'Nº fra.': num_fra, 'Importe total': totales}
        df = pd.DataFrame(data)
        dfs.append(df)

# Concatenar todos los DataFrames en uno solo
final_df = pd.concat(dfs, ignore_index=True)

# Imprimir el DataFrame final
print(final_df)

# Exportar DataFrame
final_df.to_excel('output.xlsx',index=False)