from Domain.Participant import Participant
from Repository.UpdateHandeling.UpdateParticipantList import UpdateParticipants


class ParticipantServices:

    def __init__(self,participants_repository):
        self._participants_repository = participants_repository

    # Public Functions
    def add_participant(self,name,picture_link,enrolled_events):
        """
        Function that adds a participant to the participant repo and Participant File 
        """
        self._participants_repository.add(Participant(name,picture_link,enrolled_events))
        UpdateParticipants.update_participant_list(self._participants_repository)

    def get_participants_from_a_event(self,event_id):
        """
        Function that return the participants from a event
        """
        participant_list =self._participants_repository.get_all()
        event_has_participants: bool = False
        event_participants= []
        for x in participant_list:
            event_participations = self.__parce_event_list(x.get_enrolled_events())
            for event in event_participations:
                if int(event) == int(event_id):
                    event_has_participants=True
                    event_participants.append(x.get_printable_instance())
                    break
        if(not event_has_participants):
            raise Exception("No Participants!")
        else:
            return event_participants

    def check_if_participant_exists(self,name):
        """
        Function that checks if the participant with the name "name" exist in the repo
        It is used for the sign up process
        """
        content = self._participants_repository.get_all()
        for i in range(len(content)):
            if (content[i].get_name() == name):
                return True
        return False

    def add_new_event(self,name,event_id):
        """
        Function that adds a new event to the enrolled events list for a participant
        It is used for the sign up process
        """
        target_participant= self.__find_participant_by_id(name)
        enrolled_events = target_participant.get_enrolled_events()
        if event_id in enrolled_events:
            raise Exception("Already Enrolled!")
        target_participant.add_new_event(event_id)
        UpdateParticipants.update_participant_list(self._participants_repository)


    # Helper Functions
    def __parce_event_list(self,event_list):
        parced_list = str(event_list).split(",")
        event_final_list = []
        for x in parced_list:
            event_final_list.append(int(x))
        return event_final_list

    def __find_participant_by_id(self, name):
        content = self._participants_repository.get_all()
        for i in range(len(content)):
            if content[i].get_name() == name:
                return content[i]
        return None
