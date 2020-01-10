#! /usr/bin/env python

import logging
import os
import time
import socket

from .urscript import URScript

# Gripper Variables
ACT = "ACT"
GTO = "GTO"
ATR = "ATR"
ARD = "ARD"
FOR = "FOR"
SPE = "SPE"
OBJ = "OBJ"
STA = "STA"
FLT = "FLT"
POS = "POS"

SOCKET_HOST = "127.0.0.1"
SOCKET_PORT = 30003
SOCKET_NAME = "gripper_socket"



class Robotiq85(object):

    def __init__(self,
                 payload=0.85,
                 speed=255,
                 force=50,
                 socket_host=SOCKET_HOST,
                 socket_port=SOCKET_PORT):
        """
        Controller for Robotiq 85 with socket
        lei.zhang@agile-robots.com
        :param payload:
        :param speed:
        :param force:
        :param socket_host:
        :param socket_port:
        """
        self.payload = payload
        self.speed = speed
        self.force = force
        self.socket_host = socket_host
        self.socket_port = socket_port
        self.logger = logging.getLogger(u"robotiq")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.f = open("./Robotiq/test.script", "rb")
        self.s.connect((self.socket_host, self.socket_port))
        l = self.f.read(1024)
        while (l):
            self.s.send(l)
            l = self.f.read(1024)
        self.motion_list = []
        self.max_width = 0.085
        # self.rq_set_force()

    # def rq_set_force(self):
    #     self.motion_list.append("rq_set_force({})".format(str(self.force))+ "\n")

    def rg_activated(self):
        self.motion_list.append("rq_is_gripper_activated()" + "\n")

    def rq_open_and_wait(self):
        self.motion_list.append("rq_open_and_wait()" + "\n")

    def rq_close_and_wait(self):
        self.motion_list.append("rq_close_and_wait()" + "\n")

    def rq_current_pos_mm(self):
        self.motion_list.append("rq_current_pos_mm()" + "\n")

    def rq_move_mm(self, position_mm):

        print "rq_move_norm(%s)" %(str(self.mm_to_norm(position_mm)))+ "\n"
        self.motion_list.append("rq_move_norm(%s)" %(str(self.mm_to_norm(position_mm)))+ "\n")
    #
    def rq_move_norm(self, position_norm):
        print("rq_move_norm(%s)" %(str(position_norm)) + "\n")
        self.motion_list.append("rq_move_norm(%s)" %(str(position_norm)) + "\n")

    def close_socket(self):
        self.f.close()
        self.s.close()

    def mm_to_norm(self, mm):
        return 100 - 100 * mm / self.max_width

    def motion(self):
        for str in self.motion_list:
            self.s.send(str)
        self.s.send("end"+"\n")
        print self.motion_list
        self.close_socket()

    def test_motion(self, motion_list_test = ["rq_open_and_wait()" + "\n", "rq_close_and_wait()" + "\n"]):
        for str in motion_list_test:
            self.s.send(str)
        self.s.send("end"+"\n")
        print motion_list_test
        # self.close_socket()