class Zoo:
	count_of_animals = 0

	def __init__(self,animal_name):
		Zoo.count_of_animals += 1
		self.name = animal_name

	def total_count_of_animals(self):
		return Zoo.count_of_animals


zebra = Zoo("Zebra")
elephant = Zoo("Elephant")

print(Zoo.total_count_of_animals)