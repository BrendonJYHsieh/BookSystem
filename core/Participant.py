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
        if eventA.id == eventB.id: #update event
            return False
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
        if len(self.events) == 0:
            return True
        for i in range(len(self.events)):
            if self.events[i].start_time >= event.start_time:
                if not self.event_overlap(event,self.events[i]) and not self.event_overlap(event,self.events[i-1]):
                    print("available event")
                    return True
                else:
                    print("not available event")
                    return False
        if not self.event_overlap(event,self.events[-1]):
            print("available event")
            return True
        else:
            print("not available event")
            return False
    def add_event(self,new_event):
        if len(self.events) == 0:
            self.events.append(new_event)
            return True
        for i in range(len(self.events)):
            if self.events[i].start_time >= new_event.start_time:
                if not self.event_overlap(new_event,self.events[i]) and not self.event_overlap(new_event,self.events[i-1]):
                    self.events.insert(i,new_event)
                    return True
                else:
                    print("not available event")
                    return False      
        self.events.append(new_event)
        self.print()
        return True
    def delete_event(self,event_id):
        for i in range(len(self.events)):
            if self.events[i].id == event_id:
                
                del self.events[i]
                self.print()
                return
    def print(self):
        print(self.email + "'s event : ")
        for i in range(len(self.events)):
            print(self.events[i].room.name + "  " + self.events[i].name + "  "+ str(self.events[i].start_time) +"  "+ str(self.events[i].end_time))