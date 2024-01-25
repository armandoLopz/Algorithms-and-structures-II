class carpeta:

    def __init__(self, id, name, totalSize, creationDate, fileList = [], foldersList = []):

        self.id = id
        self.name = name
        self.fileList = fileList
        self.creationDate = creationDate
        self.foldersList = foldersList
        self.totalSize = totalSize