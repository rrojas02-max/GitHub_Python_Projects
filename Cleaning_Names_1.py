from pathlib import Path

Music = Path.home() / "TEST" / "TEST"

SIMULATION = True   
Contador = 0

Remove = ["(Official Video)","(Video Oficial)","(Official Video)", "(Official Music Video)", "(Official Audio)","(128kbit_AAC-Spanish)", "(Audio)", "(Video)", "(Lyric Video)","(LYRIC VIDEO)", "(Lyrics)", "(Lyric)", "(HD)", "(HQ)", "(4K)", "(1080p)", "(720p)", "(Visual Art)", "(128kbit_AAC)", "(152kbit_Opus)", "(320kbps)", "(128kbps)", "(256kbps)", "(FLAC)", "(MP3)", "(WAV)", "(AAC)", "(ALAC)", "(OGG)", "(M4A)", "(AIFF)", "(WMA)", "(APE)", "(DSD)", "(PCM)", "(VBR)", "(CBR)", "(Lossless)", "(Lossy)"
          ]


for archivo in list(Music.rglob("*")):
    if not archivo.is_file() or archivo.suffix.lower() != ".m4a":
        continue

    nombre = archivo.stem
    for texto in Remove:
        nombre = nombre.replace(texto, "")
    nombre = " ".join(nombre.split())

    if nombre == "" or nombre == archivo.stem:
        continue

    nueva_ruta= archivo.with_name(nombre + archivo.suffix)

    if nueva_ruta.exists():
        print("YA EXISTE:, no se renombra:", archivo.name)
        continue
    if SIMULATION:
        print("SIMULACION", archivo.name, "->", nueva_ruta.name)
    else:
        archivo.rename(nueva_ruta)
        print("Renombrado", archivo.name, "->", nueva_ruta.name)
        Contador += 1

print ()
print ("Canciones a renombrar: ", Contador)


