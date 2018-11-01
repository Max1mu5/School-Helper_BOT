# -*- coding: utf-8 -*-
import vk_api
import Schedule.Schedule_10B as S_10B
import HandlerClass
import config
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

TOKEN = config.TOKEN


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, '173305237')

    schedule = S_10B.Schedule10B()
    handler = HandlerClass.Handler(vk_session, schedule)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            handler.curr_lesson(event, event.obj.text)
        elif event.type == VkBotEventType.WALL_POST_NEW:
            print(event.obj.text)
        else:
            print(event.type)
            print()


if __name__ == '__main__':
    main()
