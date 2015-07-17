from BoardController.classes.OptionsParser import OptionsParser

options_parser = OptionsParser()

if options_parser.relay_to_switch is not None:
    print("Switching relay {}".format(options_parser.relay_to_switch))

if options_parser.relay_and_value_to_set is not None:
    print("Setting relay {} to {}".format(options_parser.relay_and_value_to_set[0],
                                          options_parser.relay_and_value_to_set[1]))

if options_parser.relay_to_print is not None:
    print("Printing relay {}".format(options_parser.relay_to_print))
