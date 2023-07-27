from Domain.Event import Event
import random
from datetime import date, datetime
from Repository.UpdateHandeling.UpdateEventList import UpdateEvents
import qrcode


class EventServices:

        def __init__(self, event_repository):
            self._event_repository= event_repository


        #Public Functions
        def add_event(self, title, city, number_of_participants, max_spots, start_date,finish_date,website):
            """"
            Function that adds a new event
            """
            self._event_repository.add(Event(self.__id_randomizer(),str(title),str(city),int(number_of_participants),int(max_spots),start_date,finish_date,website))
            UpdateEvents.update_event_list(self._event_repository)

        def delete_event(self, id):
            """"
            Function that deletes a event
            """
            self._event_repository.delete(Event(int(id)))
            UpdateEvents.update_event_list(self._event_repository)

        def modify_event(self, id_initial, new_title, new_city, new_number_of_participants, new_max_spots, new_start_date,new_finish_date,new_website):
            """"
            Function that modifys a event
            Uses: __find_event_by_id helper function to get the id of the desired event
            """
            modifiable_event = self.__find_event_by_id(id_initial)
            if modifiable_event is None:
                raise Exception("Does not exist!")
            else:
                self._event_repository.modify(modifiable_event,
                                            Event(int(id_initial),new_title,new_city,new_number_of_participants,new_max_spots,new_start_date,new_finish_date,new_website))
                UpdateEvents.update_event_list(self._event_repository)

        def get_all_events(self):
            return self._event_repository.get_all()

        def get_all_events_with_participants(self):
            """"
            Function that returns all events with participants
            """
            event_list = self._event_repository.get_all()
            events_with_participants =[]
            for x in event_list:
                if x.get_number_of_participants() != 0:
                    events_with_participants.append(x)
            events_with_participants.sort(reverse=True, key=self.__sorting_by_number_of_participants)
            return events_with_participants


        def get_events_from_city(self,city_for_search):
            """"
            Function that returns all the events that are based in a city
            """
            event_list= self._event_repository.get_all()
            events_from_city= []
            for x in event_list:
                if str(x.get_city())== city_for_search:
                    events_from_city.append(x)

            if not events_from_city:
                raise Exception("Does not exist!")
            else:
                return events_from_city

        def increment_number_of_participants(self,id):
            """"
            Function that increments the number of participants of an event
            It is used for the sign up process
            """
            target_event = self.__find_event_by_id(id)
            target_event.increment_number_of_participants()
            UpdateEvents.update_event_list(self._event_repository)

        def available_for_enrollement(self,id):
            """"
            Function that checks if a event still has available spots
            """
            target_event = self.__find_event_by_id(id)
            return target_event.get_number_of_participants() < target_event.get_max_spots()

        def get_events_that_start_next_week(self):
            """"
            Function that return events that start next week (next 1 to 7 days)
            """
            event_list = self._event_repository.get_all()
            events_from_next_week = []
            for x in event_list:
                if self.__check_start_date_is_next_week(x.get_start_date()):
                    events_from_next_week.append(x)
            if not events_from_next_week:
                raise Exception("Does not exist!")
            else:
                events_from_next_week.sort(reverse=False, key=self.__sorting_by_max_spots)
                return events_from_next_week

        def get_event_that_starts_in_a_specific_month(self,month):
            """"
            Function that return the events that start in a specific month
            """
            event_list = self._event_repository.get_all()
            events_from_next_week = []
            for x in event_list:
                if self.__check_if_start_date_is_in_specific_month(month,x.get_start_date()):
                    events_from_next_week.append(x)
            if not events_from_next_week:
                raise Exception("Does not exist!")
            else:
                events_from_next_week.sort(reverse=True, key=self.__sorting_by_event_length)
                return events_from_next_week

        def get_qr_code(self,id):
            """"
            Function that creates the QR code for the website of the event passed by id
            """
            target_event = self.__find_event_by_id(id)
            img=qrcode.make(str(target_event.get_website()))
            img.save(target_event.get_title()+".jpg")


        # Helper Functions
        def __sorting_by_number_of_participants(self,entity):
            return int(entity.get_number_of_participants())

        def __check_start_date_is_next_week(self,start_date):
            today = date.today()
            date_object = datetime.strptime(start_date, '%d.%m.%Y').date()
            return 1<=(date_object-today).days <=7

        def __check_if_start_date_is_in_specific_month(self,month,start_date):
            event_month = datetime.strptime(start_date, '%d.%m.%Y').date().month
            return int(event_month) == int(month)

        def __sorting_by_max_spots(self,entity):
            return entity.get_max_spots()

        def __sorting_by_event_length(self,entity):
            start_date = datetime.strptime(str(entity.get_start_date()).strip(), "%d.%m.%Y").date()
            finish_date = datetime.strptime(str(entity.get_finish_date()).strip(), "%d.%m.%Y").date()
            return (finish_date-start_date).days

        def __id_randomizer(self):
            event_list = self._event_repository.get_all()
            while (True):
                id_event = random.randint(0, 10000000)
                for events in event_list:
                    if events.get_id() != id_event:
                        return int(id_event)

        def __find_event_by_id(self, id):
            self.__check_id_validity(id)
            content = self._event_repository.get_all()
            for i in range(len(content)):
                if int(content[i].get_id()) == int(id):
                    return content[i]
            raise Exception("Does Not Exist!")


        def __check_id_validity(self,id):
            if not id.isnumeric():
                raise Exception("Invalid ID")
