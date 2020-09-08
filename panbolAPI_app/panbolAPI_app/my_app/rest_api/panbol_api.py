from flask.views import MethodView
from my_app import app
import json

class PanbolApi(MethodView):
    def get(self):
        records = [{
            'campo1':'valor1',
            'campo2':'valor2',
            'campo3':'valor3'}]
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