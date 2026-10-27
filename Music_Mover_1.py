from pathlib import Path
import shutil

origen = Path.home() / "TEST" / "TEST"
music = Path.home() / "TEST" / "TEST"

SIMULAR = False
contador = 0

for archivo in list(origen.rglob("*.mp3")):
    Destino = music / archivo.name

    if Destino.exists():
        print("YA EXISTE, no se mueve:", archivo.name)
        continue

    if SIMULAR:
        print("[SIMULATION]", archivo.name)
        print("[SIMULATION] Borraria la carpeta:", Destino.name)
    else:
        music.mkdir(parents=True, exist_ok=True)
        shutil.move(archivo, Destino)
        print("Movido:", archivo.name)
        

    contador = contador + 1

print()
print("Total de canciones movidas:", contador)

print()
print("----- Cleaning JDownloader-----")

for elemento in list(origen.iterdir()):
    if elemento.name.startswith("."):
        continue
    if elemento.is_dir():
        pendientes = list(elemento.rglob("*.mp3")) + list(elemento.rglob("*.part"))
        if len(pendientes) > 0:
            print("Se deja, todavia tiene cancion o descarga en curso:", elemento.name)
            continue
        if SIMULAR:
            print("[SIMULATION] Borraria la carpeta:", elemento.name)
        else:
            shutil.rmtree(elemento)
            print("Carpeta borrada:", elemento.name)

    elif elemento.suffix.lower() not in [".mp3", ".part"]:
        if SIMULAR:
            print("[SIMULATION] Borraria el archivo:", elemento.name)
        else:
            elemento.unlink()
            print("Archivo borrado:",elemento.name)
 
