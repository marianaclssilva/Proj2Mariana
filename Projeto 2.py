# Grupo 34:
# Bruno Machado - 81930
# Mariana Silva - 81938
# Franscisco Santos - 82009


# Funcoes TAD coordenada

from random import *

def cria_coordenada(l,c): # Construtor     #DONE (rever comentarios)
	'''Funcao cria_coordenada: int x int -> tuple
	   Recebe dois argumentos do tipo inteiro, o primeiro corresponde a uma 
	   linha l (inteiro entre 1 e 4) e o segundo a uma coluna c (inteiro 
	   entre 1 e 4). 
           Devolve um elemento do tipo coordenada correspondente a posicao 
	   (l, c). Se os argumentos nao forem validos gera um ValueError.'''

	if 1 <= l <= 4 and 1 <= c <= 4:  # Definimos os argumentos do tipo 
		return (l,c)		 # coordenada como sendo um tuplo com
	                                 # apenas dois elementos e esses 
			                 # elementos tem de ser >= 1 e <= 4.		
	else:
		raise ValueError('cria_coordenada: argumentos invalidos')
	
	
def coordenada_linha(coordenada): # Seletor    #DONE
	'''Funcao coordenada_linha: tuple -> int  
	   Recebe um elemento do tipo coordenada. 
	   Devolve a linha respetiva.'''
	
	return (coordenada[0])
	
		
def coordenada_coluna(coordenada): # Seletor    #DONE
	'''Funcao coordenada_coluna: tuple -> int 
	   Recebe um elemento do tipo coordenada. 
	   Devolve a coluna respetiva.'''
	
	return (coordenada[1])
	
	
def e_coordenada(coord_verif): # Reconhecedor	#DONE (rever o comentario)
	'''Funcao e_coordenada: universal -> bool
	   Recebe um unico argumento.
	   Devolve True caso esse argumento seja do tipo coordenada e False 
	   em caso contrario.'''
	
	# Para um argumento ser considerado uma coordenada tem de ser um tuplo 
	# com apenas dois elementos (l,c) e esses elementos tem de ser >= 1 
	# e <= 4.
	return isinstance (coord_verif,tuple) and len(coord_verif) == 2 and \
	       1 <= coordenada_linha(coord_verif) <= 4 and \
	       1 <= coordenada_coluna(coord_verif) <= 4


def coordenadas_iguais(coord1,coord2): # Teste    #DONE  
	'''Funcao coordenadas_iguais: tuple x tuple -> bool 
	   Recebe como argumentos dois elementos do tipo coordenada. 
	   Devolve True caso esses argumentos correspondam a mesma 
	   posicao (l, c) do tabuleiro e False em caso contrario.'''
	
	return coord1[0] == coord2[0] and coord1[1] == coord2[1]


# Funcoes TAD tabuleiro	

def cria_tabuleiro(): # Construtor	#DONE (rever o comentario)
	'''Funcao cria_tabuleiro: {} -> dict
	   Nao recebe qualquer argumento.
	   Devolve um elemento do tipo tabuleiro de acordo com a representacao
	   interna escolhida.'''
	
	# A representacao interna escolhida para um elemento do tipo 'tabuleiro' 
	# foi um dicionario com 17 entradas. Em que as 16 primeiras chaves sao 
	# sao coordenada (l,c) e a ultima chave corresponde a pontuacao.
	# O valor de cada chave, incluindo da pontuacao, e 0, pois o tabuleiro 
	# devera vir vazio.
	
	tabuleiro = {(1,1): 0, (1,2): 0, (1,3): 0, (1,4): 0, (2,1):0, (2,2):0,
	             (2,3): 0, (2,4): 0, (3,1): 0, (3,2): 0, (3,3):0, (3,4):0, 
	             (4,1): 0, (4,2): 0, (4,3): 0, (4,4): 0, 'pontuacao': 0}
	
	return tabuleiro
		
def tabuleiro_posicao(t,c): # Seletor	    #Bruno
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
		raise ValueError('tabuleiro_posicao: argumentos invalidos')
	else: 
		return t[c]
	
	
def tabuleiro_pontuacao(t): # Seletor	    #DONE (rever comentario)
	'''Funcao tabuleiro_pontuacao: dict -> inteiro 
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
	   Devolve a pontuacao atual para o tabuleiro 't'.'''
	
	return t['pontuacao'] # Vai devolver a ultima chave do tabuleiro, 
                              # que e a correspondente a pontuacao.
	
	
def tabuleiro_posicoes_vazias(t): # Seletor     #Mariana
	'''Funcao tabuleiro_posicoes_vazias: dict -> list
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
	   Devolve uma lista contendo as coordenadas de todas as posicoes 
	   vazias do tabuleiro 't'.'''
	
	vazio =  []
	for l in range(1,5,1):
		for c in range(1,5,1):
			cc = cria_coordenada(l,c)
			if t[cc] == 0:
				vazio += [cc, ]
	return vazio

	
def tabuleiro_preenche_posicao(t,c,v): # Modificador   #Mariana
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

	
def tabuleiro_actualiza_pontuacao(t,v): # Modificador   #Mariana
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
def tabuleiro_reduz(t,d): # Modificador     #Fransciso
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
	cc_direcao_x = coordenada_linha(cc_direcao)
	cc_direcao_y = coordenada_coluna(cc_direcao)
	for linha in range(1,5,1):
		for coluna in range(1,5,1):
			linha_original = linha
			coluna_original = coluna
			coordenada_original = cria_coordenada(linha_original, coluna_original)
			valor_original = tabuleiro_posicao(t,coordenada_original)
			
			while True:
				coordenada_atual = cria_coordenada(linha, coluna)
				linha += cc_direcao_x
				coluna += cc_direcao_y
				try:
					coordenada = cria_coordenada(linha,coluna)
				except:
					linha = linha_original
					coluna = coluna_original
					break
				if valor_original == 0:
					break
				elif coordenada not in tabuleiro_posicoes_vazias(t):
					valor = tabuleiro_posicao(t, coordenada)
					if valor == valor_original:
						valor += valor
						tabuleiro_preenche_posicao(t, coordenada, valor)
						tabuleiro_actualiza_pontuacao(t,valor)
						tabuleiro_preenche_posicao(t, coordenada_atual, 0)
						break
					else:
						break
				tabuleiro_preenche_posicao(t,coordenada, valor_original)
				tabuleiro_preenche_posicao(t, coordenada_atual, 0)
	for coluna in range(1,5,1):
		for linha in range(1,5,1):
			linha_original = linha
			coluna_original = coluna
			coordenada_original = cria_coordenada(linha_original, coluna_original)
			valor_original = tabuleiro_posicao(t,coordenada_original)
			
			while True:
				coordenada_atual = cria_coordenada(linha, coluna)
				linha += cc_direcao_x
				coluna += cc_direcao_y
				try:
					coordenada = cria_coordenada(linha,coluna)
				except:
					linha = linha_original
					coluna = coluna_original
					break
				if valor_original == 0:
					break
				elif coordenada not in tabuleiro_posicoes_vazias(t):
					valor = tabuleiro_posicao(t, coordenada)
					if valor == valor_original:
						valor += valor
						tabuleiro_preenche_posicao(t, coordenada, valor)
						tabuleiro_actualiza_pontuacao(t,valor)
						tabuleiro_preenche_posicao(t, coordenada_atual, 0)
						break
					else:
						break
				tabuleiro_preenche_posicao(t,coordenada, valor_original)
				tabuleiro_preenche_posicao(t, coordenada_atual, 0)
	return t
	
		
def e_tabuleiro(t_verif): # Reconhecedor     #Mariana
	'''Funcao e_tabuleiro: universal -> bool
	   Recebe um unico argumento. 
	   Devolve True se o argumento for do tipo tabuleiro e False em 
	   caso contrario.'''
	for i in t_verif:
		if i == 'pontuacao':
			return True
		if not e_coordenada(i):
			return False
	return isinstance (t_verif,dict) and len(t_verif) == 17 
	
	
def tabuleiro_terminado(t): # Reconhecedor    # DONE
	'''Funcao tabuleiro_terminado: dict -> bool
	   Recebe como argumento um elemento 't' do tipo tabuleiro. 
	   Devolve True caso o tabuleiro 't' esteja terminado, ou seja, caso 
	   esteja cheio e nao existam movimentos possiveis, e False em caso 
	   contrario.'''
	
	direcao = ['N','S','W','E'] # Direcoes possiveis
	
	for d in direcao:
		# Se ja nao for possivel reduzir o tabuleiro em nenhuma das 
		# direcoes e se ja nao houver nenhuma posicao com o valor 0, 
		# entao o tabuleiro esta completo.
		if not tabuleiro_reduz(t,d) and not tabuleiro_posicoes_vazias(t):
			return True
		return False	
	
	
def tabuleiros_iguais(t1,t2): # Teste    #DONE
	'''Funcao tabuleiros_iguais: dict x dict -> bool
	   Recebe como argumentos dois elementos 't1' e 't2' do tipo tabuleiro.
	   Devolve True caso 't1' e 't2' correspondam a dois tabuleiros com a 
	   mesma configuracao e pontuacao, e False em caso contrario.'''
	
	return t1 == t2
	
	
def escreve_tabuleiro(t): # Transformador de saida     #DONE
	'''Funcao escreve_tabuleiro: dict -> {}
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
           Escreve para o ecra a representacao externa de um tabuleiro de 2048.
	   Se os argumentos nao forem validos gera um ValueError.'''
	
	if e_tabuleiro(t) == True: 
	
		print ('[',t[(1,1)],']','[', t[(1,2)],']','[', t[(1,3)],']',\
		       '[', t[(1,4)] ,'] ')
		print ('[', t[(2,1)],']','[',t[(2,2)],']','[', t[(2,3)],']',\
		       '[', t[(2,4)],'] ')
		print ('[',t[(3,1)],']','[',t[(3,2)],']','[', t[(3,3)], ']',\
		       '[',t[(3,4)],'] ')
		print ('[', t[(4,1)],']','[', t[(4,2)],']','[', t[(4,3)],']',\
		       '[',t[(4,4)],'] ') 
		print ('Pontuacao:', t['pontuacao'])
		
	else:
		raise ValueError('escreve_tabuleiro: argumentos invalidos')	
	
		
def pede_jogada(): # Teste    #DONE
	'''Funcao pede_jogada: {} -> str
	   Nao recebe qualquer argumento. Limita-se a pedir ao utilizador para 
	   introduzir uma direcao (N, S, E ou W), se o valor introduzido for
	   invalido a funcao pede novamente a informacao de jogada ao 
	   utilizador. 
	   Devolve uma cadeia de caracteres correspondente a direcao escolhida 
	   pelo utilizador.'''
	
	jogada = input('Introduza uma jogada (N, S, E, W): ')
	
	if (jogada != 'N') and (jogada != 'S') and (jogada != 'E') and \
	   (jogada != 'W'):
		
		while (jogada != 'N') and (jogada != 'S') and (jogada != 'E') \
		      and (jogada != 'W'):
			
			print('Jogada invalida.')
			jogada = input('Introduza uma jogada (N, S, E, W): ')
	return jogada


def jogo_2048(): # Teste
	'''Funcao jogo_2048: {} -> {} 
	   Nao recebe qualquer argumento e permite ao utilizador jogar um jogo 
	   completo de 2048. Em cada turno, a funcao escreve o tabuleiro no 
	   ecra e pede ao utilizador para introduzir uma nova jogada. 
	   Caso a jogada seja valida, atualiza o tabuleiro e repete este 
	   processo ate o jogo terminar. Caso contrario, escreve para o ecra a 
	   indicacao "Jogada invalida." e solicita uma nova jogada ao 
	   utilizador.'''
	
	t = cria_tabuleiro() # escreve um tabuleiro
	t = preenche_posicao_aleatoria(t) # que ja tem um numero aleatorio
	escreve_tabuleiro(t)
	# enquanto nao se verificar as condicoes da funcao tabuleiro_terminado...
	while tabuleiro_terminado(t) == False:
		jogada = pede_jogada()
		t = tabuleiro_reduz(t,jogada)
		escreve_tabuleiro(t)
		t = preenche_posicao_aleatoria(t)


def preenche_posicao_aleatoria(t):
	'''Funcao preenche_posicao_aleatoria: dict -> dict
	   Recebe um elemento do tipo tabuleiro e preenche uma posicao livre, 
	   escolhida aleatoriamente, com um dos numeros 2 ou 4, de acordo com 
	   as probabilidades.'''	
	
	def gera_2_4():
			numero = random()
			if numero <= 0.8:  # A probabilidade de o numero gerado 
				return 2   # ser 2 e de 0.8.
				
			else:              # A probabilidade de o numero gerado 
				return 4   # ser 4 e de 0.2.
				 
	
	n_default = gera_2_4()	
	# Escolher aleatoriamente uma coordenada que tenha valor 0.
	coord = choice(tabuleiro_posicoes_vazias(t)) 
	# Atribuir o valor 2 ou 4 (gerado aleatoriamente pela funcao gera_2_4) 
	# a coord escolhida, preenchendo a posicao correspondente no tabuleiro.
	res = tabuleiro_preenche_posicao(t,cord,n_default) 
	
	return t 
	

def copia_tabuleiro(t):
	'''Funcao copia_tabuleiro: dict -> dict
	   Recebe como argumento um elemento do tipo tabuleiro.
	   Devolve uma copia do mesmo.'''	
	
	t_copia = dict(t)
	t_copia = cria_tabuleiro()
	return escreve_tabuleiro(t_copia)	


