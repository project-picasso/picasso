import datetime
import logging
import os
import ssl

from flask import Flask
import sqlalchemy
from sqlalchemy.ext.serializer import loads, dumps
import json

from db import db

logger = logging.getLogger()

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Bye {}!".format(name)

@app.route("/all")
def all_art():
    with db.connect() as conn:
        all_art = conn.execute("SELECT * from art_details").fetchall()
    logger.info("Query all art: %s", all_art)
    return json.dumps([dict(r) for r in all_art])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))