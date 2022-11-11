def shuffle_musicas(musicas_tocadas: list) -> list:
    musicas_tocadas.sort()
    nova_lista = []

    while True:
        try:
            elemento = musicas_tocadas.pop()
            nova_lista.append(elemento)
            elemento = musicas_tocadas.pop(0)
            nova_lista.append(elemento)
        except IndexError:
            return nova_lista
