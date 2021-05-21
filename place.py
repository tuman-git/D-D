"""
place - this is a board for game 
-----------------------------------------------------
Board1= Board(N,M) / create a place of size a M*N  

"""
def Print_list_in_normal_status(Listok):
	for i in Listok:
		print(i,' \n')


class Board:	
	def __init__(self,length,width):
		k = 'less'
		self.place = [[k for j in range(length)] for i in range(width)]
	def create_asylum(self, N, M):
		self.place[N,M] = 'asylum'

	def create_cell_for_Person(self, N, M, Name_Person):
		self.place[N,M] = Name_Person


Board1= Board(10,10)
Board1.create_asylum(4,5)
Board1.create_cell_for_Person(1,2, "Ivan")

		

Print_list_in_normal_status(Board1.place)