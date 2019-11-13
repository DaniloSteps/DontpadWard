import os
from time import sleep

def main():
    print("Enter the dontpad domain you wish to ward:")
    warded = input("http://dontpad.com/")

    os.system('mkdir {}'.format(warded))

    os.system('cp dontpadWard.py {}'.format(warded))

    os.chdir(warded)

    os.system('mv dontpadWard.py .dontpadWard.py')

    address = open('address.txt', 'w+')
    address.write(warded)
    address.close()

    os.system('nohup python3 {}/.dontpadWard.py &'.format(os.getcwd()))

    sleep(1)

    os.system('rm address.txt')


main()
