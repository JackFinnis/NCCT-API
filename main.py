from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'API is working'


@app.route('/routes')
def get_routes():
    routeArray = []

    for i in range(1, 27):
        if i in range(1, 10):
            routeN = '0' + str(i)
        else:
            routeN = str(i)
        routePath = 'routes/route' + routeN

        churchFile = open(routePath + '/churches.txt').read()
        churchData = []
        for church in churchFile.split('\n'):
            churchArray = church.split('|')
            churchDict = {
                'name': churchArray[2],
                'urlString': churchArray[3],
                'coord': {
                    'lat': float(churchArray[1]),
                    'long': float(churchArray[0])
                }
            }
            churchData.append(churchDict)

        coordinatesFile = open(routePath + '/coordinates.txt').read()
        coordinatesData = []
        for coord in coordinatesFile.split('\n'):
            coordArray = coord.split('|')
            coordDict = {
                'lat': float(coordArray[1]),
                'long': float(coordArray[0])
            }
            coordinatesData.append(coordDict)

        descriptionFile = open(routePath + '/description.txt').read()
        descriptionData = descriptionFile.split('\n')
        start = descriptionData[0]
        end = descriptionData[1]
        metres = int(descriptionData[2])

        routeArray.append({
            'id': i,
            'start': start,
            'end': end,
            'metres': metres,
            'churches': churchData,
            'coords': coordinatesData
        })

    return jsonify(routeArray)


app.run(host='0.0.0.0', port=8080, debug=True)
