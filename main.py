import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/add', methods=['POST'])
def add_user():
    try:
        _json = request.json
        _timestamp = _json['timestamp']
        _deviceUUID = _json['deviceUUID']
        _ratingCounter = _json['ratingCounter']
        _simNumberID = _json['simNumberID']
        _countryISO = _json['countryISO']
        _phoneOperatorId = _json['phoneOperatorId']
        _simOperatorId = _json['simOperatorId']
        _operatorMcc = _json['operatorMcc']
        _operatorMnc = _json['operatorMnc']
        _devManufacturer = _json['devManufacturer']
        _devModel = _json['devModel']
        _isConected = _json['isConected']
        _phoneNetStandard = _json['phoneNetStandard']
        _phoneNetTechnology = _json['phoneNetTechnology']
        _internetConNetwork = _json['internetConNetwork']
        _latitude = _json['latitude']
        _longitude = _json['longitude']
        _pingTimeMilis = _json['pingTimeMilis']
        _downloadSpeed = _json['downloadSpeed']
        _uploadSpeed = _json['uploadSpeed']
        _ipPublicAddr = _json['ipPublicAddr']
        _internetISP = _json['internetISP']
        _phoneSignalStrength = _json['phoneSignalStrength']
        _phoneAsuStrength = _json['phoneAsuStrength']
        _phoneSignalLevel = _json['phoneSignalLevel']
        _signalQuality = _json['signalQuality']
        _fieldIsRegistered = _json['fieldIsRegistered']
        _phoneRsrpStrength = _json['phoneRsrpStrength']
        _phoneRssnrStrength = _json['phoneRssnrStrength']
        _phoneTimingAdvance = _json['phoneTimingAdvance']
        _phoneCqiStrength = _json['phoneCqiStrength']
        _phoneRsrqStrength = _json['phoneRsrqStrength']
        _cellLtePci = _json['cellLtePci']
        _cellLteCid = _json['cellLteCid']
        _cellLteTac = _json['cellLteTac']
        _cellLteeNodeB = _json['cellLteeNodeB']
        _cellLteEarfcn = _json['cellLteEarfcn']
        _cellBslat = _json['cellBslat']
        _cellBslon = _json['cellBslon']
        _cellSid = _json['cellSid']
        _cellNid = _json['cellNid']
        _cellBid = _json['cellBid']
        _cellWcdmaLac = _json['cellWcdmaLac']
        _cellWcdmaUcid = _json['cellWcdmaUcid']
        _cellWcdmaUarfcn = _json['cellWcdmaUarfcn']
        _cellWcdmaPsc = _json['cellWcdmaPsc']
        _cellWcdmaCid = _json['cellWcdmaCid']
        _cellWcdmaRnc = _json['cellWcdmaRnc']
        _cellGsmArcfn = _json['cellGsmArcfn']
        _cellGsmLac = _json['cellGsmLac']
        _cellGsmCid = _json['cellGsmCid']

        # validate the received values
        if _timestamp and _deviceUUID and _ratingCounter and _simNumberID and _countryISO and _phoneOperatorId and _simOperatorId and _operatorMcc and _operatorMnc and _devManufacturer and _devModel and _isConected and _phoneNetStandard and _phoneNetTechnology and _internetConNetwork and _latitude and _longitude and _pingTimeMilis and _downloadSpeed and _uploadSpeed and _ipPublicAddr and _internetISP and _phoneSignalStrength and _phoneAsuStrength and _phoneSignalLevel and _signalQuality and _fieldIsRegistered and _phoneRsrpStrength and _phoneRssnrStrength and _phoneTimingAdvance and _phoneCqiStrength and _phoneRsrqStrength and _cellLtePci and _cellLteCid and _cellLteTac and _cellLteeNodeB and _cellLteEarfcn and _cellBslat and _cellBslon and _cellSid and _cellNid and _cellBid and _cellWcdmaLac and _cellWcdmaUcid and _cellWcdmaUarfcn and _cellWcdmaPsc and _cellWcdmaCid and _cellWcdmaRnc and _cellGsmArcfn and _cellGsmLac and _cellGsmCid and request.method == 'POST':
            #do not save password as a plain text
            #_hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO tbcellularscan(timestamp, deviceUUID, ratingCounter, simNumberID, countryISO, phoneOperatorId, simOperatorId, operatorMcc, operatorMnc, devManufacturer, devModel, isConected, phoneNetStandard, phoneNetTechnology, internetConNetwork, latitude, longitude, pingTimeMilis, downloadSpeed, uploadSpeed, ipPublicAddr, internetISP, phoneSignalStrength, phoneAsuStrength, phoneSignalLevel, signalQuality, fieldIsRegistered, phoneRsrpStrength, phoneRssnrStrength, phoneTimingAdvance, phoneCqiStrength, phoneRsrqStrength, cellLtePci, cellLteCid, cellLteTac, cellLteeNodeB, cellLteEarfcn, cellBslat, cellBslon, cellSid, cellNid, cellBid, cellWcdmaLac, cellWcdmaUcid, cellWcdmaUarfcn, cellWcdmaPsc, cellWcdmaCid, cellWcdmaRnc, cellGsmArcfn, cellGsmLac, cellGsmCid ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (_timestamp, _deviceUUID, _ratingCounter, _simNumberID, _countryISO, _phoneOperatorId, _simOperatorId, _operatorMcc, _operatorMnc, _devManufacturer, _devModel, _isConected, _phoneNetStandard, _phoneNetTechnology, _internetConNetwork, _latitude, _longitude, _pingTimeMilis, _downloadSpeed, _uploadSpeed, _ipPublicAddr, _internetISP, _phoneSignalStrength, _phoneAsuStrength, _phoneSignalLevel, _signalQuality, _fieldIsRegistered, _phoneRsrpStrength, _phoneRssnrStrength, _phoneTimingAdvance, _phoneCqiStrength, _phoneRsrqStrength, _cellLtePci, _cellLteCid, _cellLteTac, _cellLteeNodeB, _cellLteEarfcn, _cellBslat, _cellBslon, _cellSid, _cellNid, _cellBid, _cellWcdmaLac, _cellWcdmaUcid, _cellWcdmaUarfcn, _cellWcdmaPsc, _cellWcdmaCid, _cellWcdmaRnc, _cellGsmArcfn, _cellGsmLac, _cellGsmCid,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('registro credado satisfactoriamente!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/adddev', methods=['POST'])
def add_dev():
    try:
        _json = request.json
        _deviceUUID = _json['deviceUUID']
        _deviceModel = _json['deviceModel']
        _deviceOS = _json['deviceOS']
        _osVersion = _json['osVersion']
        _isDualSim = _json['isDualSim']
        _fieldIsRegistered = _json['fieldIsRegistered']


        # validate the received values
        if _deviceUUID and _deviceModel and _deviceOS and _osVersion and _isDualSim and _fieldIsRegistered and request.method == 'POST':
            #do not save password as a plain text
            #_hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO tbdeviceinformation(deviceUUID, deviceModel, deviceOS, osVersion, isDualSim, fieldIsRegistered ) VALUES(%s, %s, %s, %s, %s, %s)"
            data = (_deviceUUID, _deviceModel, _deviceOS, _osVersion, _isDualSim, _fieldIsRegistered,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('registro credado satisfactoriamente!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()        

@app.route('/getdata')
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM cellularscantb")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/getdata/<int:id>')
def user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM cellularscantb WHERE scanid=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/update', methods=['POST'])
def update_user():
    try:
        _json = request.json
        _countryiso = _json['countryiso']
        _operatorid = _json['operatorid']
        _operatorname = _json['operatorname']
        _isconected = _json['isconected']
        _phonesignaltype = _json['phonesignaltype']
        _phonenetworktype = _json['phonenetworktype']
        _signalquality = _json['signalquality']
        _networkconectivitytype = _json['networkconectivitytype']
        _phonesignalstrength = _json['phonesignalstrength']
        _downloadmovilespeed = _json['downloadmovilespeed']
        _uploadmovilspeed = _json['uploadmovilspeed']
        _wifispeed = _json['wifispeed']
        _latitude = _json['latitude']
        _longitude = _json['longitude']
        # validate the received values
        if _countryiso and _operatorid and _operatorname and _isconected and _phonesignaltype and _phonenetworktype and _signalquality and _networkconectivitytype and _phonesignalstrength and _downloadmovilespeed and _uploadmovilspeed and _wifispeed and _latitude and _longitude and request.method == 'POST':
            #do not save password as a plain text
            #_hashed_password = generate_password_hash(_password)
            # save edits
            sql = "UPDATE cellularscantb SET _countryiso=%s,  _operatorid=%s,  _operatorname=%s,  _isconected=%s,  _phonesignaltype=%s,  _phonenetworktype=%s,  _signalquality=%s,  _networkconectivitytype=%s,  _phonesignalstrength=%s,  _downloadmovilespeed=%s,  _uploadmovilspeed=%s,  _wifispeed=%s,  _latitude=%s,  _longitude=%s WHERE user_id=%s"
            data = (_countryiso, _operatorid, _operatorname, _isconected, _phonesignaltype, _phonenetworktype, _signalquality, _networkconectivitytype, _phonesignalstrength, _downloadmovilespeed, _uploadmovilspeed, _wifispeed, _latitude, _longitude, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('registro creado satisfactoriamente')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:id>')
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cellularscantb WHERE user_id=%s", (id,))
        conn.commit()
        resp = jsonify('registro borrado satisfactoriamente!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=80)
