from Repository.InputValidation.InputValidation import InputValidation


class ParticipantUILogic:
    def __init__(self,event_services,participant_services):
        self._event_services=event_services
        self._participant_services=participant_services


    def participant_task_1(self):
        """"
        Function that prints the all the events from the available events on screen
        Uses: Event Services Functions
        """
        print("Event List:")
        for x in self._event_services.get_all_events():
            print(x,end="")


    def participant_task_2(self):
        """"
        Function that signs up someone to an event, passed by id
        1. If the event does not have any more spots, a exception is raised
        2. If a participant signs up for the first time to an event, a new Participant entity will be added to the Participants Repo(and Participants File)
        3. If it does not sign up for the first time, the event id is added to the enrolled_events field tied to that specific participant (changes in repo and Participants File)
        4. The number of participant for that event is incremented
        """
        event_id = input("Pass Id: ")
        InputValidation.check_id_validity(event_id)
        if(self._event_services.available_for_enrollement(event_id)):
            name_participant=input("Pass name (FirstName-LastName): ")
            if(self._participant_services.check_if_participant_exists(name_participant)):
                self._participant_services.add_new_event(name_participant,event_id)
            else:
                picture_link= input("Pass Picture Link: ")
                self._participant_services.add_participant(name_participant,picture_link,str(event_id))
            self._event_services.increment_number_of_participants(event_id)
        else:
            raise Exception("No More Empty Slots")


    def participant_task_3(self):
        """"
        Function that prints all the events that have the starting date within the nex week
        Uses: Event Services Functions
        """
        print("Event List:")
        for x in self._event_services.get_events_that_start_next_week():
            print(x,end="")

    def participant_task_4(self):
        """"
        Function that prints all the events that have their starting date in a specific month
        Uses: Events Services Functions
        User Input: Month that they want to see the events from (passed to the function as int)
        """
        month = input("Input month:").strip()
        InputValidation.check_month_validity(month)
        print("Event List:")
        for x in self._event_services.get_event_that_starts_in_a_specific_month(int(month)):
            print(x,end="")
