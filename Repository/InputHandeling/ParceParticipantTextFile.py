from Domain.Participant import Participant
import os
class ReadParticipantInputFile:

    def read_file(entity_list:list):
        if os.path.getsize("Input/ParticipantList.txt") > 0:
            file = open("Input/ParticipantList.txt", "r")
            for line in file:
                if line.strip():
                    parced_input = line.split(" ")
                    new_entity = Participant(str(parced_input[0]).strip(), str(parced_input[1]).strip(), str(parced_input[2]).strip())
                    entity_list.append(new_entity)
        else:
            raise Exception("No Participant Input Data")
