import random
tabuleiro = [
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
navio_humano = '█'
navio_enemigo = '#'
tiro = 'X'
acertos_humano = 0
acertos_enemigo = 0

def mostrar_tabuleiro():
  print('Tabuleiro: ')
  for linha in range(0, 10):
    for coluna in range(0, 10):
      if existe_navio_humano(linha, coluna):
        print(navio_humano*2, end='')      
      else:
        print(tabuleiro[linha][coluna]*2, end='')
    print()

def existe_navio_humano(linha, coluna): 
  if linha==y1h and coluna == x1h or linha==y2h and coluna == x2h or linha==y3h and coluna == x3h:
    return True  
  else:
    return False

x1h = y1h = x2h = y2h = x3h = y3h = 0
x1e = y1e = x2e = y2e = x3e = y3e = 0
fim_jogo = False

def gera_coordenada():
  return random.randrange(9)

def ler_coordenada(coordenada):
  return int(input(f'Digite a coordenada {coordenada} (de 0 a 9): '))

def validar_beiradas(x1, y1, x2, y2, x3, y3):
  if validar_beirada(x1, y1) and validar_beirada(x2, y2) and validar_beirada(x3, y3):
    return True
  else:
    return False

def validar_beirada(x, y):
  if x>8 or x<0:
    return False
  if y>8 or y<0:
    return False
  return True

def validar_sequencia(x1, y1, x2, y2, x3, y3):
  if x1+1==x2 and x1+2==x3 and y1==y2 and y1==y3:
    return True
  if y1+1==y2 and y1+2==y3 and x1==x2 and x1==x3:
    return True
  if x1-1==x2 and x1-2==x3 and y1==y2 and y1==y3:
    return True
  if y1-1==y2 and y1-2==y3 and x1==x2 and x1==x3:
    return True  
  return False

def validar_coordenadas(x1, y1, x2, y2, x3, y3):    
  if validar_sequencia(x1, y1, x2, y2, x3, y3) and validar_beiradas(x1, y1, x2, y2, x3, y3):
    return True
  else:
    return False

def ler_coordenadas():
  global x1h, y1h, x2h, y2h, x3h, y3h  
  x1h = ler_coordenada('primeiro x')
  y1h = ler_coordenada('primeiro y')
  x2h = ler_coordenada('segundo x')
  y2h = ler_coordenada('segundo y')
  x3h = ler_coordenada('terceiro x')
  y3h = ler_coordenada('terceiro y')

def informar_coordenadas_jogador_humano():
  ler_coordenadas()
  while not validar_coordenadas(x1h, y1h, x2h, y2h, x3h, y3h):
    print('Coordenadas inválidas! Devem ser contínuas!')
    ler_coordenadas()

def validar_coordenada_em_cima(x1e, y1e):
  if x1e == x1h and y1e == y1h:
    return False
  if x1e == x2h and y1e == y2h:
    return False
  if x1e == x3h and y1e == y3h:
    return False
  return True

def gerar_coordenadas_jogador_enemigo():
  global x1e, y1e, x2e, y2e, x3e, y3e
  x1e = gera_coordenada()
  y1e = gera_coordenada()  
  while not validar_coordenada_em_cima(x1e, y1e):
    x1e = gera_coordenada()
    y1e = gera_coordenada()  

  # Alinhar para cima

  x3e = x2e = x1e
  y2e = y1e-1
  y3e = y1e-2  
  if not validar_coordenada_em_cima(x2e, y2e) or not validar_coordenada_em_cima(x3e, y3e) or not validar_coordenadas(x1e, y1e, x2e, y2e, x3e, y3e):
   
    # Alinhar para direita
    y3e = y2e = y1e
    x2e = x1e+1
    x3e = x1e+2    
    if not validar_coordenada_em_cima(x2e, y2e) or not validar_coordenada_em_cima(x3e, y3e) or not validar_coordenadas(x1e, y1e, x2e, y2e, x3e, y3e):
      
      # Alinhar para baixo
      x3e = x2e = x1e      
      y2e = y1e+1
      y3e = y1e+2
      if not validar_coordenada_em_cima(x2e, y2e) or not validar_coordenada_em_cima(x3e, y3e) or not validar_coordenadas(x1e, y1e, x2e, y2e, x3e, y3e):
       
        # Alinhar para esquerda
        y3e = y2e = y1e
        x2e = x1e-1
        x3e = x1e-2    

def verificar_acertou_tiro(xa, ya, xb, yb):
  if xa == xb and ya == yb:
    return True
  else:
    return False

def vez_humano():

  global acertos_humano

  x = int(input('Digite a coordenada x para atirar:'))
  y = int(input('Digite a coordenada y para atirar:'))

  while not validar_beirada(x, y):

    print('Deve ser um valor entre 0 e 9')
    x = int(input('Digite a coordenada x para atirar:'))
    y = int(input('Digite a coordenada y para atirar:'))

  if verificar_acertou_tiro(x, y, x1e, y1e) or verificar_acertou_tiro(x, y, x2e, y2e) or verificar_acertou_tiro(x, y, x3e, y3e):
    print('Acertou o enemigo!')

    tabuleiro[y][x] = navio_enemigo
    acertos_humano += 1

  else:
    print('Errou o tiro!')

    tabuleiro[y][x] = tiro

  if acertos_humano == 3:
    return True
  else:
    return False

def vez_enemigo():
  global acertos_enemigo
  # Se ele acertou antes, ao invés de sortear a coordenada x, y, você deve atirar na região próxima onde acertou
  # if acertos_enemigo > 0:
  # ....
  x = random.randrange(0, 10)
  y = random.randrange(0, 10)  

  while not validar_tiro_enemigo(x, y):

    x = random.randrange(0, 10)
    y = random.randrange(0, 10)    

  if verificar_acertou_tiro(x, y, x1h, y1h) or verificar_acertou_tiro(x, y, x2h, y2h) or verificar_acertou_tiro(x, y, x3h, y3h):
    print('O enemigo te acertou!')

    acertos_enemigo += 1
  tabuleiro[y][x] = tiro

  if acertos_enemigo == 3:
    return True
  else:
    return False

def validar_tiro_enemigo(x, y):

  if (tabuleiro[y][x] == ' ' or tabuleiro[y][x] == navio_humano) and tabuleiro[y][x] != navio_enemigo:
    return True
  else:
    return False

informar_coordenadas_jogador_humano()
gerar_coordenadas_jogador_enemigo()
mostrar_tabuleiro()

while not fim_jogo:
  #print('Coordenadas Humano:', x1h, y1h, x2h, y3h, x3h, y3h)
  #print('Coordenadas Enemigo:', x1e, y1e, x2e, y2e, x3e, y3e)
  ganhou_humano = vez_humano()
  mostrar_tabuleiro()  

  if ganhou_humano:

    print('Humano Ganhou!')  
  else:

    ganhou_enemigo = vez_enemigo()
    mostrar_tabuleiro()  

    if ganhou_enemigo:

      print('Enemigo Ganhou!')
  
  if ganhou_humano or ganhou_enemigo:

    fim_jogo = True
