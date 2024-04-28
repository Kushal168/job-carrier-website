from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("helloooooooooooo")
    return render_template('home.html')

if __name__ == '__main__':
    print("inside if")
    app.run(host='0.0.0.0', debug=True)
  
















# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#   print("helloooooooooooo")


# if (__name__ == '__main__'):
#   print("insideeeennnnnnnnnifff")
#   app.run(host='0.0.0.0',port=80, debug=True)
  

# # print("hello world!!")

# # print(__name__)
