def npi(expr):
	pile = []
	for elt in expr:
		if elt == '+':
			b, a = pile.pop(), pile.pop()
			pile.append(a+b)
		elif elt == '*':
			b, a = pile.pop(), pile.pop()
			pile.append(a*b)
		else:
			pile.append(int(elt))
	return print(pile.pop())

npi([3, 2, '+', 13, '*'])
