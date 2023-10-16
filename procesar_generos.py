#!/usr/bin/env python
import cgi

# Obtener el género seleccionado del formulario
form = cgi.FieldStorage()
genero = form.getvalue("genero")

# Lista de artistas por género
artistas_por_genero = {
    "rock": ["Artista de Rock 1", "Artista de Rock 2"],
    "pop": ["Artista de Pop 1", "Artista de Pop 2"],
    # Agrega más géneros y artistas aquí
}

# Imprimir la lista de artistas del género seleccionado
if genero in artistas_por_genero:
    artistas = artistas_por_genero[genero]
    for artista in artistas:
        print(artista)
else:
    print("No se encontraron artistas para este género.")
