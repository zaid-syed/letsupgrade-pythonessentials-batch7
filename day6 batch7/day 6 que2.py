import math
class cone:
	
	def __init__ (self):
		self.radius=int(input("Enter radius for Cone: "))
		self.height=int(input("Enter height for Cone: "))
	def volume(self):
		volumeCone=(math.pi*(self.radius**2)*self.height)/3
		return volumeCone
	def surface_Area(self):
		Base=math.pi*(self.radius**2)
		Side=math.pi*self.radius*(math.sqrt(self.radius**2+self.height**2))
		return Base+Side



aCone=cone()
print("Volume of cone is: ",aCone.volume())
print("Surface Area of cone is:",aCone.surface_Area())