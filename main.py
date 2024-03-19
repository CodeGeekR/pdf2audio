import os
import sys
import PyPDF2
from gtts import gTTS

def convert_pdf_to_audio(pdf_path):
    # Abre el archivo PDF en modo lectura binaria
    pdf_file = open(pdf_path, 'rb')

    # Crea un objeto PDFFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Inicializa una cadena vacía para almacenar el texto
    text = ''

    # Recorre todas las páginas del PDF y extrae el texto
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    # Cierra el archivo PDF
    pdf_file.close()

    # Crea un objeto gTTS con el texto extraído y el idioma español
    tts = gTTS(text=text, lang='es')

    # Guarda el audio en un archivo mp3
    audio_path = os.path.splitext(pdf_path)[0] + '.mp3'
    tts.save(audio_path)

    print(f'Audio guardado en: {audio_path}')

if __name__ == "__main__":
    # Comprueba si se proporcionó un argumento de línea de comandos
    if len(sys.argv) != 2:
        print('Uso: python3 script.py <ruta_del_pdf>')
        sys.exit(1)

    # Convierte el PDF a audio
    convert_pdf_to_audio(sys.argv[1])