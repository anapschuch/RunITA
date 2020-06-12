inimigo_esperto = [(95, 140)]
player = (33, 80)
end_phase = (585, 490)
inimigo_aleatorio = [(332, 196), (500, 190), (770, 350), (1000, 160), (1000, 520), (100, 845), (515, 655)]
bullets = [(310, 380), (30, 845), (890, 585), (680, 265), (325, 205), (660, 815), (945, 30)]
Fase1 = {
    'phase': 1,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets
}

Fase2 = {
    'phase': 2,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets
}

dados = [Fase1, Fase2]
arquivo = open('dados.txt', 'w')
arquivo.write(str(dados))
arquivo.close()
