inimigo_esperto = [(95, 815)]
player = (65, 35)
end_phase = (810, 25)
inimigo_aleatorio = [(155, 245), (35, 455), (815, 515), (515, 785), (755, 35), (395, 65)]
bullets = [(300, 840), (330, 690), (60, 900), (300, 360), (300, 150), (60, 150), (300, 60), (810, 210), (720, 510), (780, 660), (480, 330)]

Fase1 = {
    'phase': 1,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets
}

inimigo_esperto = [(332, 196)]
player = (33, 80)
end_phase = (585, 490)
inimigo_aleatorio = [(95, 140), (500, 190), (770, 350), (1000, 160), (1000, 520), (100, 845), (515, 655)]
bullets = [(310, 380), (30, 845), (890, 585), (680, 265), (325, 205), (660, 815), (945, 30)]

Fase2 = {
    'phase': 2,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets
}

inimigo_esperto = [(155, 365)]
player = (65, 65)
end_phase = (85, 1345)
inimigo_aleatorio = [(65, 665), (605, 455), (695, 95), (1115, 215), (1385, 515), (425, 665), (335, 995), (275, 1325), (785, 1385), (1085, 1055)]
bullets = [(750, 95), (1080, 215), (1380, 485), (480, 665), (150, 365), (60, 665), (270, 995), (270, 1175), (900, 1205), (930, 875), (1380,695), (660, 455)]

Fase3 = {
    'phase': 3,
    'player': player,
    'end_phase': end_phase,
    'inimigo_esperto': inimigo_esperto,
    'inimigo_aleatorio': inimigo_aleatorio,
    'bullets': bullets
}

dados = [Fase1, Fase2, Fase3]
arquivo = open('dados.txt', 'w')
arquivo.write(str(dados))
arquivo.close()
