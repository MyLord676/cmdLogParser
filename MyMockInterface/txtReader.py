from MyInterfaces.logReaderInterface import logReader


class txtReader(logReader):
    def __init__(self, path):
        self.file = open(path, 'rb')

    def readline(self):
        bytesLine = self.file.readline()
        if bytesLine:
            decodeLine = bytesLine.decode("utf-8")
            return decodeLine
        return None

    def close(self):
        self.file.close()
