class TwoMultOfTwentyFive():
	def __init__(self):
		self.count=0

	def check_win(self,number):
		if(number%25==0):
			self.count+=1

		if(self.count>=2):
			return True
		
		return False
