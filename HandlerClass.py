import vk_api
from vk_api.utils import get_random_id

class Handler:
    def __init__(self, session, schedule):
        self.vk_session = session
        self.schedule = schedule

    def curr_lesson(self, event, str):
        randomid = vk_api.utils.get_random_id()
        if str.lower() == 'понедельник':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['monday'], 'random_id': randomid}
                              )
        elif str.lower() == 'вторник':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['tuesday'], 'random_id': randomid}
                              )
        elif str.lower() == 'среда':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['wednesday'], 'random_id': randomid}
                              )
        elif str.lower() == 'четверг':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['thursday'], 'random_id': randomid}
                              )
        elif str.lower() == 'пятница':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['friday'], 'random_id': randomid}
                              )
        elif str.lower() == 'суббота':
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['saturday'], 'random_id': randomid}
                              )
