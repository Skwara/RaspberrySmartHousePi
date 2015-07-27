class BoardController:
    @staticmethod
    def switch_relay(relay):
        print("Switching relay {}".format(relay))

    @staticmethod
    def set_relay(relay, value):
        print("Setting relay {} to {}".format(relay, value))

    @staticmethod
    def get_relay(relay):
        print("Printing relay {}".format(relay))

    @staticmethod
    def get_current_temperature():
        print("Printing current temperature")

    @staticmethod
    def get_time_interval_temperature(from_timestamp, to_timestamp):
        print("Printing time interval temperature from {} to {}".format(from_timestamp, to_timestamp))
