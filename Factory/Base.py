from enum import Enum
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, object_mapper
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, update

class ColumnType(Enum):
    """数据库字段类型枚举
    """
    Str = String
    Int = Integer


pass


#继承ORM基类
def BaseModel():
    return declarative_base()


def IntegerColum(isPrimaryKey=False):
    return Column(Integer, primary_key=True)


def StringColumn(isPrimaryKey=False, len=0):
    return Column(len > 0 and String(len) or String)


pass


class BaseCRUD:
    __database__ = None

    session = None

    def __getPrimayKeys__(self):
        mapper = object_mapper(self)
        result = list(map(lambda col:col.key,mapper.primary_key))
        return result

    def __initConnect__(self):
        #数据库连接
        engine = create_engine(self.__database__, echo=True)
        session = sessionmaker(bind=engine)
        self.session = session()
        pass

    def Create(self, new):
        self.__initConnect__()
        self.session.add(new)
        self.session.commit()
        pass

    def Update(self, data, targetColumn=None):
        self.__initConnect__()
        self.session.commit()
        pass
    
