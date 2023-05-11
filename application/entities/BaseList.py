from abc import ABC, abstractmethod
from datetime import date
from typing import List

from application.entities.BaseItem import BaseItem

class BaseList(ABC):
	def __init__(self, id: int, name: str, creation_date: date):
		self.ID = id
		self.name = name
		self.creation_date = creation_date
		self.item_list:List[BaseItem] = []

	@abstractmethod
	def add_item(self, item: BaseItem) -> None:
		self.item_list.append(item)

		def takeId(elem: BaseItem):
			return elem.ID
		
		self.item_list.sort(takeId)

	
	@abstractmethod
	def delete_item(self, id: int) -> None:
		index = self.__find_item_index(id)

		if(index is not -1):
			self.item_list.pop(index)
		else:
			raise NotImplementedError()
	
	@abstractmethod
	def update_item(self, id: int, values: dict) -> None:
		index = self.__find_item_index(id)

		if(index is -1):
			raise NotImplementedError()

		item = self.item_list[index]
		item.update(values)

	@abstractmethod
	def update_list(self, values: dict) -> None:
		...

	def __find_item_index(self, id: int) -> int:
		start = 0
		end = len(self.item_list) - 1
		middle = 0

		while(start < end):
			middle = (start + end) // 2
			item = self.item_list[middle]
			if(item.ID == id ):
				return middle
			elif(item.ID > id):
				end = middle - 1
			else:
				start = middle + 1

		return end if self.item_list[end].ID == id else -1
