import MySQLdb


def writeToDatabase(name, score):
	databaseName = "first"
	tableName = "students"
	query = "insert into students values (%s, %s)"
	conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="123456",
                  db="first")
	x = conn.cursor()
	x.execute("""INSERT INTO students VALUES (%s,%s)""", (name, score))
	conn.commit()
	conn.close()
	
f = open("text.txt")
d = {}
for line in f:
	# remove newline from line
	line = line.strip("\n")
	if len(line) == 0:
		continue

	# split the line into two words
	words = line.split(" ")
	# first word is name
	name = words[0]
	# second word is score
	score = int(words[1])
	d[name] = score
	writeToDatabase(name, score)

print d
