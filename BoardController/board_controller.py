from BoardController.classes.OptionsParser import OptionsParser

options_parser = OptionsParser()

if options_parser.relay_to_switch:
    print("Switching relay {}".format(options_parser.relay_to_switch))

if options_parser.relay_and_value_to_set:
    print("Setting relay {} to {}".format(options_parser.relay_and_value_to_set[0],
                                          options_parser.relay_and_value_to_set[1]))

if options_parser.relay_to_print:
    print("Printing relay {}".format(options_parser.relay_to_print))

if options_parser.current_temperature:
    print("Printing current temperature")

if options_parser.time_interval_temperature:
    print("Printing time interval temperature from {} to {}".format(options_parser.time_interval_temperature[0],
                                                                    options_parser.time_interval_temperature[1]))
