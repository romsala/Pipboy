# Endroit pour entreposer des variables accessibles à tous les scripts

screen = 3
def InitGlobal():
    screen = 3

# TODO je sais pas si on laisser le getter ou pas...
def GetScreen():
    return screen

def SetScreen(new):
    _screen = new


class Directory:
    def __init__(self, path, rect):
        self.next = None
        self.path = path
        self.rect = rect

    def Append(self, dir):
        if self.next is None:
            self.next = Directory(dir.path, dir.rect)
            self.next.path = dir.path
            self.next.rect = dir.rect
        else:
            self.next.Append(dir)