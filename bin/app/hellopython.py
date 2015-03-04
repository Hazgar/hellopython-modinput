#!/usr/bin/env python
#
# Copyright 2013 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys

from splunklib.modularinput import *

class HelloPython(Script):
    """All modular inputs should inherit from the abstract base class Script
    from splunklib.modularinput.script.
    They must override the get_scheme and stream_events functions, and,
    if the scheme returned by get_scheme has Scheme.use_external_validation
    set to True, the validate_input function.
    """
    def get_scheme(self):
        """When Splunk starts, it looks for all the modular inputs defined by
        its configuration, and tries to run them with the argument --scheme.
        Splunkd expects the modular inputs to print a description of the
        input in XML on stdout. The modular input framework takes care of all
        the details of formatting XML and printing it. The user need only
        override get_scheme and return a new Scheme object.

        :return: scheme, a Scheme object
        """
        scheme = Scheme("HelloPython Modular Input")

        scheme.description = "Randomly generate events"
        # If you set external validation to True, without overriding validate_input,
        # the script will accept anything as valid. Generally you only need external
        # validation if there are relationships you must maintain among the
        # parameters, such as requiring min to be less than max in this example,
        # or you need to check that some resource is reachable or valid.
        # Otherwise, Splunk lets you specify a validation string for each argument
        # and will run validation internally using that string.
        scheme.use_external_validation = True
        scheme.use_single_instance = False

        whoareyou_argument = Argument("whoareyou")
        whoareyou_argument.data_type = Argument.data_type_string
        whoareyou_argument.description = "Who are you?"
        whoareyou_argument.required_on_create = True
        whoareyou_argument.required_on_edit = False
        scheme.add_argument(whoareyou_argument)

        whereareyou_argument = Argument("whereareyou")
        whereareyou_argument.data_type = Argument.data_type_string
        whereareyou_argument.description = "Where are you?"
        whereareyou_argument.required_on_create = True
        whereareyou_argument.required_on_edit = False
        scheme.add_argument(whereareyou_argument)
    
        howareyou_argument = Argument("howareyou")
        howareyou_argument.data_type = Argument.data_type_string
        howareyou_argument.description = "How are you?"
        howareyou_argument.required_on_create = False
        howareyou_argument.required_on_edit = False
        scheme.add_argument(howareyou_argument)

        whatisyourfavoritecolor_argument = Argument("whatisyourfavoritecolor")
        whatisyourfavoritecolor_argument.data_type = Argument.data_type_string
        whatisyourfavoritecolor_argument.description = "What is your favorite color?"
        whatisyourfavoritecolor_argument.required_on_create = False
        whatisyourfavoritecolor_argument.required_on_edit = False
        scheme.add_argument(whatisyourfavoritecolor_argument)

        magic_argument = Argument("magic")
        magic_argument.data_type = Argument.data_type_string
        magic_argument.description = "What is the answer to all the question in the universe?"
        magic_argument.required_on_create = True
        magic_argument.required_on_edit = True
        scheme.add_argument(magic_argument)

        return scheme

    def validate_input(self, validation_definition):
        whoareyou = validation_definition.parameters["whoareyou"]
        whereareyou = validation_definition.parameters["whereareyou"]
        howareyou = validation_definition.parameters["howareyou"]
        whatisyourfavoritecolor = validation_definition.parameters["whatisyourfavoritecolor"]
        magic = validation_definition.parameters["magic"]

        if whatisyourfavoritecolor.lower() == "rainbow":
            raise ValueError("%s really ?" % whatisyourfavoritecolor)
        elif magic != "42":
            raise ValueError("%s is not likely to be the answer." % magic)

    def stream_events(self, inputs, ew):
        colormap = {'red': "nervous", 'blue': "cool", 'green': "hippie", 'yellow': "good guy", 'pink': "extravagant"}
        citymap = {'paris': "'s stylish", 'london': " rocks", 'san francisco': "'s nice"}
        moudmap = {'fine': "happy", 'bad': "sad", 'sad': "bad", 'ok': "great", 'good': "super"}  
        for input_name, input_item in inputs.inputs.iteritems():
            whoareyou = input_item["whoareyou"]
            whereareyou = input_item["whereareyou"]
            howareyou = input_item["howareyou"]
            whatisyourfavoritecolor = input_item["whatisyourfavoritecolor"]
            magic = input_item["magic"]

            sentiment = colormap[whatisyourfavoritecolor.lower()] if whatisyourfavoritecolor.lower() in colormap else "zen"
            advise = citymap[whereareyou.lower()] if whereareyou.lower() in citymap else " sucks"
            moud = moudmap[howareyou.lower()] if howareyou.lower() in moudmap else "numb"

            # Create an Event object, and set its fields
            ew.log(input_name, "generate event")
            event = Event()
            event.stanza = input_name
            event.data = "%s must be the %s type as his favorite color is %s and also he lives in %s and that%s. But it seems he's just %s." % (whoareyou, sentiment, whatisyourfavoritecolor, whereareyou, advise, moud)  
            
            # Tell the EventWriter to write this event
            ew.write_event(event)
            ew.log(input_name, "event generated")

if __name__ == "__main__":
    sys.exit(HelloPython().run(sys.argv))
