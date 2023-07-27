from Repository.InputHandeling.ParceEventTextFile import ReadEventInputFile
from Repository.Repository import Repository
from Repository.InputHandeling.ParceParticipantTextFile import  ReadParticipantInputFile
from Services.EventServices import EventServices
from Services.ParticipanServices import ParticipantServices
from UI.GeneralUI import GeneralUI

"""
Project: SDB Evaluation 2023
Author: Matei Coldea
Details:
- Are file repository in care se pot vedea modificari pe parcursul operatiilor
- Are Qr code generator(QR code-ul se salveaza sub forma de .jpg in folderul proiectului, dupa terminarea rularii programului)
- Are Basic Input Validation
"""

try:
    # Reading the InputFiles
    event_list = []
    ReadEventInputFile.read_file(event_list)
    participant_list = []
    ReadParticipantInputFile.read_file(participant_list)

    # Creating the Repos
    event_repo = Repository(event_list)
    participant_repo = Repository(participant_list)

    # Creating the Services
    event_services = EventServices(event_repo)
    participants_services = ParticipantServices(participant_repo)

    # Initializing the UI
    interface = GeneralUI(event_services, participants_services)
    interface.run()
except Exception as ex:
    print("\n", ex)
