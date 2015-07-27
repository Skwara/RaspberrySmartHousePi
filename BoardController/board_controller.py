from BoardController.classes.OptionsParser import OptionsParser

options_parser = OptionsParser()

if options_parser.relay_to_switch:
    print("Switching relay {}".format(options_parser.relay_to_switch))

if options_parser.relay_and_value_to_set:
    print("Setting relay {} to {}".format(options_parser.relay_and_value_to_set[0],
                                          options_parser.relay_and_value_to_set[1]))

if options_parser.relay_to_print:
    print("Printing relay {}".format(options_parser.relay_to_print))

if options_parser.print_current_temperature:
    print("Printing current temperature")
