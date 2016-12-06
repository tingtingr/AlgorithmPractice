class BigInt(object):
	def add(self, int1, int2):
		l1 = [int(i) for i in list(int1)[::-1]]
		l2 = [int(i) for i in list(int2)[::-1]]
		res = []
		carry = 0
		if l1 < l2:
			self.add(l2,l1)
			print(l1)
			print(l2)
		for i in range(len(l1)):
			sumV = l1[i]+ l2[i] + carry if i < len(l2) else l1[i] + carry
			digit = sumV % 10
			carry = sumV / 10
			res.append(digit)
		return "".join(reversed([str(i) for i in res]))

	def substract(self, int1,int2):
		l1 = [int(i) for i in list(int1)[::-1]]
		l2 = [int(i) for i in list(int2)[::-1]]
		res = []
		carry = 0
		if len(l1) < len(l2):
			return "-"+ self.substract(int2,int1)
		for i in range(len(l1)):
			a = l1[i] + carry
			b = l2[i] if i < len(l2) else 0
			carry = 0
			if a < b:
				value = a + 10 - b
				res.append(value)
				carry = -1
			else:
				value = a - b
				res.append(value)
		s = "".join(reversed([str(i) for i in res]))
		return s
		
	def multiply(self, int1, int2):
		l1 = map(int,list(int1))
		l2 = map(int,list(int2))
		res = [0 for i in range(len(l1)*len(l2))]
		for i in range(len(l2)-1, -1, -1):
			carry = 0
			for j in range(len(l1) - 1, -1, -1):
				print(l1[j],l2[i])
				value = l1[j]*l2[i] + carry
				print(value)
				carry = (res[i+j+1] + value) / 10
				print(carry)
				res[i+j+1] = (res[i+j+1] + value) %10
				print(res)
			res[i] += carry
		res = "".join([str(i) for i in res])
		return '0' if not res.lstrip('0') else res.lstrip('0')
		
		# for i in range(len(l2)):
		# 	carry = 0
		# 	for j in range(len(l1)):
		# 		temp = l1[i] * l2[i] + carry
		# 		carry = res[i+j] + temp //10
		# 		res[i+j] = (res[i+j] + temp) % 10
		# 	res[i] += carry
		# res = "".join([str(i) for i in res])
		# return '0' if not res.lstrip('0') else res.lstrip('0')




		# def multiply(self, num1, num2):
  #   res = [0] * (len(num1) + len(num2))
  #   for i in xrange(len(num1)-1, -1, -1):
  #       carry = 0
  #       for j in xrange(len(num2)-1, -1, -1):
  #           tmp = int(num1[i])*int(num2[j])+carry 
  #           # take care of the order of the next two lines
  #           carry = (res[i+j+1] + tmp) // 10  
  #           res[i+j+1] = (res[i+j+1] + tmp) % 10
  #           # or simply: carry, res[i+j+1] = divmod((res[i+j+1] + tmp), 10)
  #       res[i] += carry
  #   res = "".join(map(str, res))
  #   return '0' if not res.lstrip("0") else res.lstrip("0")

x = BigInt().add('1234127364918649813641','24631846147631764175')
print(x)
print(1234127364918649813641 + 24631846147631764175)

y = BigInt().substract('1236565435','23162873618726318726311')
print(1236565435-23162873618726318726311)
print(y)

z = BigInt().multiply('25', '123')
print(25 * 123)
print(z)
# if a = 10
# b = 8
# then 

# we have 0, 1
# and 8
#  0 < 8
#   then carry -1
#   0 + 10 - 8
