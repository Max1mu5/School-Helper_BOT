class Handler:
    def __init__(self, session, schedule):
        self.vk_session = session
        self.schedule = schedule

    def curr_lesson(self, event, str):
        if str.lower() == 'понедельник':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['monday']}
                              )
        elif str.lower() == 'вторник':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['tuesday']}
                              )
        elif str.lower() == 'среда':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['wednesday']}
                              )
        elif str.lower() == 'четверг':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['thursday']}
                              )
        elif str.lower() == 'пятница':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['friday']}
                              )
        elif str.lower() == 'суббота':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['saturday']}
                              )
