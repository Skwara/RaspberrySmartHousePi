from subprocess import call, check_output

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
        temp_output = str(check_output(["python", "scripts/tmp.py"], universal_newlines=True)).replace("\n", "")
        return temp_output

    @staticmethod
    def get_time_interval_temperature(from_timestamp, to_timestamp):
        print("Printing time interval temperature from {} to {}".format(from_timestamp, to_timestamp))
