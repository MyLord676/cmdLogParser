from datetime import datetime
from sys import argv
import json
import yaml

from MyLibs.myTimeLib import round_time_floor
from MyMockInterface.txtReader import txtReader


def Main():
    if len(argv) <= 1:
        print("file not selected.")
        return

    with open("Configs/Config.yaml", "r") as stream:
        try:
            cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    myDict: dict[float, dict[str, int]] = {}

    for i in range(1, len(argv), 1):
        currentFile = txtReader(argv[i])
        while True:
            line = currentFile.readline()
            if not line:
                currentFile.close()
                break
            parts = line.split(' ')
            statusCode = parts[len(parts) - 2]
            date = datetime.strptime(parts[3], "[%d/%b/%Y:%H:%M:%S")
            roundDate = round_time_floor(date, cfg['grouping_depth'])
            if roundDate in myDict:
                if statusCode in myDict[roundDate]:
                    myDict[roundDate][statusCode] += 1
                else:
                    myDict[roundDate][statusCode] = 1
            else:
                myDict[roundDate]: dict[str, int] = {}

    sortDict = dict(sorted(myDict.items()))
    for key in sortDict:
        print(datetime.fromtimestamp(key), ": ")
        print(json.dumps(sortDict[key], sort_keys=True, indent=4))


if __name__ == "__main__":
    Main()
