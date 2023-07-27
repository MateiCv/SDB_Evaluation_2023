from Domain.Event import Event
import os

class ReadEventInputFile:

    def read_file(entity_list: list):
        if os.path.getsize("Input/EventsList.txt") > 0:
            file = open("Input/EventsList.txt", "r")
            for line in file:
                if line.strip():
                    parced_input = line.split(" ")
                    new_entity = Event(int(parced_input[0].strip()), str(parced_input[1].strip()), str(parced_input[2].strip()), int(parced_input[3].strip()), int(parced_input[4].strip()),
                                parced_input[5].strip(), parced_input[6].strip(),str(parced_input[7].strip()))
                    entity_list.append(new_entity)
        else:
            raise Exception("No Event Input Data")
