
from le_poste import __version__ as _version
from le_poste.config import config
from sklearn.base import BaseEstimator, TransformerMixin

class Queue(BaseEstimator, TransformerMixin):
	"""This queue subcategory is not demande deployment
		A new excel file for manual inspection is being created"""

	def __init__(self, df, name, path_s):
		self.df = df
		self.name = name
		self.path_s = path_s

	def fit(self):
		return self

	def transform(self):
		self.df.to_excel(self.path_s / self.name)