import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '535586410:AAHc1x-dOUeBt9c6XugFTzy23REKwazaAd4'
WEBHOOK_URL = 'https://87377d11.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'greeting',
        'rank',
        'player',
        'showEast',
        'showWest',
        'showPlayer',
        'trap'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'greeting',
            'conditions':'is_going_to_greeting'       
        },
        
        {
            'trigger': 'advance',
            'source': 'greeting',
            'dest': 'rank',
            'conditions':'is_going_to_rank'       
        },

        {
            'trigger': 'advance',
            'source': 'greeting',
            'dest': 'player',
            'conditions':'is_going_to_player'       
        },

        {
            'trigger': 'advance',
            'source': 'greeting',
            'dest': 'trap',
            'conditions':'is_going_to_trap'       
        },

        {
            'trigger': 'go_back',
            'source': 'trap',
            'dest': 'greeting'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
