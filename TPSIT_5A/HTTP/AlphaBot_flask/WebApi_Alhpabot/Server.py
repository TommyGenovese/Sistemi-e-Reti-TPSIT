from flask import Flask, render_template, redirect, url_for, request
import time, alphabot

#add log
app = Flask(__name__)

robot = alphabot.AlphaBot()
robot.stop()

@app.route('/drive', methods=['POST'])
def drivep():
    print("Start")
    #lettura dati dal sito
    movement = request.form['btn']

    if movement == "Forward":
        print("avanti")
        robot.forward()
        time.sleep(0.5)
        robot.stop()

    if movement == "Right":
        print("Sinistra")
        robot.left()
        time.sleep(0.5)
        robot.stop()

    if movement == "Backward":
        print("Indietro")
        robot.backward()
        time.sleep(0.5)
        robot.stop()

    if movement == "Left":
        print("Destra")
        robot.right()
        time.sleep(0.5)
        robot.stop()
        
    return render_template("drive.html", methods=['GET'])

@app.route("/drive", methods=['GET'])
def drive():
    print("Drive")
    return render_template("drive.html")

@app.route("/")             #http://127.0.0.1:5000/
def main():
    print("Main")
    robot.stop()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="192.168.1.107", debug=True)