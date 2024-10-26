import os
from intelxapi import intelx
from flask import Flask, request


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/info', methods=['GET'])
    def info():
        try:
            url = request.args.get('url')
            limit = request.args.get('limit')
            
            ix = intelx('REPLACE_WITH_YOUR_API_KEY')

            if limit:
                search = ix.search(url, int(limit))
            else:
                search = ix.search(url)

            return {
                'result': search['records']
            }
        except Exception as e:
            return {'error': str(e)}

    return app