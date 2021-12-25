class Participant:
    email = ""
    events = [] #pointer to event
    def __init__(self) -> None:
        self.events = []
        pass
    def get_events(self):
        return self.events
    def add_event(self,event):
        self.events.append(event)
        return
    def delete_event(self):
        for i in range(len(self.events)):
            if self.events[i] == None:
                del self.events[i]
                i-=1
                