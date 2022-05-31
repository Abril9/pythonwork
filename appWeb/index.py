from flask import Flask, render_template
""" Se encarga de arrancar la aplicacion, el sitio web

esta flash y django para una appweb
flash es más sencillo, basta con llamar una biblioteca para usarla
django es más completo, investigar después ...


primero corro pip install Flash, se instaló la 1.0.3

importo desde flash render_template para poder trabajar con htmls

en el run de la aplicacion, la variable debug en true hace que sin tener 
que reiniciar el servidor se actualice cada vez que modifico algo. 
Por defecto es false.

"""

#le indico que este archivo es el principal:
#inicializo Flash a partir de el objeto que llamamos app
app = Flask(__name__) #name es una variable que me brinda python

#creamos las rutas
@app.route('/') #le paso el nombre de la url
def home():
        return render_template('home.html')

@app.route('/info') #le paso el nombre de la url
def info():
        return render_template('info.html')

#como escuchamos peticiones desde el navegador:
if __name__ == '__main__':
    app.run(debug=True) #ejecuta la aplicación








