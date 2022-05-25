class APrime():
	def __init__(self):
		self.count=0
		self.isPrime= self.create_primes()

	def create_primes(self):
		isPrime=[True for i in range(0,101)]
		isPrime[0]=False
		isPrime[1]=False
		for i in range(2,101):
			if isPrime[i]:
				for j in range(2*i,101,i):
					isPrime[j]=False
		return isPrime

	def check_win(self,number):
		if(self.isPrime[number]):
			self.count+=1

		if(self.count>=1):
			return True
		
		return False