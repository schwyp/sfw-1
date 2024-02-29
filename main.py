import os
import re

class Contador:
    @staticmethod
    def contar_palabra_en_archivo(archivo, palabra):
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                contenido = file.read()
                return len(re.findall(r'\b{}\b'.format(re.escape(palabra)), contenido.lower()))
        except FileNotFoundError:
            return 0

    @staticmethod
    def main():
        ruta_carpeta = input("Ingrese la ruta completa de la carpeta: ")

        if not os.path.exists(ruta_carpeta):
            print("La carpeta indicada no existe.")
            return

        palabra_buscar = input("Ingrese la palabra que desea buscar: ")

        total_palabra = 0

        archivos_texto_encontrados = False

        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith(('.txt', '.xml', '.json', '.csv')):
                archivos_texto_encontrados = True
                ruta_archivo = os.path.join(ruta_carpeta, archivo)
                veces_en_archivo = Contador.contar_palabra_en_archivo(ruta_archivo, palabra_buscar)
                print(f"La palabra '{palabra_buscar}' aparece {veces_en_archivo} veces en el archivo '{archivo}'.")
                total_palabra += veces_en_archivo

        if not archivos_texto_encontrados:
            print("No se encontraron archivos de texto en la carpeta.")

        print(f"\nLa palabra '{palabra_buscar}' aparece un total de {total_palabra} veces en la carpeta '{ruta_carpeta}'.")

if __name__ == "__main__":
    Contador.main()
