from sprites import HANGMAN_SPRITES

# Variables

word = ''
max_tries = len(HANGMAN_SPRITES) - 1
fails = 0
raw_input = ''
clues = []

# Funciones

def save_assertions(raw_input):
  global word, clues
  for l in raw_input:
    for i, letter in enumerate(word):
      if(l == letter):
        clues[i] = letter

def print_status():
  global clues, max_tries, fails
  print('Intentos restantes: %s' % (max_tries - fails))
  print(HANGMAN_SPRITES[fails])
  print(' '.join(clues))
  print('')

def up_fails():
  global fails
  fails = fails + 1

def game_completed():
  global word, clues, raw_input
  completed_by_clues = ''.join(word) == ''.join(clues)
  completed_by_word = ''.join(word) == ''.join(raw_input)
  return completed_by_clues or completed_by_word

def no_more_tries():
  global max_tries, fails
  return max_tries > fails

def clue_discovered():
  global raw_input, word
  return len(raw_input) == 1 and raw_input[0] in word

def clear_screen():
  print(chr(27) + "[2J")

# Logica del juego

word = list(input('Escribe la palabra a descubrir: ').upper())
clues = list('_' * len(word))
clear_screen()

while(not game_completed() and no_more_tries()):
  clear_screen()
  print_status()
  raw_input = list(input("Digita una letra o la palabra: ").upper())
  if(clue_discovered()):
    save_assertions(raw_input)
  else:
    up_fails()


if(not game_completed()):
  print('PERDISTE')
  print_status()
else:
  print('GANASTE')
  save_assertions(raw_input)
  print_status()
