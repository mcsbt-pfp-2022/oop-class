
#%%


class Clock:

    def __init__(self, hours: int, minutes: int):

        if hours not in range(0, 24):
            raise Exception("hours must be 0-23")

        if minutes not in range(0, 60):
            raise Exception("minutes must be 0-59")

        self.hours = hours
        self.minutes = minutes

clock_1 = Clock("potato", 43)
# %%

