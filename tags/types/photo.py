class Photo:
	def __init__(self, filepath):
		self.filepath = filepath

	def __repr__(self):
		return self.filepath