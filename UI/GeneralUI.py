from UI.OrganizerMode.OrganizerUI import OrganizerUI
from UI.ParticipantMode.ParticipantUI import ParticipantUI
from UI.UiUtils.UiUtils import UiUtils

class GeneralUI:
    def __init__(self, event_sevice, participant_service):
        self._event_sevice = event_sevice
        self._participant_service = participant_service

    def run(self):
        while True:
            self.__print_manu()
            command = input(">")
            try:
                if command == "0":
                    return
                if command == "1":
                    interface= OrganizerUI(self._event_sevice , self._participant_service )
                    interface.run()
                if command == "2":
                    interface= ParticipantUI(self._event_sevice , self._participant_service)
                    interface.run()
            except Exception as ex:
                print("\n", ex)

    def __print_manu(self):
        ui_utils = UiUtils()
        ui_utils.print_separator()
        print("\nChoose Mode\n\n"
              "Options:\n\n"
              "1 - Organizer Mode\n"
              "2 - Participant Mode\n"
              "0 - Exit\n")
