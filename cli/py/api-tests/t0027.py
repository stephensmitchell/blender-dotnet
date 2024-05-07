import clr
clr.AddReference(r'C:\Users\steph\Desktop\blenderdotnet\libs\libfs\bin\Debug\net481\libfs.dll')
import libfs # type: ignore
from libfs import Say # type: ignore
Say.hello("World")
#print(dir(Say))
#print(help(Say.hello))
