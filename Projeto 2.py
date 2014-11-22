# Grupo 34:
# Bruno Machado - 81930
# Mariana Silva - 81938
# Franscisco Santos - 82009


def cria_coordenada(l,c):
	'''Funcao cria_coordenada: int x int -> tuple
	   Recebe dois argumentos do tipo inteiro, o primeiro corresponde a uma 
	   linha l (inteiro entre 1 e 4) e o segundo a uma coluna c (inteiro 
	   entre 1 e 4). 
           Devolve um elemento do tipo coordenada correspondente a posicao 
	   (l, c). Se os argumentos nao forem validos gera um ValueError.'''

	if 1 <= l <= 4 and 1 <= c <= 4:  
		return (l,c)
	
	else:
		raise ValueError('cria_coordenada: argumentos invalidos')
	
def coordenada_linha(coordenada):
	'''Funcao coordenada_linha: tuple -> int  
	   Recebe um elemento do tipo coordenada. 
	   Devolve a linha respetiva.'''
	
	return (coordenada[0])
	
def coordenada_coluna(coordenada):
	'''Funcao coordenada_coluna: tuple -> int 
	   Recebe um elemento do tipo coordenada. 
	   Devolve a coluna respetiva.'''
	
	return (coordenada[1])
	
def e_coordenada(coord_verif):
	'''Funcao e_coordenada: universal -> bool
	   Recebe um unico argumento.
	   Devolve True caso esse argumento seja do tipo coordenada e False 
	   em caso contrario.'''
	
	return isinstance (coord_verif,tuple) and len(coord_verif) == 2
		
def coordenadas_iguais(coord1,coord2):
	'''Funcao coordenadas_iguais: tuple x tuple -> bool 
	   Recebe como argumentos dois elementos do tipo coordenada. 
	   Devolve True, caso esses argumentos correspondam a mesma 
	   posicao (l, c) do tabuleiro, e False em caso contrario.'''
	
	return coord1[0] == coord2[0] and coord1[1] == coord2[1]
	
def cria_tabuleiro(): #Bruno	
	'''Funcao cria_tabuleiro: {} -> tabuleiro
	   Nao recebe qualquer argumento.
	   Devolve um elemento do tipo tabuleiro de acordo com a representacao
	   interna escolhida.'''
	
def tabuleiro_posicao(): #Bruno
	'''Funcao tabuleiro_posicao: tabuleiro x coordenada -> inteiro
	   Recebe como argumentos um elemento t do tipo tabuleiro e um elemento
           c do tipo coordenada.
	   Devolve um elemento do tipo inteiro, que corresponde ao valor na 
	   posicao do tabuleiro correspondente a coordenada c. Caso a posicao 
	   correspondente a c esteja vazia, devera devolver o valor 0. A funcao
           deve verificar se o segundo argumento e uma coordenada valida, e 
	   gerar um ValueError com a mensagem "tabuleiro_posicao: argumentos
           invalidos" caso nao seja.'''
	
	
def tabuleiro_pontuacao(): #Bruno
	'''Funcao tabuleiro_pontuacao: tabuleiro -> inteiro 
	   Recebe como argumento um elemento t do tipo tabuleiro.
	   Devolve a pontuacao atual para o tabuleiro t.'''
	
	
def tabuleiro_posicoes_vazias(): #Mariana
	'''Funcao tabuleiro_posicoes_vazias: tabuleiro -> lista
	   Recebe como argumento um elemento t do tipo tabuleiro.
	   Devolve uma lista contendo as coordenadas de todas as posicoes 
	   vazias do tabuleiro t.'''
	
	
def tabuleiro_preenche_posicao(): #Mariana
	'''Funcao tabuleiro_preenche_posicao:  -> 
	   '''
	
	
def tabuleiro_actualiza_pontuacao(): #Mariana
	'''Funcao tabuleiro_actualiza_pontuacao:  -> 
		   '''
	
	
def tabuleiro_redu(): #Fransciso
	'''Funcao tabuleiro_redu:  -> 
		  '''
	
	
def e_tabuleiro(): #Mariana
	'''Funcao e_tabuleiro:  -> 
		   '''
	
	
def tabuleiro_terminado(): #Fransciso
	'''Funcao tabuleiro_terminado:  -> 
		  '''
	
	
def tabuleiros_iguais(): #Fransciso
	'''Funcao tabuleiros_iguais: -> 
		  '''
	
	
def escreve_tabuleiro(): #Bruno
	'''Funcao escreve_tabuleiro:  -> 
		 '''
	
	
def pede_jogada():
	'''Funcao pede_jogada: -> 
		'''
	
	
def jogo_2048():
	'''Funcao jogo_2048: -> 
		  '''
