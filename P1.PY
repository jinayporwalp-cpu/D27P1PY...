class FamilyMember:
	def __init__(self,eye_colour,height_cm):
		self.eye_colour = eye_colour
		self.height_cm = height_cm

	def show_traits(self):
		print("eye colour ",self.eye_colour)
		print("height cm",self.height_cm)

class Kid(FamilyMember):
	def __init__(self, name,age, eye_colour, height_cm):
		self.name = name
		self.age = age
		super().__init__(eye_colour, height_cm)

	def show_traits(self):
		print("name",self.name)
		print("age",self.age)
		super().show_traits

	def favoriote_hobby(self,hobby):
		print(self.name,"loves",hobby)

child = Kid("Maya",10,"brown",140)
child.show_traits()
child.favoriote_hobby("painting")
print("is kid a subclass of familymember?",issubclass(Kid,FamilyMember))