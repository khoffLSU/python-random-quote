import random

def primary():
  # print("Keep it logically awesome. Test statement")

  with open("quotes.txt") as f:
    quotes = f.readlines()

  rnd = random.randint(0,len(quotes)-1)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
