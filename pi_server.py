from servomotor import Servomotor
from socket import *
from enum import IntEnum
from time import sleep
import RPi.GPIO as GPIO


class DoorCommand(IntEnum):
    DOWN = 1
    UP = 2


def main():
    servo = Servomotor()
    host = ''
    port = 21567
    buffer_size = 1  # read 1 byte max at a time
    address = (host, port)
    tcp_ser_sock = socket(AF_INET, SOCK_STREAM)

    try:
        tcp_ser_sock.bind(address)
        tcp_ser_sock.listen(5)
        print('Waiting for connection')
        tcp_cli_sock, addr = tcp_ser_sock.accept()
        print('...connected from :', addr)
        while True:
            data = tcp_cli_sock.recv(buffer_size)
            print('read ' + data)
            if not data:
                break
            try:
                door_cmd = DoorCommand(int(data))  # 1 / 2
            except (KeyError, ValueError):
                print('Data invalid: ' + data)
                break
            else:
                if door_cmd == DoorCommand.UP:
                    servo.ServoUp()
                if door_cmd == DoorCommand.DOWN:
                    servo.ServoDown()
    except Exception as e:
        print(e)
    finally:
        print('cleaning up..')
        tcp_ser_sock.close()
        servo.close()


if __name__ == '__main__':
    main()
