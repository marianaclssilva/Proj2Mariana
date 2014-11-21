def cria_coordenada(l,c):
	'''Funcao cria_coordenada: inteiro x inteiro -> tuplo
	   Recebe os valores da linha e da coluna.
	   Devolve a coordenada respectiva, sob a forma (x,y)'''

	if l < 1 or l > 4 or c < 1 or c > 4:
		raise ValueError('cria_coordenada: argumentos invalidos')
	else:
		cord = (c,l)
		return cord
	
def coordenada_linha():
	'''Funcao coordenada_linha: coordenada -> inteiro 
	   Recebe um elemento do tipo coordenada. 
	   Devolve a linha respetiva.'''
	
	
def coordenada_coluna():
	'''Funcao coordenada_coluna: coordenada -> inteiro 
	   Recebe um elemento do tipo coordenada. 
	   Devolve a coluna respetiva.'''	
		
	
def e_coordenada():
	'''Funcao e_coordenada: universal -> logico
	   Recebe um unico argumento.
	   Devolve True caso esse argumento seja do tipo coordenada e False 
	   em caso contrario.'''	
	
	
def coordenadas_iguais():
	'''Funcao coordenadas_iguais: coordenada x coordenada -> logico 
	   Recebe como argumentos dois elementos do tipo coordenada. 
	   Devolve True caso esses argumentos correspondam a mesma 
	   posicao (l; c) do tabuleiro e False em caso contrario.'''
	
	
def cria_tabuleiro():	
	'''Funcao cria_tabuleiro: {} -> tabuleiro
	   Nao recebe qualquer argumento.
	   Devolve um elemento do tipo tabuleiro de acordo com a representacao
	   interna escolhida.'''
	
def tabuleiro_posicao():
	'''Funcao tabuleiro_posicao: tabuleiro x coordenada -> inteiro
	   Recebe como argumentos um elemento t do tipo tabuleiro e um elemento
           c do tipo coordenada.
	   Devolve um elemento do tipo inteiro, que corresponde ao valor na 
	   posicao do tabuleiro correspondente a coordenada c. Caso a posicao 
	   correspondente a c esteja vazia, devera devolver o valor 0. A funcao
           deve verificar se o segundo argumento e uma coordenada valida, e 
	   gerar um ValueError com a mensagem "tabuleiro_posicao: argumentos
           invalidos" caso nao seja.'''
	
	
def tabuleiro_pontuacao():
	'''Funcao tabuleiro_pontuacao: tabuleiro -> inteiro 
	   Recebe como argumento um elemento t do tipo tabuleiro.
	   Devolve a pontuacao atual para o tabuleiro t.'''
	
	
def tabuleiro_posicoes_vazias():
	'''Funcao tabuleiro_posicoes_vazias: tabuleiro -> lista
	   Recebe como argumento um elemento t do tipo tabuleiro.
	   Devolve uma lista contendo as coordenadas de todas as posicoes 
	   vazias do tabuleiro t.'''
	
	
def tabuleiro_preenche_posicao():
	'''Funcao tabuleiro_preenche_posicao:  -> 
	   '''
	
	
def tabuleiro_actualiza_pontuacao():
	'''Funcao tabuleiro_actualiza_pontuacao:  -> 
		   '''
	
	
def tabuleiro_redu():
	'''Funcao tabuleiro_redu:  -> 
		  '''
	
	
def e_tabuleiro():
	'''Funcao e_tabuleiro:  -> 
		   '''
	
	
def tabuleiro_terminado():
	'''Funcao tabuleiro_terminado:  -> 
		  '''
	
	
def tabuleiros_iguais():
	'''Funcao tabuleiros_iguais: -> 
		  '''
	
	
def escreve_tabuleiro():
	'''Funcao escreve_tabuleiro:  -> 
		 '''
	
	
def pede_jogada():
	'''Funcao pede_jogada: -> 
		'''
	
	
def jogo_2048():
	'''Funcao jogo_2048: -> 
		  '''
