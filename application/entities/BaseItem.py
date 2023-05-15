from abc import ABC, abstractmethod
from datetime import date
from typing import Optional



class BaseItem:
	
	def __init__(self, id: int, creation_date: date, content: str, list = None) -> None:
		self.ID = id
		self.list = list
		self.creation_date = creation_date
		self.content = content

	@abstractmethod
	def update(self, values: dict) -> None:
		...
	
	def set_list(self, list) -> None:
		self.list = list