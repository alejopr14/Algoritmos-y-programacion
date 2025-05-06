Diccionario = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,
'Maite': 5}

valor_sin = []

for valor in Diccionario.values():
    if valor not in valor_sin:
        valor_sin.append(valor)

print(valor_sin)