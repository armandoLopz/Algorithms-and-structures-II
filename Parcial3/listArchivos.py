class listArchivos:

    def __init__(self, archivos = []):

        self.__archivos = archivos
    
    def addArchivos(self, archivo):

        #Se agregan los archivos a la lista
        self.archivos.append(archivo)