from telebot import types

emote_dict = {'😐': 'ಠ_ಠ',
              '😣': '(>_<)',
              '🙄': '(◔_◔)',
              '😌': '<(￣︶￣)>',
              '😞': '╯ˍ╰',
              '🙂': '(ツ)',
              '🤔': '¯\\_(⊙︿⊙)_/¯',
              '😒': '(￢_￢)',
              '😊': '^̮ ^',
              '😍': 'ヽ(♡‿♡)ノ',
              '🤗': '༼ つ ◕_◕ ༽つ',
              '😄': '(¬‿¬)',
              '🤨': '( ͠° ͟ʖ ͡°)',
              '🙋‍♂️': '⊂(◉‿◉)つ',
              'lenny': '( ͡° ͜ʖ ͡°)',
              '🖕': '( ︶︿︶)_╭∩╮',
              'lennies': '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)'}

emote_buttons = [types.KeyboardButton(emote) for emote in emote_dict.values()]
emote_keyboard = types.ReplyKeyboardMarkup(row_width=3)
emote_keyboard.add(*emote_buttons)
