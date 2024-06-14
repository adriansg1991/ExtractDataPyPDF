# ℹ️ Extracción de datos en PDF's - Librería PyPDF2
[![Python Version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)
![PyPDF2 - Version](https://img.shields.io/pypi/v/pypdf2)
[![Pandas](https://img.shields.io/badge/pandas-1.2.0+-yellow)](https://pandas.pydata.org/)

## 📦 Librería PyPDF2
PyPDF2 es una biblioteca de Python diseñada para trabajar con archivos PDF. Proporciona funciones para extraer información y realizar diversas operaciones en documentos PDF, como la fusión de archivos, la división de páginas y la extracción de texto.
En el contexto de la contabilización de facturas, PyPDF2 puede ser utilizado para extraer texto e información relevante de archivos PDF que contienen datos de facturas.
La contabilización de facturas emerge como una de las labores más monótonas para cualquier contable, llegando a absorber hasta un 80% de su jornada laboral en muchas ocasiones.
Con mi constante búsqueda de soluciones para automatizar procesos, he aprovechado mi experiencia en Python para descubrir una librería sumamente valiosa en este ámbito: PyPDF2. Esta herramienta se revela como una opción fascinante para agilizar la automatización de la contabilización de facturas, permitiéndo optimizar tiempo y recursos de manera efectiva.

---

## 📑Caso práctico: Extracción de información de facturas
La contabilización de facturas emerge como una de las labores más monótonas para cualquier contable, llegando a absorber hasta un 80% de su jornada laboral en muchas ocasiones.
Con mi constante búsqueda de soluciones para automatizar procesos, he aprovechado mi experiencia en Python para descubrir una librería sumamente valiosa en este ámbito: PyPDF2. Esta herramienta se revela como una opción fascinante para agilizar la automatización de la contabilización de facturas, permitiéndo optimizar tiempo y recursos de manera efectiva.

El caso práctico que voy a explicar se basa en la **extracción de la información de las facturas almacenadas en archivos PDF dentro de una carpeta en nuestro PC, con el objetivo de generar un archivo en formato Excel/CSV compatible con nuestro sistema ERP.**
Esta automatización permitirá realizar una carga masiva de facturas sin la necesidad de contabilizar cada factura de manera individual.

### Explicación de la automatización
Para automatizar este proceso, he creado diferentes facturas ficticias en excel y las he exportado a pdf. Todas estas facturas, las he guardado en una carpeta específica. De esta forma, el script extraerá la información de todos los pdf que estén en esta carpeta.

El módelo de factura es el siguiente:

![Modelo Factura](https://github.com/adriansg1991/ExtractData_PyPDF/blob/main/fra1.png)

Los campos subrallados de la factura son los que voy a extraer. Este proceso lo hará por cada una de las facturas de la carpeta.

---
Como comentaba, el script itera sobre todos los archivos en la carpeta especificada, verifica si son archivos PDF, extrae información que le hemos solicitado y luego concatena todos los DataFrames resultantes en uno solo. Hay que tener en cuenta que estos scripts se deberán de ajustar a las particularidades de cada factura.
Finalmente, después de extraer la información de las facturas, será necesario ajustar el DataFrame al formato necesario para tu ERP.
Este proceso puede llevarse a cabo utilizando la biblioteca Pandas.
En el caso de las facturas de compra, por ejemplo, si deseas incluir el centro de coste, este es el momento de agregar una columna con dicha información.

Después de realizar este ajuste, solo quedaría exportar el DataFrame al formato requerido, siendo común que tu ERP solicite archivos en formato Excel o CSV.
Una vez completado este paso, simplemente tendrías que cargar el archivo en tu ERP para llevar a cabo la carga masiva de facturas.

Código del script: [Extracción de datos en Facturas](https://github.com/adriansg1991/ExtractData_PyPDF/blob/main/ExtractDataFras.py)

En el siguiente vídeo, podrás observar como el script permite extraer la información de los archivos PDF que se encuentran en una carpeta específica.

[![Vista previa del video](https://img.youtube.com/vi/q0--Z0egplE/0.jpg)](https://youtu.be/q0--Z0egplE)
---

### OUTPUT
Como se muestra en la siguiente imagen, la información necesaria de los PDFs ha sido extraída y se han generado las columnas requeridas por nuestro ERP. Por lo tanto, el paso final es exportar este DataFrame a un archivo .csv o Excel y cargar dicho archivo en nuestro ERP.

![Output](https://github.com/adriansg1991/ExtractData_PyPDF/blob/main/Output.png)
```python
# Para exportar el dataframe
final_df.to_excel('output.xlsx', index=False)  # para exportarlo a Excel
final_df.to_csv('output.csv', index=False)  # para exportarlo a .csv
![OutputExcel](https://github.com/adriansg1991/ExtractData_PyPDF/blob/main/OutputExcel.png)
