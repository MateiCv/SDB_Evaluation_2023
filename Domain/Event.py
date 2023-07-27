class Event:
    # de dat final value in init la toate in afara de id
    def __init__(self, id:int,title:str="",city:str="",number_of_participants=0,max_spots:int=0,start_date="-",finish_date="-",website=""):
        self._id:int = id
        self._title:str=title
        self._city=city
        self._number_of_participants=number_of_participants
        self._max_spots= max_spots
        self._start_date=start_date
        self._finish_date=finish_date
        self._website=website


    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def set_title(self,new_title):
        self._title=new_title

    def get_city(self):
        return self._city

    def set_city(self,new_city):
        self._city = new_city

    def get_number_of_participants(self):
        return self._number_of_participants

    def set_number_of_participants(self,new_number_of_participants):
        self._number_of_participants=new_number_of_participants

    def increment_number_of_participants(self):
        self._number_of_participants= int(self._number_of_participants)+1

    def get_max_spots(self):
        return self._max_spots

    def set_max_spots(self,new_max_spots):
        self._max_spots = new_max_spots

    def get_start_date(self):
        return self._start_date

    def set_start_date(self, new_start_date):
        self._start_date=new_start_date

    def get_finish_date(self):
        return self._finish_date

    def set_finish_date(self,new_finish_date):
        self._finish_date = new_finish_date

    def get_website(self):
        return self._website

    def __eq__(self, event):
        return event.get_id() == self.get_id()

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}\n".format(self._id,self._title,self._city,self._number_of_participants,self._max_spots,self._start_date,self._finish_date,self._website)
