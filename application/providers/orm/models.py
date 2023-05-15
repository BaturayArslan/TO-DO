from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy import String, Date, Integer, ForeignKey, Boolean
from datetime import date
from typing import Optional, List



class Base(DeclarativeBase):
    pass

class ListModel(Base):
    __tablename__ = "TodoList"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    user: Mapped["UserModel"] = relationship(back_populates="lists")
    name: Mapped[str] = mapped_column(String(30))
    creation_date: Mapped[date] = mapped_column(Date())
    update_date: Mapped[Optional[date]] = mapped_column(Date())
    deletion_date: Mapped[Optional[date]] = mapped_column(Date())
    completion_percentage: Mapped[int] = mapped_column(Integer())
    item_list: Mapped[List["ItemModel"]] = relationship(back_populates="list", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"ListModel(id={self.id}, name={self.name}, creation_date={self.creation_date}, update_date={self.update_date},\
            deletion_date={self.deletion_date}, complition={self.completion_percentage}, item_list: {self.item_list})"


class ItemModel(Base):
    __tablename__ = "TodoItem"

    id: Mapped[int] = mapped_column(primary_key=True)
    list_id: Mapped[int] = mapped_column(ForeignKey("TodoList.id"))
    list: Mapped["ListModel"] = relationship(back_populates="item_list")
    creation_date: Mapped[date] = mapped_column(Date())
    content: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String())
    deletion_date: Mapped[Optional[date]] = mapped_column(Date())
    update_date: Mapped[Optional[date]] = mapped_column(Date())

    def __repr__(self) -> str:
         return f"ItemModel(id={self.id}, list_id={self.list_id}, creation_date={self.creation_date}, update_date={self.update_date},\
            deletion_date={self.deletion_date}, status={self.status}, content={self.content}, list={self.list})"


class UserModel(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(100))
    privileged: Mapped[bool] = mapped_column(Boolean())
    lists: Mapped[List["ListModel"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, password={self.password}, privileged={self.privileged})"