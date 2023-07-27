from UI.ParticipantMode.ParticipantUILogic import ParticipantUILogic
from UI.UiUtils.UiUtils import UiUtils


class ParticipantUI:
    def __init__(self,event_services, participant_services):
        self._event_service=event_services
        self._participant_services= participant_services


    def run(self):
        while True:  # meniul
            self.__print_menu()
            participant_input_handeling = ParticipantUILogic(self._event_service,self._participant_services)
            command = input(">")
            try:
                if command == "0":
                    return
                if command == "1":
                    participant_input_handeling.participant_task_1()
                if command == "2":
                    participant_input_handeling.participant_task_2()
                if command == "3":
                    participant_input_handeling.participant_task_3()
                if command == "4":
                    participant_input_handeling.participant_task_4()
            except Exception as ex:
                print("\n", ex)



    def __print_menu(self):
        ui_utils = UiUtils()
        ui_utils.print_separator()
        print("\nParticipant Mode\n"
              "Options:\n\n"
              "1 - Print All Events\n"
              "2 - Sign Up To Event\n\n"
              "3 - Print Events That Start Next Week\n"
              "4 - Print Events That Start In A Specific Month\n"
              "0 - Exit\n")
