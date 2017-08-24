def make_msg(textA, textH):
      return textA = textH

def get_scream():
      numA = random.randint(1,15)
      numH = random.randint(1,15)
      textA = "a" * numA
      textH = "h" * numH
      scream_msg - make_msg(textA, textH)
      return scream_msg

numA2 = random.randint(1,15)
numH2 = random.randint(1,15)
def get_scream2(numA2,numH2):
    textA2 = "a" * numA2
    textH2 = "a" * numH2
    scream_msg = make_msg(textA2, textH2)
    return scream_msg

#scream = get_scream()
#print(scream)

def main():
    scream = get_scream()
    print(scream)
    scream2 = get_scream2(numA2, numH2)
    print(scream2)
main()
