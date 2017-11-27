from sample.core import AB

class XY:

    def __init__(self):
        self.__attr = 0

    def write(self):
        b = AB()
        b.getSome()


def main():
    x = XY()
    x.write()


if __name__ == '__main__':
    main()