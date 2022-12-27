from datetime import datetime

from MyLibs.myTimeLib import round_time_floor


if __name__ == "__main__":
    r = round_time_floor(datetime(2017, 2, 26, 12, 58, 0))
    t = datetime.fromtimestamp(r)
    print(t)
