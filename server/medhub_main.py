from flask import Flask
import os


path = ""
app = Flask(__name__, static_folder=path)


def main():
    app.run(port="8080", host='0.0.0.0', threaded=True)


@app.route('/<path:path>')
def regulat_http(path):
    return app.send_static_file( path )


@app.route('/stories', methods=['GET'])
def get_user_stories():
    pass
    # idx = request.args.get('idx', default=-999, type=int)
    # ltime = request.args.get('lTime', default=0, type=float)
    # if idx == -999:
    #     return monitor_all()
    # else:
    #     return monitor_device(idx, ltime)
    # pass


# @app.route('/stories', methods=['POST'])
# @app.route('/stories', methods=['Put']))

if __name__ == "__main__":
    main()