class Repository:


    def __init__(self,entities_list):
        self._entitiesList = entities_list

    def find_position(self, entity):

        for i in range(len(self._entitiesList)):
            if self._entitiesList[i] == entity:
                return i
        return -1


    def add(self, entity):

        if self.find_position(entity) != -1:
            raise Exception("Already exists!")
        self._entitiesList.append(entity)

    def delete(self, entity):

        position = self.find_position(entity)
        if position == -1:
            raise Exception("Does not exist!")
        del self._entitiesList[position]

    def get_all(self):

        return self._entitiesList

    def modify(self,entity,newentity):
        position = self.find_position(entity)

        if position == -1:
            raise Exception("Does not exist!")
        self._entitiesList[position]=newentity
