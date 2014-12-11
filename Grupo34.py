# Grupo 34:
# Bruno Machado - 81930
# Mariana Silva - 81938
# Franscisco Santos - 82009

from random import *

direcao = ('N','S','E','W')

# Funcoes TAD coordenada

def cria_coordenada(l,c): # Construtor
	'''Funcao cria_coordenada: int x int -> tuple
	   Recebe dois argumentos do tipo inteiro, o primeiro corresponde a uma 
	   linha l (inteiro entre 1 e 4) e o segundo a uma coluna c (inteiro 
	   entre 1 e 4). 
           Devolve um elemento do tipo coordenada correspondente a posicao 
	   (l, c). Se os argumentos nao forem validos gera um ValueError.'''
	
	# Definimos os argumentos do tipo coordenada como sendo um tuplo com 
	# apenas dois elementos e esses elementos tem de ser numeros inteiros
	# maiores ou iguais a 1 e menores ou iguais a 4.	

	if isinstance(l,int) and isinstance(c,int) and 1 <= l <= 4 and\
	   1 <= c <= 4:   
		return (l,c)	# Verificar se l e c sao numeros inteiros e
				# se sao >= 1 e <= 4.
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
	
	# Para um argumento ser considerado uma coordenada tem de ser um tuplo 
	# com dois elementos (l,c) e esses elementos tem de ser numeros inteiros
	# maiores ou iguais a 1 e menores ou iguais a 4.
	return isinstance (coord_verif,tuple) and len(coord_verif) == 2 and \
	       isinstance(coord_verif[0],int) and \
	       isinstance(coord_verif[1],int) and \
	       1 <= coord_verif[0] <= 4 and \
	       1 <= coord_verif[1] <= 4


def coordenadas_iguais(coord1,coord2): # Teste  
	'''Funcao coordenadas_iguais: tuple x tuple -> bool 
	   Recebe como argumentos dois elementos do tipo coordenada. 
	   Devolve True caso esses argumentos correspondam a mesma 
	   posicao (l, c) do tabuleiro e False em caso contrario.'''
	
	return coordenada_linha(coord1) == coordenada_linha(coord2)\
	 and coordenada_coluna(coord1) == coordenada_coluna(coord2)


# Funcoes TAD tabuleiro	

def cria_tabuleiro(): # Construtor
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
		
		
def tabuleiro_posicao(t,c): # Seletor
	'''Funcao tabuleiro_posicao: dict x tuple -> int
	   Recebe como argumentos um elemento 't' do tipo tabuleiro e um 
	   elemento 'c' do tipo coordenada.
	   Devolve um elemento do tipo inteiro, que corresponde ao valor na 
	   posicao do tabuleiro correspondente a coordenada 'c'. Caso a posicao 
	   correspondente a 'c' esteja vazia, devera devolver o valor 0. Se os 
	   argumentos nao forem validos gera um ValueError.'''
	
	if e_coordenada(c) == False:# Verificar se 'c' e uma coordenada valida.
		raise ValueError('tabuleiro_posicao: argumentos invalidos')
	# Se 'c' for uma coordenada valida vai devolver o valor da posicao do 
	# tabuleiro correspondente a coordenada 'c'.	
	else: 
		return t[(coordenada_linha(c),coordenada_coluna(c))]
	
	
def tabuleiro_pontuacao(t): # Seletor	
	'''Funcao tabuleiro_pontuacao: dict -> inteiro 
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
	   Devolve a pontuacao atual para o tabuleiro 't'.'''
	
	return t['pontuacao'] # Vai devolver a ultima chave do tabuleiro, 
			      # que e a correspondente a pontuacao.
	
	
def tabuleiro_posicoes_vazias(t): # Seletor
	'''Funcao tabuleiro_posicoes_vazias: dict -> list
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
	   Devolve uma lista contendo as coordenadas de todas as posicoes 
	   vazias do tabuleiro 't'.'''
	
	vazio =  []
	for l in range(1,5):
		for c in range(1,5):
			cc = cria_coordenada(l,c)
			# Se o valor da posicao do tabuleiro correspondente a 
			# coordenada cc for 0 devolve uma lista contendo
			# as coordenadas de todas as posicoes vazias do
			# tabuleiro 't'.			
			if tabuleiro_posicao(t,cc) == 0:
				vazio += [cc]
	return vazio

	
def tabuleiro_preenche_posicao(t,c,v): # Modificador 
	'''Funcao tabuleiro_preenche_posicao: dict x tuple x int -> dict
	   Recebe como argumentos um elemento 't' do tipo tabuleiro, um elemento 
	   'c' do tipo coordenada e um elemento 'v' do tipo inteiro e modifica 
	   o tabuleiro 't' colocando o valor 'v' na posicao correspondente a 
	   coordenada 'c'. 
	   Devolve o tabuleiro modificado. Se os argumentos nao forem validos 
	   gera um ValueError.'''
	
	if e_coordenada(c) and isinstance (v,int):
		# Verificar se 'c' coordenada e se 'v' numero inteiro.
		# Atribuir o valor de 'v' a posicao do tabuleiro correspondente 
		# a coordenada 'c'.
		t[(coordenada_linha(c),coordenada_coluna(c))] = v
		return t	
	
	raise ValueError('tabuleiro_preenche_posicao: argumentos\
 invalidos')	

	
def tabuleiro_actualiza_pontuacao(t,v): # Modificador  
	'''Funcao tabuleiro_actualiza_pontuacao: dict x int -> dict
	   Recebe como argumentos um elemento 't' do tipo tabuleiro e um 
	   elemento 'v' do tipo inteiro, nao negativo e multiplo de 4. Modifica
	   o tabuleiro 't', acrescentando ao valor da respectiva pontuacao 'v' 
	   pontos. 
	   Devolve o tabuleiro modificado. Se os argumentos nao forem validos 
	   gera um ValueError. '''
	
	if isinstance(v,int) and v >= 0 and v % 4 == 0:
		t['pontuacao'] = tabuleiro_pontuacao(t) + v
		return t			
			
	else:
		raise ValueError('tabuleiro_actualiza_pontuacao: argumentos\
 invalidos')	
	
	
def tabuleiro_reduz(t,d): # Modificador 
	'''Funcao tabuleiro_reduz: dict x string -> dict 
	   Recebe como argumento um elemento 't' do tipo tabuleiro e uma
           cadeia de caracteres 'd' correspondente a uma de 4 acoes possiveis, 
	   'd' deve ser uma das cadeias de caracteres 'N', 'S', 'W', 'E'. 
	   A funcao modifica o tabuleiro 't', reduzindo-o na direcao 'd' de 
	   acordo com as regras do jogo 2048. 
	   Devolve o tabuleiro 't' modificado, incluindo a atualizacao da
	   pontuacao. Se os argumentos nao forem validos gera um ValueError.'''

	tecla = {'N': [(-1,0), (4,0,-1), [(1,5,1),(1,5,1)]],\
	         'S': [(1,0),(1,5,1),[(4,0,-1),(4,0,-1)]],\
	         'W': [(0, -1),(4,0,-1),[(4,0,-1),(1,5,1)]],\
	         'E': [(0,1),(1,5,1),[(1,5,1),(4,0,-1)]]}
	
	dCC = tecla[d][0]	
	dL = dCC[0]		# Valor x da direcao
	dC = dCC[1]		# Valor y da coluna
	
	cFOR = tecla[d][1]	# Valores do loop da funcao junta_tabuleiro
	a1 = cFOR[0]		# Valor a que comeca a contar
	a2 = cFOR[1]		# Valor a que acaba a contar
	a3 = cFOR[2]		# Cresce de um em um ou decresce de um em um
	
	cFOR2 = tecla[d][2]	# Valores do loop da funcao soma_valores
	l1 = cFOR2[0][0]	# Valor que comeca a contar das linhas
	l2 = cFOR2[0][1]	# Valor que acaba das linhas
	l3 = cFOR2[0][2]	# Cresce de um em um ou decresce de um em um
	
	c1 = cFOR2[1][0]	# Valor que comeca a contar das colunas
	c2 = cFOR2[1][1]	# Valor que acaba das colunas
	c3 = cFOR2[1][2]	# Cresce de um em um ou decresce de um em um
	

	def junta_tabuleiro(t, dL, dC):
		for l in range(a1,a2,a3):               # linhas  
			for c in range(a1,a2,a3):       # colunas
				a = cria_coordenada(l,c)   #posicao antiga
				aV = tabuleiro_posicao(t,a)#valor da pos antiga
				nL = l + dL                #nova linha(comparar)	
				nC = c + dC		  #nova coluna(comparar)
				try:
					b = cria_coordenada(nL,nC) #posicao nova
				except:
					# Se ultrepassar os limites do tabuleiro
					# passa para a proxima linha
					break 
				bV = tabuleiro_posicao(t,b) #valor da pos nova
				
				#se o valor antigo comparado com mais recente
				#nao for zero enquanto que o outro for zero
				#troca os valores e junta todos os que nao forem
				#zero
				if aV != 0 and bV== 0:
					tabuleiro_preenche_posicao(t,a,bV)
					tabuleiro_preenche_posicao(t,b,aV)
					a = b
					
					
		return t
		
	def soma_valores(t,dL,dC):
		for l in range(l1,l2,l3):                   # linhas
			for c in range(c1,c2,c3):           # colunas
				a = cria_coordenada(l,c)    #posicao antiga
				aV = tabuleiro_posicao(t,a) #valor da pos antiga
				nL = l - dL                 #nova linha	 
				nC = c - dC                 #nova coluna
				try:
					b = cria_coordenada(nL,nC) #posicao nova
				except:
					break
				bV = tabuleiro_posicao(t,b) #valor da pos nova
				
				#Se o valor antigo com o recente forem iguais 
				#soma-os e poe na posicao antiga o valor somado 
				# e no recente poe a zero
				if aV == bV and aV > 0:
					aV += bV
					tabuleiro_preenche_posicao(t,a,aV)
					tabuleiro_preenche_posicao(t,b,0)
					tabuleiro_actualiza_pontuacao(t,aV)
					
		return t
	
	
	for i in range(4):
		junta_tabuleiro(t,dL,dC)
	soma_valores(t,dL,dC)
	for i in range(4):
		junta_tabuleiro(t,dL,dC)
	return t
	
		
def e_tabuleiro(t_verif): # Reconhecedor    
	'''Funcao e_tabuleiro: universal -> bool
	   Recebe um unico argumento. 
	   Devolve True se o argumento for do tipo tabuleiro e False em 
	   caso contrario.'''
	if isinstance (t_verif,dict) and len(t_verif) == 17:
		for i in t_verif:
			if isinstance(i,tuple):
				if not isinstance(i[0],int) or not\
				   isinstance(i[1], int) or not \
				   isinstance(t_verif[i],int):
					return False
			elif isinstance(i,str):
				if i != 'pontuacao' or not\
				   isinstance(t_verif[i],int):
					return False
			else:
				return False
		return True
	return False

	
def tabuleiro_terminado(t): # Reconhecedor
	'''Funcao tabuleiro_terminado: dict -> bool
	   Recebe como argumento um elemento 't' do tipo tabuleiro. 
	   Devolve True caso o tabuleiro 't' esteja terminado, ou seja, caso 
	   esteja cheio e nao existam movimentos possiveis, e False em caso 
	   contrario.'''

	if tabuleiro_posicoes_vazias(t) == []:
		t2 = copia_tabuleiro(t)
	
		for d in direcao:
			# Se ja nao for possivel reduzir o tabuleiro em nenhuma  
			# das direcoes e se ja nao houver nenhuma posicao com o  
			# valor 0, entao o tabuleiro esta completo.
			if  not tabuleiros_iguais(tabuleiro_reduz(t2,d), t) :
				return False
		
		return True	
	return False
	
	
def tabuleiros_iguais(t1,t2): # Teste
	'''Funcao tabuleiros_iguais: dict x dict ->lif isinstance(i,str):
				if i != 'pontuacao' bool
	   Recebe como argumentos dois elementos 't1' e 't2' do tipo tabuleiro.
	   Devolve True caso 't1' e 't2' correspondam a dois tabuleiros com a 
	   mesma configuracao e pontuacao, e False em caso contrario.'''
	
	if tabuleiro_pontuacao(t1) != tabuleiro_pontuacao(t2):
		return False
	for i in range(1,5):
		for j in range(1,5):
			cc = cria_coordenada(i,j)
			if tabuleiro_posicao(t1,cc) != tabuleiro_posicao(t2,cc):
				return False
					
	return True	
	
	
def escreve_tabuleiro(t): # Transformador de saida
	'''Funcao escreve_tabuleiro: dict -> {}
	   Recebe como argumento um elemento 't' do tipo tabuleiro.
           Escreve para o ecra a representacao externa de um tabuleiro de 2048.
	   Se os argumentos nao forem validos gera um ValueError.'''
	
	if e_tabuleiro(t): # Verificar se 't' e do tipo tabuleiro.
		
		for i in range(1,5):
			for j in range(1,5):
				cc = cria_coordenada(i,j)
				print('[',tabuleiro_posicao(t,cc),']',end =' ')
			print('')

		print ('Pontuacao:', tabuleiro_pontuacao(t))

		
	else:
		raise ValueError('escreve_tabuleiro: argumentos invalidos')	
	
		
def pede_jogada(): # Teste
	'''Funcao pede_jogada: {} -> str
	   Nao recebe qualquer argumento. Limita-se a pedir ao utilizador para 
	   introduzir uma direcao (N, S, E ou W), se o valor introduzido for
	   invalido a funcao pede novamente a informacao de jogada ao 
	   utilizador. 
	   Devolve uma cadeia de caracteres correspondente a direcao escolhida 
	   pelo utilizador.'''
	
	jogada = str(input('Introduza uma jogada (N, S, E, W): '))
	
	while jogada not in direcao:
			
		print('Jogada invalida.')
		jogada = str(input('Introduza uma jogada (N, S, E, W): '))

	return jogada


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
	vazio = tabuleiro_posicoes_vazias(t)
	if vazio != []:
		coord = choice(vazio) 
	# Atribuir o valor 2 ou 4 (gerado aleatoriamente pela funcao gera_2_4) 
	# a coord escolhida, preenchendo a posicao correspondente no tabuleiro.
		t = tabuleiro_preenche_posicao(t,coord,n_default) 
	
	return t 


def copia_tabuleiro(t):
	'''Funcao copia_tabuleiro: dict -> dict
	Recebe um elemento do tipo tabuleiro e copia cada valor de elemento 
	do tabuleiro para um tabuleiro novo''' 
	
	t2 = cria_tabuleiro()
	tabuleiro_actualiza_pontuacao(t2,tabuleiro_pontuacao(t))
	for i in range(1,5):
		for j in range(1,5):
			cc = cria_coordenada(i,j)
			tabuleiro_preenche_posicao(t2, cc,\
			                           tabuleiro_posicao(t,cc))
	return t2


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
	t = preenche_posicao_aleatoria(t)
	t = preenche_posicao_aleatoria(t) # que ja tem um numero aleatorio
	# enquanto nao se verificar as condicoes da funcao tabuleiro_terminado..
	while not tabuleiro_terminado(t):
		escreve_tabuleiro(t)
		jogada = pede_jogada()
		t2 = copia_tabuleiro(t)
		t = tabuleiro_reduz(t,jogada)
		while tabuleiros_iguais(t,t2):
			escreve_tabuleiro(t)
			jogada = pede_jogada()
			t = tabuleiro_reduz(t,jogada)
		t = preenche_posicao_aleatoria(t)
	return
	



