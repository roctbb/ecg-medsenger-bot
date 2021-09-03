import base64

from flask import jsonify
from manage import *
from medsenger_api import AgentApiClient, prepare_file
from helpers import *

medsenger_api = AgentApiClient(API_KEY, MAIN_HOST, AGENT_ID, API_DEBUG)


@app.route('/')
def index():
    return "Waiting for the thunder"


@app.route('/status', methods=['POST'])
@verify_json
def status(data):
    answer = {
        "is_tracking_data": False,
        "supported_scenarios": [],
        "tracked_contracts": []
    }

    return jsonify(answer)


@app.route('/init', methods=['POST'])
@verify_json
def init(data):
    return "ok"


@app.route('/remove', methods=['POST'])
@verify_json
def remove(data):
    return "ok"


# settings and views
@app.route('/settings', methods=['GET'])
@verify_args
def get_settings(args, form):
    return "Этот интеллектуальный агент не требует настройки."


@app.route('/message', methods=['POST'])
@verify_json
def message(data):
    return "ok"

@app.route('/parse', methods=['POST'])
@verify_args
def parse(args, data):
    data = request.json

    print(data)

    medsenger_api.send_message(args.get('contract_id'), "ЭКГ", need_answer=True, send_from='patient', attachments=[prepare_file("files/example.pdf")])

    return "ok"


if __name__ == "__main__":
    app.run(HOST, PORT, debug=API_DEBUG)
