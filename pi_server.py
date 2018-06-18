from servomotor import Servomotor
from socket import *
from enum import IntEnum
from time import sleep
import RPi.GPIO as GPIO


class DoorCommand(IntEnum):
    UP = 1
    DOWN = 2


def main():
    servo = Servomotor()
    host = ''
    port = 21567
    buffer_size = 1024
    address = (host, port)
    tcp_ser_sock = socket(AF_INET, SOCK_STREAM)
    tcp_ser_sock.bind(address)
    tcp_ser_sock.listen(5)

    print('Waiting for connection')
    tcp_cli_sock, addr = tcp_ser_sock.accept()
    print('...connected from :', addr)

    try:
        while True:
            sleep(3)
            data = tcp_cli_sock.recv(buffer_size)
            if not data:
                break
            try:
                door_cmd = DoorCommand(data)
            except KeyError:
                break
            else:
                if door_cmd == DoorCommand.UP:
                    servo.ServoUp()
                    print('Increased to: ', servo.cur_X)
                if door_cmd == DoorCommand.DOWN:
                    servo.ServoDown()
                    print('Decreased to: ', servo.cur_X)
    except KeyboardInterrupt:
        servo.close()
        GPIO.cleanup()
        tcp_ser_sock.close()


if __name__ == '__main__':
    main()
