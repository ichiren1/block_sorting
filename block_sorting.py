import sys

def encode(text):
  text = text.strip() + '$'
  block = []
  for t in text:
    block.append(text)
    text = text[1:]+text[0]
  return ''.join([b[-1] for b in sorted(block)])

def decode(text):
  L = [t for t in text]
  pos = text.find('$')
  LF_mapping = {
    index:tup[0] for index, tup in enumerate(
    sorted(
      {index: t for index, t in enumerate(L)}.items()
    , key=lambda x:x[1]))
  }
  result = []
  for _ in L:
    pos = LF_mapping[pos]
    result.append(L[pos])
  return "".join(result)

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print('usage: "e"or"d" text')
    quit()
  if sys.argv[1] == 'e':
    print(encode(sys.argv[2]))
  elif sys.argv[1] == 'd':
    print(decode(sys.argv[2]))
  else:
    print('argv1 is "e" encod or "d" decode')
