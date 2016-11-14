
class Student:
	__rollNumberSeparator = "."

	def __init__(self, roll):
		self.dept = roll[:2]
		self.section = roll[3:5]
		self.roll = int(roll[6:])

	def setScore(self, score):
		self.score = score

	def printDetails(self):
		print "Student with roll number " + self.__getPrintableRoll() + " has score " + str(self.score)

	def __getPrintableRoll(self):
		return self.dept + Student.__rollNumberSeparator + self.section + Student.__rollNumberSeparator + str(self.roll)

s1 = Student("CS.S1.100")
s1.setScore(90)
s1.printDetails()

