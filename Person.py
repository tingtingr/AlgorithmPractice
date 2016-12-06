# class Person {
#     int id;
#     String name;
#     List<Person> friends;
#     // mike => {miller, Jelly, Billy}
#     // miller => {miller, Cathy}
#     // Billy => {Henry, John}
#     // Cathy => {miller}
#     // print friends list of current person, e.g, mike -> miller, Jelly, Billy, Henry, John. more info on 1point3acres.com
#     public void printFriend() {
#         // implement here
#     }
# }

class Person(object):
	def __init__(self, name, id):
		self.id = id
		self.name = name
		self.friends = set()
	def addFriend(self, person):
		self.friends.add(person)
	def printFriendsGraph(self):
		res = set()
		s = self.friends
		while s:
			n = s.pop()
			res.add(n)
			for m in n.friends:
				if m not in res and m.name != self.name:
					s.add(m)
		for x in res:
			print(x.name),
		print('\n')

Mike = Person('Mike', 1)
Mitch = Person('Mitch', 2)
Ryan = Person('Ryan', 3)
Lila = Person('Lila',4)
Mike.addFriend(Mitch)
Mike.addFriend(Ryan)
Mitch.addFriend(Mike)
Ryan.addFriend(Mike)
Ryan.addFriend(Lila)
Lila.addFriend(Ryan)


# Mike.printFriendsGraph()
#Lila.printFriendsGraph()
#Mike.printFriendsGraph()
#Mitch.printFriendsGraph()
#Ryan.printFriendsGraph()
Lila.printFriendsGraph()