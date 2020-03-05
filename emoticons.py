from telebot import types

emote_dict = {'😐': 'ಠ_ಠ',
              '😣': '(>_<)',
              '🙄': '( ⚆ _ ⚆ )',
              '😳': '(⊙＿⊙)',
              '😡': 'ᕙ(˵•̀෴•́˵)ᕗ',
              '🙂': '(ツ)',
              '😒': '(￢_￢)',
              '☹': '(´◕︵◕`)',
              '😄': '^‿^',
              '😍': 'ヽ(♡‿♡)ノ',
              '🤗': '༼ つ ◕_◕ ༽つ',
              '😊': '(◔‿◔)',
              '🤨': '( ͠° ͟ʖ ͡°)',
              '🙋‍♂️': '⊂(◉‿◉)つ',
              'lenny': '( ͡° ͜ʖ ͡°)',
              '🖕': '( ︶︿︶)_╭∩╮',
              'idk': '¯\\_(⊙︿⊙)_/¯', }

emote_buttons = [types.KeyboardButton(emote) for emote in emote_dict.values()]
emote_keyboard = types.ReplyKeyboardMarkup(row_width=3)
emote_keyboard.add(*emote_buttons)

inline_all_results = [types.InlineQueryResultArticle(i, emote, types.InputTextMessageContent(emote)) for i, emote in
                      enumerate(emote_dict.values())]


def get_inline_results(q):
    if q in emote_dict:
        return [types.InlineQueryResultArticle('1', emote_dict[q], types.InputTextMessageContent(emote_dict[q]))]
    else:
        return inline_all_results
