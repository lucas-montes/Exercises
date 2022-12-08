def twoStrings(s1, s2):
    letras_visitadas = []
    for letra in s1:
        if letra in letras_visitadas:
            continue
        if re.search(letra, s2):
            return 'YES'
        letras_visitadas.append(letra)
    return 'NO'