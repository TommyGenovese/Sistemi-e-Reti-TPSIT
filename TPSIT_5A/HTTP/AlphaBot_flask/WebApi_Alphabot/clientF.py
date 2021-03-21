from flask import Flask, render_template, redirect, url_for, request, jsonify
import json, time, sqlite3, AlphaBot

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    robot = AlphaBot.AlphaBot()
    DR = 16
    DL = 19

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

    #inizializzare il thread per il controllo di ambo i sensori

    if 'path' in request.args:
        path = int(request.args['path'])
    else:
        return "Error: No path provided. Please specify a path"
    
    conn = sqlite3.connect("path.db")
    cur= conn.cursor()
    cur.execute(f"SELECT * FROM percorsi WHERE percorso={path}")
    perc = cur.fetchall()
    print(perc)

    print(perc)

    #cambiare la parte seguente, implementare le Web API

    index = 0
    while index < len(perc):
        distance = ''
        if perc[index] == 'F':
            index = index + 1
            while index < len(perc) and perc[index].isnumeric():
                distance = distance + perc[index]
                index = index + 1


            robot.forward()
            time.sleep(distance)
            robot.stop()

        elif perc[index] == 'B':
            index = index + 1
            while index < len(perc) and perc[index].isnumeric():
                distance = distance + perc[index]
                index = index + 1

            robot.backward()
            time.sleep(distance)
            robot.stop()

        elif perc[index] == 'L':
            index = index + 1
            while index < len(perc) and perc[index].isnumeric():
                distance = distance + perc[index]
                index = index + 1

            robot.left()
            time.sleep(distance)
            robot.stop()

        elif perc[index] == 'R':
            index = index + 1
            while index < len(perc) and perc[index].isnumeric():
                distance = distance + perc[index]
                index = index + 1

            robot.right()
            time.sleep(distance)
            robot.stop()
    
    
    conn.close()


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Page not found</h1><p>Write better your code!</p>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
