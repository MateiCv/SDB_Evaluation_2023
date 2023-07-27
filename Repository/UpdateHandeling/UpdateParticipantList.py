class UpdateParticipants:

    def update_participant_list(participant_repo:list):
        f = open("Input/ParticipantList.txt", "w")
        for x in participant_repo.get_all():
            f.write(str(x))
        f.close()
