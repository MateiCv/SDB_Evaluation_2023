from Repository.InputValidation.InputValidation import InputValidation


class OrganizerUILogic:

    def __init__(self,event_services, participant_services):
        self._event_services=event_services
        self._participant_services=participant_services

    def organizer_task_1(self):
        """"
        Function that adds an event to the event_repo and to the DT file
        Uses: Event Services Functions
        User Input: Details for the newly added event
        """
        title=input("Pass Title: ")
        InputValidation.check_word_validation(title)
        city=input("Pass City: ")
        InputValidation.check_city_validation(city)
        number_of_participants= input("Pass Number Of Participants: ")
        InputValidation.check_numeric_value_validation(number_of_participants)
        max_spots= input("Pass Max Number Of Participants: ")
        InputValidation.check_numeric_value_validation(max_spots)
        start_date= input("Pass Start Date (d.m.Y): ")
        InputValidation.check_date_validity(start_date)
        finish_date= input("Pass Finish Date (d.m.Y): ")
        InputValidation.check_date_validity(finish_date)
        website= input("Pass Website: ")
        InputValidation.check_website_validity(website)
        self._event_services.add_event(title,city,number_of_participants,max_spots,start_date,finish_date,website)


    def organizer_task_2(self):
        """"
        Function that deletes an event from the event_repo and the DT file
        Uses: Event Services Functions
        User Input: ID of the event to be deleted
        """
        Id = input("Pass Id To Delete: ")
        self._event_services.delete_event(Id)

    def organizer_task_3(self):
        """"
        Function that gets the input and modifys an event passed through ID
        Uses: InputValidation class for validating the input
        User Input: Event fields
        """
        Id=input("Pass Id To Modify: ")
        InputValidation.check_id_validity(Id)
        title = input("Pass New Title: ")
        InputValidation.check_word_validation(title)
        city = input("Pass New City: ")
        InputValidation.check_city_validation(city)
        number_of_participants = input("Pass New Number Of Participants: ")
        InputValidation.check_numeric_value_validation(number_of_participants)
        max_spots = input("Pass New Max Number Of Participants: ")
        InputValidation.check_numeric_value_validation(max_spots)
        start_date = input("Pass New Start Date (d.m.Y): ")
        InputValidation.check_date_validity(start_date)
        finish_date = input("Pass New Finish Date (d.m.Y): ")
        InputValidation.check_date_validity(finish_date)
        website= input("Pass New Website: ")
        InputValidation.check_website_validity(website)
        self._event_services.modify_event(Id,title, city, number_of_participants, max_spots, start_date, finish_date,website)

    def organizer_task_4(self):
        """"
        Function that prints all the events
        """
        print("Event List: ")
        for x in self._event_services.get_all_events():
            print(x, end="")

    def organizer_task_5(self):
        """"
        Function that prints all the events from a specific city(passed by user)
        Uses: InputValidation class for validating the input
        """
        city= input("Pass city: ")
        InputValidation.check_city_validation(city)
        print("Event List: ")
        for x in self._event_services.get_events_from_city(city):
            print(x, end="")

    def organizer_task_6(self):
        """"
        Function that prints all the participants from an event
        Uses: InputValidation class for validating the input
        """
        event_id= input("Event ID: ")
        InputValidation.check_id_validity(event_id)
        event_participants= self._participant_services.get_participants_from_a_event(event_id)
        for x in event_participants:
            print(x)

    def organizer_task_7(self):
        """"
        Function that prints events that have participants
        """
        print("Event List: ")
        for x in self._event_services.get_all_events_with_participants():
            print(x, end="")

    def organizer_task_8(self):
        """"
        Function that saves a QR code for the website of an event(passed through ID by the user)
        OBS: It appears after runtime ends
        """
        event_id = input("Event ID: ")
        InputValidation.check_id_validity(event_id)
        self._event_services.get_qr_code(event_id)
