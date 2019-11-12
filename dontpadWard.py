import requests
from bs4 import BeautifulSoup
from os import system
import time


def access_dontpad(dontpad):
    link = requests.get(dontpad)
    soup = BeautifulSoup(link.text, 'html.parser')
    text = soup.find('textarea').get_text()
    buffer = open('buffer.txt', 'w+')
    buffer.write(text)
    buffer.close()


def log(address, last_time):
    log_file = open('log.txt', 'a+')
    log_file.write(
        '\nhttp://dontpad.com/{} changed at {}.'.format(address, last_time))
    log_file.close()


def main():

    with open('address.txt') as warded:
        address = warded.read()

    access_dontpad("http://dontpad.com/{}/".format(address))
    last_time = time.strftime("%H:%M:%S-%d_%m_%Y", time.localtime())
    system('mv buffer.txt {}_{}.txt'.format(address, last_time))

    log_file = open('log.txt', 'w+')
    log_file.write(
        'Warded \"http://dontpad.com/{}\" at {}'.format(address, last_time))
    log_file.close()

    while (1):
        access_dontpad("http://dontpad.com/{}/".format(address))

        with open('{}_{}.txt'.format(address, last_time)) as last_file, open('buffer.txt') as buffer:
            last_data = last_file.read()
            buffer_data = buffer.read()
            if last_data != buffer_data:
                last_time = time.strftime(
                    "%H:%M:%S-%d_%m_%Y", time.localtime())
                system('mv buffer.txt {}_{}.txt'.format(address, last_time))
            #     log_file = open('log.txt', 'a+')
            #     log_file.write(
            #         '\nhttp://dontpad.com/{} changed at {}.'.format(address, last_time))
            #     log_file.close()
            # else:
            #     log_file = open('log.txt', 'a+')
            #     log_file.write(
            #         '\nNo changes on http://dontpad.com/{} at {}.'.format(address, last_time))
            #     log_file.close()

            log_time = time.strftime("%H:%M:%S-%d_%m_%Y", time.localtime())

            log_file = open('log.txt', 'w+')
            log_file.write(
                'The last call to ward was at {}.'.format(log_time))
            log_file.close()

        time.sleep(5)


main()
