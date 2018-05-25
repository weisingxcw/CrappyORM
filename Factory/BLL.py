import Entity


class MovBLL(Entity.Mov):
    """电影逻辑层
        :param Entity.Mov: 
    """
    def AddNewMov(self, newMov):
        self.Create(newMov)
        pass


newMov = Entity.Mov()
newMov.title = 'sf'
newMov.id = 3

print(type(MovBLL().ReadByFilter(1,{'id':1})))