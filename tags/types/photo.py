class Photo:
	def __init__(self, filepath):
		self.filepath = filepath
		self.filename = filepath.split('/')[-1]

	def __repr__(self):
		return self.filename