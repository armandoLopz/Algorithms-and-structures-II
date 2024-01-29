import fichero 
import unidad 
import carpeta 
import comando 
import datetime

fi = fichero.fichero(1,"Documentos",20,".json", 20, "Archivo de prueba" )
fi1 = fichero.fichero(2,"archivos futbol",70,".json", 120, "Archivo de prueba" )
fi2 = fichero.fichero(3,"archivos beisbol",270,".json", 220, "Archivo de prueba" )
fi3 = fichero.fichero(4,"archivos tenis",40,".json", 204, "Archivo de prueba" )

listFiles = [fi,fi1,fi2,fi3]

ca = carpeta.carpeta(1,"Imagenes", 400, datetime.datetime.now, listFiles, None)
ca2 = carpeta.carpeta(2,"Imagenes Familia", 300, datetime.datetime.now, listFiles, None)
ca3 = carpeta.carpeta(3,"Contenido PDF", 1400, datetime.datetime.now, listFiles, None)

listFolders = [ca,ca2,ca3]

un1 = unidad.unidad(1,"C",1024, 350, "SSD", listFolders)

#print(fi.showDetailsFile())
#print("ARCHIVOS DE LA CARPETA: ")
#print(ca.contentFolder())

comando = comando.comando(1,"comando dir", "Describe los archivos que hay en la unidad ", "ADMIN")

print("COMANDO DIR ")

print(comando.commandDir(un1))