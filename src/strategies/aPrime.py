class APrime():
	def __init__(self):
		self.count=0
		self.isPrime=[True for i in range(1,101)]

	def check_win(self,number):
		if(self.isPrime[number]):
			self.count+=1

		if(self.count>=1):
			return True
		
		return False