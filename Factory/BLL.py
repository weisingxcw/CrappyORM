import Entity


class MovBLL(Entity.Mov):
    def __init__(self,initObj):
        self = initObj
        print(self.title)
    def AddNewMov(self, title):
        self.Create()
        pass

newMov = Entity.Mov()
newMov.title = 'sf'

movMethod = MovBLL(newMov)
movMethod.AddNewMov('tfs')