from mycroft import MycroftSkill, intent_handler


class ijs(MycroftSkill):
    @intent_handler('do.you.like.intent')
    def handle_do_you_like(self):
        likes_ice_cream = self.ask_yesno('do.you.like.ice.cream')
        if likes_ice_cream == 'yes':
            self.speak_dialog('does.like')
        elif likes_ice_cream == 'no':
            self.speak_dialog('does.not.like')
        else:
            self.speak_dialog('could.not.understand')


def create_skill():
    return ijs()
