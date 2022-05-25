class FiveEven():
	def __init__(self):
		self.count=0

	def check_win(self,number):
		if(number%2==0):
			self.count+=1

		if(self.count>=5):
			return True
		
		return False
