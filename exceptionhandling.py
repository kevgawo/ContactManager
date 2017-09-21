# Mr Todd has bouught Andrew a new weave , so now Mest is on a hiring freeze.
# it can pay only 4 fellows at a time
# >>Use a static field to keep track of how many fellows have been created
# >>If a user tries to construct a fifth Fellow, raise an exception


class MestGhana:
    track_fellows = 0

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

        MestGhana.track_fellows += 1

    def hire_fellow(self):
        if MestGhana.track_fellows < 5:
            print("You just got hired, congradulations")

        else:
            Exception ("Were currently broke to hire {} from {}".format(self.name, self.nationality))

hire_or_fire = MestGhana("Andrew", "USA")
hire_or_fire = MestGhana("Pascal", "DRC")
hire_or_fire = MestGhana("Miishe", "GH/Murika")
hire_or_fire = MestGhana("Simphiwe", "Africa del Sur")
hire_or_fire = MestGhana("Edem", "Ghana")
hire_or_fire = MestGhana("Kerry", "Murika")

hire_or_fire.hire_fellow()