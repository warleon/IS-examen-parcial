class APrime():
	def __init__(self):
		self.count=0
		self.is_prime= self.create_primes()

	def create_primes(self):
		prime_list=[True for x in range(0,101)]
		prime_list[0]=False
		prime_list[1]=False
		for i in range(2,101):
			if prime_list[i]:
				for j in range(2*i,101,i):
					prime_list[j]=False
		return prime_list

	def check_win(self,number):
		if(self.is_prime[number]):
			self.count+=1

		if(self.count>=1):
			return True
		
		return False