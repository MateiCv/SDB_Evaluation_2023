class UpdateEvents:

    def update_event_list(event_repo:list):
        f = open("Input/EventsList.txt", "w")
        for x in event_repo.get_all():
            f.write(str(x))
        f.close()
