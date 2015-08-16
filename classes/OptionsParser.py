import argparse

from classes.Constants import Constants


class ValidateSetRelay(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        relay, state = values
        if relay not in Constants.relays:
            args = {'value': relay, 'choices': ', '.join(map(repr, Constants.relays))}
            msg = "invalid choice: %(value)r (choose from %(choices)s)"
            raise argparse.ArgumentError(self, msg % args)
        if state not in Constants.relay_states:
            args = {'value': state, 'choices': ', '.join(map(repr, Constants.relay_states))}
            msg = "invalid choice: %(value)r (choose from %(choices)s)"
            raise argparse.ArgumentError(self, msg % args)
        setattr(namespace, self.dest, [relay, state])


class OptionsParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--switch_relay", nargs=1, type=int, choices=Constants.relays,
                            help="Switches specified relay state", metavar="RELAY")
        parser.add_argument("--set_relay", action=ValidateSetRelay, nargs=2, type=int,
                            help="Sets specified relay state", metavar=("RELAY", "STATE"))
        parser.add_argument("--get_relay", nargs=1, type=int, choices=Constants.relays,
                            help="Prints specified relay state", metavar="RELAY")
        parser.add_argument("--get_current_temperature", action="store_true",
                            help="Prints current temperature")
        parser.add_argument("--get_time_interval_temperature", nargs=2, type=int,
                            help="Prints temperature for specified time interval", metavar=("FROM", "TO"))
        parser.add_argument("--get_last_period_temperature", nargs=1, choices=Constants.last_periods,
                            help="Prints temperatures for specified period", metavar="PERIOD_STRING")
        parser.add_argument("--save_temperature", action="store_true",
                            help="Saves current temperature to database")
        parser.add_argument("--readable_timestamps", "-r", action="store_true",
                            help="Displays timestamps in a readable form")
        self.arguments = parser.parse_args()

    @property
    def relay_to_switch(self):
        return self.arguments.switch_relay

    @property
    def relay_and_value_to_set(self):
        return self.arguments.set_relay

    @property
    def relay_to_print(self):
        return self.arguments.get_relay

    @property
    def current_temperature(self):
        return self.arguments.get_current_temperature

    @property
    def time_interval_temperature(self):
        return self.arguments.get_time_interval_temperature

    @property
    def last_period_temperature(self):
        return self.arguments.get_last_period_temperature

    @property
    def save_temperature(self):
        return self.arguments.save_temperature

    @property
    def readable_timestamps(self):
        return self.arguments.readable_timestamps
