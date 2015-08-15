from classes.BoardController import BoardController
from classes.OptionsParser import OptionsParser

options_parser = OptionsParser()

if options_parser.relay_to_switch:
    BoardController.switch_relay(options_parser.relay_to_switch[0])

if options_parser.relay_and_value_to_set:
    BoardController.set_relay(options_parser.relay_and_value_to_set[0], options_parser.relay_and_value_to_set[1])

if options_parser.relay_to_print:
    print(BoardController.get_relay(options_parser.relay_to_print[0]))

if options_parser.current_temperature:
    print(BoardController.get_current_temperature())

if options_parser.time_interval_temperature:
    BoardController.get_time_interval_temperature(options_parser.time_interval_temperature[0],
                                                  options_parser.time_interval_temperature[1])
