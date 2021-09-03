import maintenance

# from flask import Flask, jsonify
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'API is working'

# @app.route('/routes')
# def get_routes():
#     routeArray = []

#     for i in range(1, 27):
#         if i in range(1, 10):
#             routeN = '0' + str(i)
#         else:
#             routeN = str(i)
#         routePath = 'routes/route' + routeN

#         routeDict = {}
#         routeDict['id'] = i
#         churchId = i * 50

#         # Churches
#         churchFile = open(routePath + '/churches.txt').read()
#         churchData = []
#         for church in churchFile.split('\n'):
#             churchId += 1
#             churchArray = church.split('|')
#             churchDict = {
#                 'id': churchId,
#                 'name': churchArray[2],
#                 'url': churchArray[3],
#                 'coordinate': [float(churchArray[1]), float(churchArray[0])]
#             }
#             churchData.append(churchDict)
#         routeDict['churches'] = churchData

#         # Coordinates
#         coordinatesFile = open(routePath + '/coordinates.txt').read()
#         coordinatesData = []
#         for coord in coordinatesFile.split('\n'):
#             coordArray = coord.split('|')
#             coord = [float(coordArray[1]), float(coordArray[0])]
#             coordinatesData.append(coord)
#         routeDict['coords'] = coordinatesData

#         # Description
#         descriptionFile = open(routePath + '/description.txt').read()
#         descriptionData = descriptionFile.split('\n')
#         routeDict['start'] = descriptionData[0]
#         routeDict['end'] = descriptionData[1]
#         routeDict['metres'] = int(descriptionData[2])

#         if len(descriptionData) > 4:
#             routeDict['routeTitle'] = descriptionData[4]
#         if len(descriptionData) > 5:
#             routeDict['routeDescription'] = descriptionData[5]
#         if len(descriptionData) > 6:
#             routeDict['directionsAuthor'] = descriptionData[6]
#         if len(descriptionData) > 8:
#             routeDict['directions'] = descriptionData[8:]

#         routeArray.append(routeDict)
#     return jsonify(routeArray)


# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)
