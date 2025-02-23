import io
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import base64




app = Flask(__name__)


CORS(app)


@app.route("/graficar/<x1>/<x2>/<x3>/<y1>/<y2>/<y3>")


def generate_image(x1, x2, x3, y1, y2, y3):

    x = [int(x1) ,int(x2) ,int(x3)]

    y = [int(y1) ,int(y2) ,int(y3)]


    # creating the bar plot
    pyplot.plot(x,y)
    #referencia = random.randint(0,10000);

    #img = str(referencia);

    # create PNG image in memory
    img= io.BytesIO()  
           # create file-like object in memory to save image without using disk
    

    pyplot.savefig(img, format='png') 
    img.seek(0) 

    #save image in file-like object
   
            
    data = img.getvalue()
       


    data = base64.b64encode(data) # convert to base64 as bytes
    data = data.decode()  # move to beginning of file-like object to read it later
   
   
    img.close()
    pyplot.clf()
    pyplot.close()
  
    return jsonify(data)

           
def create_app():
    return app
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)



    
    
    
