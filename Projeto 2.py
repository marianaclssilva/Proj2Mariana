# Grupo 34:
# Bruno Machado - 81930
# Mariana Silva - 81938
# Franscisco Santos - 82009

# TAD coordenada
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

# TAD tabuleiro	
def cria_tabuleiro(): #Bruno	
	'''Funcao cria_tabuleiro: {} -> tabuleiro
	   Nao recebe qualquer argumento.
	   Devolve um elemento do tipo tabuleiro de acordo com a representacao
	   interna escolhida.'''
	tabuleiro = {(1,1): 0, (1,2): 0, (1,3): 0, (1,4): 0, (2,1):0, (2,2):0,
	             (2,3): 0, (2,4): 0, (3,1): 0, (3,2): 0, (3,3):0, (3,4):0, 
	             (4,1): 0, (4,2): 0, (4,3): 0, (4,4): 0, 'pontuacao': 0}
	return tabuleiro
		
def tabuleiro_posicao(t,c): #Bruno
	'''Funcao tabuleiro_posicao: tabuleiro x coordenada -> inteiro
	   Recebe como argumentos um elemento t do tipo tabuleiro e um elemento
           c do tipo coordenada.
	   Devolve um elemento do tipo inteiro, que corresponde ao valor na 
	   posicao do tabuleiro correspondente a coordenada c. Caso a posicao 
	   correspondente a c esteja vazia, devera devolver o valor 0. A funcao
           deve verificar se o segundo argumento e' uma coordenada valida, e 
	   gerar um ValueError com a mensagem "tabuleiro_posicao: argumentos
           invalidos" caso nao seja.'''
	if c == ():
		return 0
	elif e_coordenada(c) == False:
		return ValueError('tabuleiro_posicao: argumentos invalidos')
	else: 
		return t[c]
	
	
def tabuleiro_pontuacao(t): #Bruno
	'''Funcao tabuleiro_pontuacao: tabuleiro -> inteiro 
	   Recebe como argumento um elemento t do tipo tabuleiro.
	   Devolve a pontuacao atual para o tabuleiro t.'''
	return t['pontuacao']
	
	
def tabuleiro_posicoes_vazias(t): #Mariana
	'''Funcao tabuleiro_posicoes_vazias: tabuleiro -> list
	   Recebe como argumento um elemento t do tipo tabuleiro.
	   Devolve uma lista contendo as coordenadas de todas as posicoes 
	   vazias do tabuleiro t.'''
	
	
def tabuleiro_preenche_posicao(t,c,v): #Mariana
	'''Funcao tabuleiro_preenche_posicao: tabuleiro x tuple x int -> tabuleiro
	   Recebe como argumentos um elemento 't' do tipo tabuleiro, um elemento 
	   'c' do tipo coordenada e um elemento 'v' do tipo inteiro e modifica 
	   o tabuleiro 't' colocando o valor 'v' na posicao correspondente a 
	   coordenada 'c'. 
	   Devolve o tabuleiro modificado. Se os argumentos nao forem validos 
	   gera um ValueError.'''
	
	if e_coordenada(c) == True and isinstance (v,int):
		t[c] = v	
		return t
			
	else:
		raise ValueError('tabuleiro_preenche_posicao: argumentos\
 invalidos')	

	
def tabuleiro_actualiza_pontuacao(t,v): #Mariana
	'''Funcao tabuleiro_actualiza_pontuacao: tabuleiro x int -> tabuleiro
	   Recebe como argumentos um elemento 't' do tipo tabuleiro e um 
	   elemento 'v' do tipo inteiro, nao negativo e multiplo de 4. Modifica
	   o tabuleiro 't', acrescentando ao valor da respectiva pontuacao 'v' 
	   pontos. 
	   Devolve o tabuleiro modificado. Se os argumentos nao forem validos 
	   gera um ValueError. '''
	
	if v > 0 and v % 4 == 0:
		return # (incompleto)
			
			
	else:
		raise ValueError('tabuleiro_actualiza_pontuacao: argumentos\
 invalidos')	
	
	
def tabuleiro_reduz(t,d): #Fransciso
	'''Funcao tabuleiro_redu: tabuleiro x string -> tabuleiro 
	   Recebe como argumento um elemento 't' do tipo tabuleiro e uma
           cadeia de caracteres 'd' correspondente a uma de 4 acoes possiveis. 
	   Em particular, 'd' devera ser uma das cadeias de caracteres 'N', 'S', 
	   'W', 'E'. A funcao deve modificar o tabuleiro 't', reduzindo-o 
	   na direcao 'd' de acordo com as regras do jogo 2048. 
	   Devolve o tabuleiro 't' modificado, incluindo a atualizacao da
	   pontuacao. Se os argumentos nao forem validos gera um ValueError.'''
	
	
def e_tabuleiro(): #Mariana
	'''Funcao e_tabuleiro: universal -> bool
	   Recebe um unico argumento. 
	   Devolve True se o argumento for do tipo tabuleiro e False em 
	   caso contrario.'''
	
	return # (incompleto)
	
def tabuleiro_terminado(t): #Fransciso
	'''Funcao tabuleiro_terminado: tabuleiro  ->  bool
	   Recebe como argumento um elemento 't' do tipo tabuleiro. 
	   Devolve True caso o tabuleiro 't' esteja terminado, ou seja, caso 
	   esteja cheio e nao existam movimentos possiveis, e False em caso 
	   contrario.'''
	
	
def tabuleiros_iguais(t1,t2): #Fransciso
	'''Funcao tabuleiros_iguais: tabuleiro x tabuleiro -> bool
	   Recebe como argumentos dois elementos 't1' e 't2' do tipo tabuleiro.
	   Devolve True caso 't1' e 't2' correspondam a dois tabuleiros com a 
	   mesma configuracao e pontuacao e False em caso contrario.'''
	
	
def escreve_tabuleiro(t): #Bruno
	'''Funcao escreve_tabuleiro: tabuleiro -> {}
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
           Escreve para o ecra a representacao externa de um tabuleiro de 2048.
	   Se os argumentos nao forem validos gera um ValueError.'''
	
	print ( '','[',t[(1,1)],']','[', t[(1,2)],']','[', t[(1,3)],']','[', t[(1,4)] ,']','\n',
	        '[', t[(2,1)],']','[',t[(2,2)],']','[', t[(2,3)],']','[', t[(2,4)],']','\n',
	        '[',t[(3,1)],']','[',t[(3,2)],']','[', t[(3,3)], ']','[',t[(3,4)],']', '\n',
	        '[', t[(4,1)],']','[', t[(4,2)],']','[', t[(4,3)],']', '[',t[(4,4)],']', '\n', 
	        'pontuacao:', t['pontuacao'])
		
def pede_jogada():
	'''Funcao pede_jogada: -> 
		'''
	
	
def jogo_2048():
	'''Funcao jogo_2048: -> 
		  '''
