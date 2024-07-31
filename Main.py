from flask import Flask,render_template 
app = Flask(__name__) 
@app.route('/') 
def hello_world():
# return render_template('mydigitproject') 
    return render_template('''<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Document</title> <style> body { height: 100%; border: 2pt solid black; } </style> </head> <body> <center><h1>GO DIGIT</h1> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6GPEQUyzbZFwsqF1W5YgXY_SQHuys1E5yvw&s"> </center> </body> </html>''')
if __name__ == '__main__': 
    app.run(debug=True,port=8080)
