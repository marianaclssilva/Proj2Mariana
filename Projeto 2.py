# Grupo 34:
# Bruno Machado - 81930
# Mariana Silva - 81938
# Franscisco Santos - 82009

# Funcoes TAD coordenada
def cria_coordenada(l,c): # Construtor
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
	
def coordenada_linha(coordenada): # Seletor
	'''Funcao coordenada_linha: tuple -> int  
	   Recebe um elemento do tipo coordenada. 
	   Devolve a linha respetiva.'''
	
	return (coordenada[0])
	
def coordenada_coluna(coordenada): # Seletor
	'''Funcao coordenada_coluna: tuple -> int 
	   Recebe um elemento do tipo coordenada. 
	   Devolve a coluna respetiva.'''
	
	return (coordenada[1])
	
def e_coordenada(coord_verif): # Reconhecedor
	'''Funcao e_coordenada: universal -> bool
	   Recebe um unico argumento.
	   Devolve True caso esse argumento seja do tipo coordenada e False 
	   em caso contrario.'''
	
	return isinstance (coord_verif,tuple) and len(coord_verif) == 2 and \
1 <= coordenada_linha(coord_verif) <= 4 and \
1 <= coordenada_coluna(coord_verif) <= 4

		
def coordenadas_iguais(coord1,coord2): # Teste
	'''Funcao coordenadas_iguais: tuple x tuple -> bool 
	   Recebe como argumentos dois elementos do tipo coordenada. 
	   Devolve True, caso esses argumentos correspondam a mesma 
	   posicao (l, c) do tabuleiro, e False em caso contrario.'''
	
	return coord1[0] == coord2[0] and coord1[1] == coord2[1]

# Funcoes TAD tabuleiro	
def cria_tabuleiro(): #Bruno	
	'''Funcao cria_tabuleiro: {} -> dict
	   Nao recebe qualquer argumento.
	   Devolve um elemento do tipo tabuleiro de acordo com a representacao
	   interna escolhida.'''
	
	# A representacao interna escolhida para um elemento do tipo 'tabuleiro' 
	# foi um dicionario com 17 entradas, que contem as coordenadas e a 
	# pontuacao (incompleto...)
	tabuleiro = {(1,1): 0, (1,2): 0, (1,3): 0, (1,4): 0, (2,1):0, (2,2):0,
	             (2,3): 0, (2,4): 0, (3,1): 0, (3,2): 0, (3,3):0, (3,4):0, 
	             (4,1): 0, (4,2): 0, (4,3): 0, (4,4): 0, 'pontuacao': 0}
	return tabuleiro
		
def tabuleiro_posicao(t,c): #Bruno
	'''Funcao tabuleiro_posicao: dict x tuple -> int
	   Recebe como argumentos um elemento 't' do tipo tabuleiro e um 
	   elemento 'c' do tipo coordenada.
	   Devolve um elemento do tipo inteiro, que corresponde ao valor na 
	   posicao do tabuleiro correspondente a coordenada 'c'. Caso a posicao 
	   correspondente a 'c' esteja vazia, devera devolver o valor 0. Se os 
	   argumentos nao forem validos gera um ValueError.'''
	
	if c == ():
		return 0
	elif e_coordenada(c) == False:
		return ValueError('tabuleiro_posicao: argumentos invalidos')
	else: 
		return t[c]
	
	
def tabuleiro_pontuacao(t): #Bruno
	'''Funcao tabuleiro_pontuacao: dict -> inteiro 
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
	   Devolve a pontuacao atual para o tabuleiro 't'.'''
	return t['pontuacao']
	
	
def tabuleiro_posicoes_vazias(t): #Mariana
	'''Funcao tabuleiro_posicoes_vazias: dict -> list
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
	   Devolve uma lista contendo as coordenadas de todas as posicoes 
	   vazias do tabuleiro 't'.'''
	coordenadas = [(1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4),
	               (3,1), (3,2), (3,3), (3,4), (4,1), (4,2), (4,3), (4,4)]
	coordenada_vazia = []
	for i in coordenadas:
		if t[i] == 0:
			coordenada_vazia += [i, ]
	return coordenada_vazia
			
	
def tabuleiro_preenche_posicao(t,c,v): #Mariana
	'''Funcao tabuleiro_preenche_posicao: dict x tuple x int -> dict
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
	'''Funcao tabuleiro_actualiza_pontuacao: dict x int -> dict
	   Recebe como argumentos um elemento 't' do tipo tabuleiro e um 
	   elemento 'v' do tipo inteiro, nao negativo e multiplo de 4. Modifica
	   o tabuleiro 't', acrescentando ao valor da respectiva pontuacao 'v' 
	   pontos. 
	   Devolve o tabuleiro modificado. Se os argumentos nao forem validos 
	   gera um ValueError. '''
	
	if v > 0 and v % 4 == 0:
		t['pontuacao'] += v
		return t			
			
	else:
		raise ValueError('tabuleiro_actualiza_pontuacao: argumentos\
 invalidos')	
	
# Estamos a considerar a coordenada (0,0) como sendo o ponto mais esquerda e em cima do tabuleiro
def tabuleiro_reduz(t,d): #Fransciso
	'''Funcao tabuleiro_redu: dict x string -> dict 
	   Recebe como argumento um elemento 't' do tipo tabuleiro e uma
           cadeia de caracteres 'd' correspondente a uma de 4 acoes possiveis, 
	   'd' deve ser uma das cadeias de caracteres 'N', 'S', 'W', 'E'. 
	   A funcao modifica o tabuleiro 't', reduzindo-o na direcao 'd' de 
	   acordo com as regras do jogo 2048. 
	   Devolve o tabuleiro 't' modificado, incluindo a atualizacao da
	   pontuacao. Se os argumentos nao forem validos gera um ValueError.'''

	   tecla = {'N': (-1,0), 'S': (1,0), 'W': (0, -1), 'E': (0,1)}
	   cc_direcao = tecla[d]
	   cc_direcao_x = coordenada_linha(cc)
	   cc_direcao_y = coordenada_coluna(cc)
	   for linha in range(4):
	   		for coluna in range(4):
	   			linha_original = linha
	   			coluna_original = coluna
	   			coordenada_original = cria_coordenada(linha, coluna)
	   			valor_original = tabuleiro_posicao(t,coordenada_original)

	   			while True:
	   				coordenada = cria_coordenada(linha,coluna)
	   				if not e_coordenada(coordenada):
	   					linha -= cc_direcao_x
	   					coluna -= cc_direcao_y
	   					coordenada = cria_coordenada(linha,coluna)
	   					tabuleiro_preenche_posicao = (t, coordenada, valor_original)
	   					break


	   				linha += cc_direcao_x
	   				coluna += cc_direcao_y





	
	
def e_tabuleiro(t_verif): #Mariana
	'''Funcao e_tabuleiro: universal -> bool
	   Recebe um unico argumento. 
	   Devolve True se o argumento for do tipo tabuleiro e False em 
	   caso contrario.'''
	
	return isinstance (t_verif,dict) and len(t_verif) == 17  # esta errado
	
def tabuleiro_terminado(t): #Fransciso
	'''Funcao tabuleiro_terminado: dict -> bool
	   Recebe como argumento um elemento 't' do tipo tabuleiro. 
	   Devolve True caso o tabuleiro 't' esteja terminado, ou seja, caso 
	   esteja cheio e nao existam movimentos possiveis, e False em caso 
	   contrario.'''
	
	
def tabuleiros_iguais(t1,t2): #Fransciso
	'''Funcao tabuleiros_iguais: dict x dict -> bool
	   Recebe como argumentos dois elementos 't1' e 't2' do tipo tabuleiro.
	   Devolve True caso 't1' e 't2' correspondam a dois tabuleiros com a 
	   mesma configuracao e pontuacao, e False em caso contrario.'''
	
	
def escreve_tabuleiro(t): #Bruno
	'''Funcao escreve_tabuleiro: dict -> {}
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
