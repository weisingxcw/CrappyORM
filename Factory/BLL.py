import Entity


class MovBLL(Entity.Mov):
    def __init__(self, initObj):
        self = initObj

    def AddNewMov(self, newMov):
        self.Create(newMov)
        pass


newMov = Entity.Mov()

newMov.title = 'sf'
newMov.id = 1

movMethod = MovBLL(newMov)
movMethod.Update(newMov)