import argparse
from BoardController.classes.Constants import Constants


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
        self.arguments = vars(parser.parse_args())

    @property
    def relay_to_switch(self):
        return self.arguments['switch_relay'][0] if self.arguments['switch_relay'] is not None else None

    @property
    def relay_and_value_to_set(self):
        return self.arguments['set_relay'][0:2] if self.arguments['set_relay'] is not None else None
