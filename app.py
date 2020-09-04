import random


def shuffle(string):
    arr = list(string)
    random.shuffle(arr)
    return "".join(arr)


uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))
lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))
punc1 = chr(random.randint(33, 37))
punc2 = chr(random.randint(33, 37))

password = uppercase1 + uppercase2 + lowercase1 + lowercase2 + punc1 + punc2

print(shuffle(password))
