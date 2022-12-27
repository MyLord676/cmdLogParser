from datetime import datetime
from sys import argv

from MyLibs.myTimeLib import round_time_floor
from MyMockInterface.txtReader import txtReader


def Main():
    print(argv)
    if len(argv) <= 1:
        print("file not selected.")
        return

    for i in range(1, len(argv), 1):
        currentFile = txtReader(argv[i])
        j = 0
        while True:
            j += 1
            line = currentFile.readline()
            if not line:
                currentFile.close()
                break
            parts = line.split(' ')
            print(j, line)
            print(parts[len(parts) - 2])
            date = datetime.strptime(parts[3], "[%d/%b/%Y:%H:%M:%S")
            print(date)


if __name__ == "__main__":
    Main()
