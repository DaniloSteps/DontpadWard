import requests
from bs4 import BeautifulSoup
from os import system
import time


def access_dontpad(dontpad):
    link = requests.get(dontpad)
    soup = BeautifulSoup(link.text, 'html.parser')
    text = soup.find('textarea').get_text()
    return text


def download_dontpad(dontpad):
    text = access_dontpad(dontpad)
    buffer = open('buffer.txt', 'w+')
    buffer.write(text)
    buffer.close()


# def save():



def main():
    monitored = input("Please enter the dontpad domain you wish to monitor: ")

    download_dontpad("http://dontpad.com/"+monitored+"/")
    last_time = time.strftime("%H:%M:%S-%d_%m_%Y", time.localtime())
    system("mv buffer.txt save_{}.txt".format(last_time))

    while (1):
        download_dontpad("http://dontpad.com/"+monitored+"/")
        # download_dontpad("http://pudim.com.br/")

        # save()

        with open('save_{}.txt'.format(last_time)) as last_file, open('buffer.txt') as buffer:
            last_data = last_file.read()
            buffer_data = buffer.read()
            if last_data != buffer_data:
                last_time = time.strftime("%H:%M:%S-%d_%m_%Y", time.localtime())
                print("there was a change at ", last_time)
                system("mv buffer.txt save_{}.txt".format(last_time))
            # else:
                # print("there was no change")


        time.sleep(5)


main()
