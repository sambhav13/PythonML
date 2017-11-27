import sample

class AB:

    def __init__(self):
        self.__attr = 0

    def getSome(self):
        print("enjoying!!!")


def main():
    a = AB()
    print("hello")
    a.getSome()

if __name__ == '__main__':
    main()