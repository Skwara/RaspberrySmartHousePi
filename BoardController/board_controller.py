from BoardController.classes.BoardController import BoardController
from BoardController.classes.OptionsParser import OptionsParser

options_parser = OptionsParser()

if options_parser.relay_to_switch:
    BoardController.switch_relay(options_parser.relay_to_switch)

if options_parser.relay_and_value_to_set:
    BoardController.set_relay(options_parser.relay_and_value_to_set[0], options_parser.relay_and_value_to_set[1])

if options_parser.relay_to_print:
    BoardController.get_relay(options_parser.relay_to_print)

if options_parser.current_temperature:
    BoardController.get_current_temperature()

if options_parser.time_interval_temperature:
    BoardController.get_time_interval_temperature(options_parser.time_interval_temperature[0],
                                                  options_parser.time_interval_temperature[1])
