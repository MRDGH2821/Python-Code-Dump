from flask import Flask

from cassandra.cluster import Cluster

cluster = Cluster()

session = cluster.connect()

app = Flask(__name__)
@app.route('/')
def index():
    return session.execute("SELECT release_version FROM system.local").one()
app.run()