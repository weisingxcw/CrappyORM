from enum import Enum
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, object_mapper
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, update


#继承ORM基类
def BaseModel():
    return declarative_base()


def IntegerColum(isPrimaryKey=False):
    return Column(Integer, primary_key=True)


def StringColumn(isPrimaryKey=False, len=0):
    return Column(len > 0 and String(len) or String)


pass


def GetPrimaryKeyDict(obj):
    #返回主键LIST
    mapper = object_mapper(obj)

    keys = list(
        map(lambda col: {col.key: getattr(obj, col.key)}, mapper.primary_key))

    #转换list[dict]为dicts
    return {k: v for dct in keys for k, v in dct.items()}


class BaseCRUD:
    __database__ = None

    session = None

    def __initConnect__(self):
        """初始化数据库会话连接，依赖于self.__database__的数据库配置，来建立连接
            :param self: 
        """
        #数据库连接
        engine = create_engine(self.__database__, echo=True)
        session = sessionmaker(bind=engine)
        self.session = session()
        pass

    def Create(self, new):
        """新增数据
            :param self: 
            :param new: 新增对象单例
        """
        self.__initConnect__()
        self.session.add(new)
        self.session.commit()
        pass

    def ReadById(self, *args):
        """读取数据（主键）
            :param self: 
            :param **kwargs: 主键值
        """
        self.__initConnect__()
        instance = self.session.query(self.__class__).get(args)
        return instance

    def ReadByFilter(self, scalar, dict):
        """读取数据（条件）
            :param self: 
            :param **kwargs: 
        """
        self.__initConnect__()
        instance = self.session.\
                        query(self.__class__).\
                        filter_by(**dict).\
                        limit(scalar)
        return instance

    def Update(self, data, **kwargs):
        """更新数据（主键）
            :param self: 
            :param adttribute_names:更新对象单例
            :param **kwargs:更新字段（例：name = 'charle'）
        """
        self.__initConnect__()
        primaryKey = GetPrimaryKeyDict(data)
        scalar = self.session.query(self.__class__).\
                        filter_by(**primaryKey).\
                        update(kwargs)
        self.session.commit()
        return scalar

    def Delete(self, data):
        """删除数据（主键）~慎重
            :param self: 
            :param data: 删除对象单例
        """
        self.__initConnect__()
        primaryKey = GetPrimaryKeyDict(data)
        scalar = self.session.query(self.__class__).\
                        filter_by(**primaryKey).\
                        delete(synchronize_session='fetch')
        self.session.commit()
        return scalar
