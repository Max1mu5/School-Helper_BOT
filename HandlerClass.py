import vk_api
from vk_api.utils import get_random_id

class Handler:
    def __init__(self, session, schedule):
        self.vk_session = session
        self.schedule = schedule

    def curr_lesson(self, event, str):
        randomid = vk_api.utils.get_random_id()
        if 'понедельник' in str.lower():
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['monday'], 'random_id': randomid}
                              )
        elif 'вторник' in str.lower():
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['tuesday'], 'random_id': randomid}
                              )
        elif 'среда' in str.lower():
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['wednesday'], 'random_id': randomid}
                              )
        elif 'четверг' in str.lower():
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['thursday'], 'random_id': randomid}
                              )
        elif 'пятница' in str.lower():
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['friday'], 'random_id': randomid}
                              )
        elif 'суббота' in str.lower():
            self.vk_session.method('messages.send',
                              {'peer_id': event.obj.from_id, 'message': self.schedule.lessons['saturday'], 'random_id': randomid}
                              )
        elif 'сайт школы' in str.lower() or 'школьный сайт' in str.lower():
            self.vk_session.method('messages.send',
                                   {'peer_id': event.obj.from_id, 'message': 'Официальный сайт школы - http://kursk-sosh7.ru/',
                                    'random_id': randomid}
                                   )
        elif 'помощь' in str.lower() or 'справка' in str.lower():
            self.vk_session.method('messages.send',
                                   {'peer_id': event.obj.from_id,
                                    'message': 'Привет! У Этого бота есть несколько команд: \n 1. Напиши любой день недели и он прилет тебе расписание \n 2. Напиши Сайт школы или школьный сайт и ты попадешь на главную страницу официального сайта школы \n 3. Напиши Автор и можешь связаться с создателем этого бота.',
                                    'random_id': randomid}
                                   )
        elif 'автор' in str.lower():
            self.vk_session.method('messages.send',
                                   {'peer_id': event.obj.from_id,
                                    'message': 'Привет! Можешь написать мне тут - https://vk.com/serper8',
                                    'random_id': randomid}
                                   )
        else:
            self.vk_session.method('messages.send',
                                   {'peer_id': event.obj.from_id,
                                    'message': 'Я не понял тебя :( Напиши Помощь и увидишь список доступных комманд',
                                    'random_id': randomid}
                                   )