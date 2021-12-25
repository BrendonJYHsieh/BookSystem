class Participant:
    email = ""
    events = [] #pointer to event
    def __init__(self,_email) -> None:
        self.email = _email
        self.events = []
        pass
    def get_events(self):
        return self.events
    def event_overlap(self,eventA,eventB):
        if eventB.start_time > eventA.start_time:
            if eventB.start_time >= eventA.end_time:
                return False
            else:
                return True
        elif eventB.start_time < eventA.start_time:
            if eventB.end_time <= eventA.start_time:
                return False
            else:
                return True
        else: #eventB.start_time == eventA.start_time
            return True

    def available_event(self,event):
        for i in range(len(self.events)):
            if self.events[i].start_time >= event.start_time:
                if not self.event_overlap(event,self.events[i]):
                    return True
                else:
                    return False
        return True
    def add_event(self,new_event):
        for i in range(len(self.events)):
            if self.events[i].start_time >= new_event.start_time:
                if not self.event_overlap(new_event,self.events[i]):
                    self.events.insert(i,new_event)
                    return True
                else:
                    return False
        self.events.append(new_event)
        return True
    def delete_event(self,event_id):
        for i in range(len(self.events)):
            if self.events[i].id == event_id:
                del self.events[i]
                return