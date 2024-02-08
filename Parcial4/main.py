import datetime
from objects.SystemComponents import file as fl
from objects.DOSconsolePA import DOSconsole 
from objects.SystemComponents import unit, folder
from objects.userManage import user

file = fl.file(1,"A", 48, "txt", "20/14/74", None,"skskkskks" )
file2 = fl.file(1,"A", 48, "txt", "20/14/74", None,"skskkskks" )
file3 = fl.file(1,"A", 48, "txt", "20/14/74", None,"skskkskks" )
file4 = fl.file(1,"A", 48, "txt", "20/14/74", None,"skskkskks" )
"""
file2 = file.file(17,"B", 46, "txt", "20/14/74", None,"skskkskks" )
file3 = file.file(3,"C", 45, "txt", "20/14/74", None,"skskkskks" )
file4 = file.file(157,"D", 14, "txt", "20/14/74", None,"skskkskks" )
file5 = file.file(15,"3", 44, "txt", "20/14/74", None,"skskkskks" )"""

lisFiles = [file,file2,file3,file4]

#lisFiles = [file,file2,file3,file4,file5]

ca = folder.folder(1,"ArchivosJSON", 400, datetime.datetime.now, lisFiles, None)
ca2 = folder.folder(2,"ImagenesFamilia", 300, datetime.datetime.now, lisFiles, None)
ca3 = folder.folder(3,"ContenidoPDF", 1400, datetime.datetime.now, lisFiles, None)

listFolders = (ca,ca2,ca3)

unit = unit.unit(1,"C:",1024,1024, "SSD", listFolders)

consola = DOSconsole.DOSConsole(unit)

consola.run()