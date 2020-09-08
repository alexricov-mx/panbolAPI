from flask.views import MethodView
from my_app import app
from azure.cosmos import CosmosClient,PartitionKey
import json

class PanbolApi(MethodView):
    def get(self):
        # Initialize the Cosmos client
        endpoint = "<uri>"
        key = "<key>"
        
        # <create_cosmos_client>
        client = CosmosClient(endpoint, key)
        # </create_cosmos_client>

        # Create a database
        # <create_database_if_not_exists>
        database_name = 'CosmosDBFutbolapp'
        database = client.create_database_if_not_exists(id=database_name)
        # </create_database_if_not_exists>


        # Create a container
        # Using a good partition key improves the performance of database operations.
        # <create_container_if_not_exists>
        container_name = 'UsuariosContainer'
        container = database.create_container_if_not_exists(
            id=container_name, 
            partition_key=PartitionKey(path="/lastName"),
            offer_throughput=400
        )
        # </create_container_if_not_exists>

        # <create_item>
        records = {
            'id':'1',
            'lastName':'Rico'
            }

        container.create_item(body=records)
        # </create_item>
        
        #la funcion dumps de JSON convierte el texto a un objeto JSON
        return json.dumps(records)
    
    def post(self):
        return

    def put(self,id):
        return
    
    def delete(self,id):
        return
    
panbol_view = PanbolApi.as_view('panbol_view')
app.add_url_rule('/api/panbol/',
view_func=panbol_view,
methods=['GET'])

app.add_url_rule('/api/panbol/<int:id>',
view_func=panbol_view,
methods=['GET','POST','PUT','DELETE'])