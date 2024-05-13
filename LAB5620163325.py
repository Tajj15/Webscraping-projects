#Problem 1
def encode(str):
	if len(str) == 0:
		return ""
	else:
		return chr(ord(str[0]) + 5) + encode(str[1:])

def decode(str):
    if not str:
        return ""
    return chr(ord(str[0]) - 5) + decode(str[1:])

#Problem 2
def removePun(s):
    punctuation = [",", ".", "?", "!", ";", ":"]
    new_string = " "
    for char in s:
      if char not in punctuation:
        new_string += char
    return new_string

#Problem 3
def stringList(str1):
	return str1.split()

def encodeM(lst):
  if not lst:
    return []
  else:
    return [encode(lst[0])] + encodeM(lst[1:])
      

def decodeM(lst):
  if not lst:
    return []
  else:
    return [decode(lst[0])] + decodeM(lst[1:])

def main(s):
	slst=removePun(s)
	eList = encodeM(stringList(slst))
	dList = decodeM(eList)
	print("Given string =>", s)
	print("Punctuation removed =>", slst)
	print("List Encoded =>", eList)
	print("List Decoded =>", dList)
	print ("Encoded Message =>",' '.join(eList))

