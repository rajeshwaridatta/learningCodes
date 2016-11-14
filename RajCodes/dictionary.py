
def findScore(rollList,scoreList,rollint):
	for index in range(0,len(rollList)):
		if rollList[index]==rollint:	
			return scoreList[index]
	return -1

def findScoreV2(d, rollint):
	return d[rollint]

rollList = []
scoreList = []
d = {}
for roll in range(10000, 11000000):
	rollList.append(roll)
	scoreList.append(roll % 100)
	d[roll] = roll % 100

import time
ct = time.time()
print findScore(rollList, scoreList, 10500056)
print 10000 *(time.time() - ct)
ct = time.time()
print findScoreV2(d, 10500056)
print 10000 *(time.time() - ct)
