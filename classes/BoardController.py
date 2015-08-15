from subprocess import call, check_output
import sys

from classes.Constants import Constants


class BoardController:
    @staticmethod
    def switch_relay(relay):
        BoardController.set_relay(relay, not BoardController.get_relay(relay))

    @staticmethod
    def set_relay(relay, value):
        call(["gpio", "-g", "write", str(Constants.relay_ports[relay][0]), str(int(value))])
        call(["gpio", "-g", "write", str(Constants.relay_ports[relay][1]), str(int(value))])
        call(["gpio", "-g", "write", str(Constants.relay_ports[relay][2]), str(int(not value))])

    @staticmethod
    def get_relay(relay):
        call(["gpio", "-g", "mode", str(Constants.relay_ports[relay][0]), "out"])
        call(["gpio", "-g", "mode", str(Constants.relay_ports[relay][1]), "out"])
        call(["gpio", "-g", "mode", str(Constants.relay_ports[relay][2]), "out"])
        state = int(str(check_output(["gpio", "-g", "read",
                                     str(Constants.relay_ports[relay][0])],
                                     universal_newlines=True)).replace("\n", ""))
        return state

    @staticmethod
    def get_current_temperature():
        raw_output = check_output(["python", sys.path[0] + "/scripts/tmp.py"], universal_newlines=True)
        output = str(raw_output).replace("\n", "")
        return output.split(" ")
