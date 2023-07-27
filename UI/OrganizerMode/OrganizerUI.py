from UI.OrganizerMode.OrganizerUILogic import OrganizerUILogic
from UI.UiUtils.UiUtils import UiUtils


class OrganizerUI:
    def __init__(self,event_services, participant_services):
        self._event_service=event_services
        self._participant_services= participant_services



    def run(self):
        while True:
            self.__print_menu()
            organizer_input_handeling = OrganizerUILogic(self._event_service,self._participant_services)
            command = input(">")
            try:
                if command == "0":
                    return
                if command == "1":
                    organizer_input_handeling.organizer_task_1()
                if command == "2":
                    organizer_input_handeling.organizer_task_2()
                if command == "3":
                    organizer_input_handeling.organizer_task_3()
                if command == "4":
                    organizer_input_handeling.organizer_task_4()
                if command == "5":
                    organizer_input_handeling.organizer_task_5()
                if command == "6":
                    organizer_input_handeling.organizer_task_6()
                if command == "7":
                    organizer_input_handeling.organizer_task_7()
                if command == "8":
                    organizer_input_handeling.organizer_task_8()

            except Exception as ex:
                print("\n", ex)

    def __print_menu(self):
        ui_utils = UiUtils()
        ui_utils.print_separator()
        print("\nOrganizer Mode\n"
              "Options:\n\n"
              "1 - Add Event\n"
              "2 - Delete Event\n"
              "3 - Modify Event \n"
              "4 - Print Event List\n\n"
              "5 - Print Event List Form A Specific City\n"
              "6 - Print Participants From Event\n"
              "7 - Print Events That Have Participants\n"
              "8 - Get Website QR Code\n"
              "0 - Exit\n")
