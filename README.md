Este proyecto implementa un sistema para crear archivos en diferentes formatos usando Programación Orientada a Objetos (POO) con herencia y polimorfismo.

El programa genera una carpeta principal Documents y dentro de ella las subcarpetas:

Word → archivos .docx con python-docx

Text → archivos .txt con Python nativo

PDF → archivos .pdf con reportlab

Excel → archivos .xlsx con openpyxl

Cada tipo de archivo es creado por una subclase que implementa el método create_file, mostrando el uso práctico de la herencia y el polimorfismo.

🚀 Ejecución

Instalar dependencias:

pip install python-docx reportlab openpyxl

Ejecutar el programa principal:

python main.py

Se generarán los archivos de prueba en la estructura de carpetas automáticamente.

👨‍💻 Integrantes

Miguel Angel Diaz (aka Accelerati0n )

William Vargas (aka wmvargas-cell )

📋 Revisión

El código fue revisado por el profesor de POO:

Juan Miguel Vargas Cortez (aka juanvarco95 )
