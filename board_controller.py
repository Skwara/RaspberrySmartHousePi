from datetime import datetime

from classes.BoardController import BoardController
from classes.DatabaseHandler import DatabaseHandler
from classes.OptionsParser import OptionsParser


def print_temperature(temp_struct):
    if options_parser.readable_timestamps:
        print("{:<7} {}".format(temp_struct[0],
                                datetime.fromtimestamp(float(temp_struct[1])).strftime("%H:%M %Y-%m-%d")))
    else:
        print("{} {}".format(temp_struct[0], temp_struct[1]))


options_parser = OptionsParser()

if options_parser.relay_to_switch:
    BoardController.switch_relay(options_parser.relay_to_switch[0])

if options_parser.relay_and_value_to_set:
    BoardController.set_relay(options_parser.relay_and_value_to_set[0], options_parser.relay_and_value_to_set[1])

if options_parser.relay_to_print:
    print(BoardController.get_relay(options_parser.relay_to_print[0]))

if options_parser.current_temperature:
    temp = BoardController.get_current_temperature()
    print_temperature(temp)

if options_parser.time_interval_temperature:
    database_handler = DatabaseHandler()
    temp_tab = database_handler.get_time_interval_temperature(options_parser.time_interval_temperature[0],
                                                              options_parser.time_interval_temperature[1])
    for temp in temp_tab:
        print_temperature(temp)

if options_parser.last_period_temperature:
    database_handler = DatabaseHandler()
    temp_tab = database_handler.get_last_period_temperature(options_parser.last_period_temperature[0],
                                                            options_parser.without_filling)
    for temp in temp_tab:
        print_temperature(temp)

if options_parser.save_temperature:
    temp = BoardController.get_current_temperature()
    database_handler = DatabaseHandler()
    database_handler.save_temperature(temp[0], temp[1])
