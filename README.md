# Convertidor de PDF a Audio

[![Python](https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://www.python.org)

Este script de Python convierte un archivo PDF a audio utilizando las bibliotecas `PyPDF2` y `gTTS` (Google Text-to-Speech).

## Funcionalidades

- Lee un archivo PDF y extrae el texto.
- Convierte el texto extraído a audio con una voz similar a la humana en español.
- Guarda el audio en un archivo mp3 en el mismo directorio que el PDF.

## Instalación

Para instalar y ejecutar este proyecto, necesitarás Python 3 y pip instalados en tu máquina. A continuación, puedes clonar este repositorio y instalar las dependencias.

### Clonar este repositorio

```
git clone https://github.com/CodeGeekR/pdf2audio.git
```

### Ir al directorio del repositorio

```
cd pdf2audio
```

### Crear y activar entorno virtual

```
python -m venv venv
```

```
source venv/bin/activate
```

### Instalar las dependencias

```
pip install -r requirements.txt
```

## Cómo ejecutar el script

Para ejecutar este script, puedes usar el siguiente comando:

```
python main.py <ruta_del_pdf>
```

reemplazando `<ruta_del_pdf>` con la ruta del archivo PDF que quieres convertir a audio.

## Contribuir

Si te gusta este proyecto, por favor dale una estrella ⭐ y sígueme para más proyectos interesantes.
