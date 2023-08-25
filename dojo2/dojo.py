# https://dojopuzzles.com/problems/jokenpo/

def jokenpo(jogador1, jogador2):
    
    lista = ['pedra','papel','tesoura']
    try:
        jogador1 = jogador1.lower()
        jogador2 = jogador2.lower()
    except AttributeError:
        return 'erro'
    if jogador1 in lista and jogador2 in lista :     
        if jogador2 == 'papel' and  jogador1 == 'pedra':
            return 'papel'
        elif jogador2 == 'pedra' and jogador1 == 'papel':
            return 'papel'
        elif jogador1 == 'papel' and jogador2 == 'tesoura': 
            return 'tesoura'
        elif jogador1 == 'tesoura' and jogador2 == 'papel':
            return 'tesoura'  
        elif  jogador1 == 'tesoura' and jogador2 == 'pedra': 
            return 'pedra'
        elif jogador1 == 'pedra' and jogador2 == 'tesoura':
            return 'pedra'
        return 'empate'

    return 'erro'

assert jokenpo('pedra','pedra') == 'empate'
assert jokenpo('papel','papel') == 'empate'
assert jokenpo('tesoura','tesoura') == 'empate'
assert jokenpo('pedra','papel') == 'papel'
assert jokenpo('papel','pedra') == 'papel'
assert jokenpo('papel','tesoura') == 'tesoura'
assert jokenpo('tesoura','papel') == 'tesoura'
assert jokenpo('tesoura','pedra') == 'pedra'
assert jokenpo('pedra','tesoura') == 'pedra'
assert jokenpo('bomba','tesoura') == 'erro'
assert jokenpo('pedra','bomba') == 'erro'
assert jokenpo({},'tesoura') == 'erro'
assert jokenpo('Tesoura','tesoura') == 'empate'