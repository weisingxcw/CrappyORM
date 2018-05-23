from enum import Enum
from Base import BaseCRUD, BaseModel, IntegerColum, StringColumn


class DataBase(Enum):
    local = 'mysql+pymysql://root:root@localhost:3306/movindex'


class Mov(BaseModel(),BaseCRUD):
    #数据库连接配置
    __database__ = DataBase.local.value
    #表名
    __tablename__ = 'mov'
    #字段
    id = IntegerColum(isPrimaryKey=True)
    title = StringColumn(isPrimaryKey=False, len=150)
pass
