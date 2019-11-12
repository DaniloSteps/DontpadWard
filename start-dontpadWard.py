import os


def create_address(warded):
    address = open('address.txt', 'w+')
    address.write(warded)
    address.close()


def create_folder(warded):
    os.system('mkdir {}'.format(warded))
    os.system('mv address.txt {}'.format(warded))


def place_ward(warded):
    path = os.path.dirname(os.path.abspath(__file__))

    os.system('cp dontpadWard.py {}/{}'.format(path, warded))
    os.system('nohup python3 {}/{}/dontpadWard.py &'.format(path, warded))


def main():
    print("Enter the dontpad domain you wish to ward:")
    warded = input("http://dontpad.com/")

    create_address(warded)

    create_folder(warded)

    place_ward(warded)


main()
