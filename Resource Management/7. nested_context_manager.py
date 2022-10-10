from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File', file)
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File', file)
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File', file)
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File', file)
    open_card_file.close()

with poem_files('poem.txt', 'r') as poem:
   with card_files('card.txt', 'w') as card:
     print(poem, card)
     card.write(poem.read())