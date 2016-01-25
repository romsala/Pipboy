# Endroit pour entreposer des variables accessibles à tous les scripts

screen = 3
def InitGlobal():
    screen = 3

# TODO je sais pas si on laisser le getter ou pas...
def GetScreen():
    return screen

def SetScreen(new):
    _screen = new
