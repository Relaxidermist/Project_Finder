class IProject:
	subdir = []

	def _init_(self, name):
		print(name)

	def format(self, mode):
		if mode == 0:
			output_string = ""
			for item in self.subdir:
				output_string = output_string + item + "\t"
		else:
			output_string = "Not Supported"
		return output_string

	def identify(self):
		print(type(self))