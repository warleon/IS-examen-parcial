class threeMultOfTen:
	def __init__(self):
		self.count=0

	def check_win(self,number):
		if(number%10==0):
			self.count+=1

		if(self.count>=3):
			return True
		
		return False

		