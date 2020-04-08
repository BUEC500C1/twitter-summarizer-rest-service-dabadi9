from flask import Flask, send_file
from flask_restful import Resource, Api
import threads

calls = -1

application = Flask(__name__)


@application.route('/getvideo')
def get_video():
    return send_file("media/video/video.mp4")


@application.route('/gettext/<string:handle>')
def get(handle):
    global calls
    calls += 1

    t_id = calls % threads.MAX_THREADS
    threads.producer(handle, t_id)

    if calls == 0:
        threads.thread_init()
    while True:
        if (threads.done[t_id] == 1):
            threads.done[t_id] = 0
            return send_file("media/thread%s/text.txt" % str(t_id))


if __name__ == '__main__':
    application.run()
