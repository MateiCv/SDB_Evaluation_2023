class Participant:
    def __init__(self,name,picture_link,enrolled_events:str):
        self._name=name
        self._picture_link=picture_link
        self._enrolled_events=enrolled_events

    def get_name(self):
        return self._name

    def get_picture_link(self):
        return self._picture_link

    def get_enrolled_events(self):
        return self._enrolled_events

    def add_new_event(self,event_id):
        self._enrolled_events += ","+event_id

    def get_printable_instance(self):
        return "{0} {1}".format(self._name,self._picture_link)

    def __str__(self):
        return "{0} {1} {2}\n".format(self._name,self._picture_link,self._enrolled_events)
