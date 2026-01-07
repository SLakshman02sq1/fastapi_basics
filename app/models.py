from sqlalchemy import Column,Integer,String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String,index=True,unique=True)
    email = Column(String,index=True)


# id: Mapped[int] = mapped_column(primary_key=True, index=True)
# name: Mapped[str] = mapped_column(index=True)
# email: Mapped[str] = mapped_column(index=True)