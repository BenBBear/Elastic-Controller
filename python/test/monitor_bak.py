from flask import Flask,request,Response, jsonify
import Config as config
import util
Traffic_Data = {}
app = Flask(__name__)

topo_inited = False



@app.route("/")
def hello():
    return "This is the Monitor Node!"


@app.route(config.MONITOR['METHODS']['STAT'][0], methods=[config.MONITOR['METHODS']['STAT'][1]])
def stat():    
    statDict = request.get_json()
    # TODO:    
    # argment the Traffic_Data here
    # format of statDict:
    # switches_traffic: {dpid: number of in packet, dpid: number of in packet, ...}
    """
    for switch in statDict.keys():
        if switch in Traffic_Data.keys():
            Traffic_Data[switch] += statDict[switch]
        else:
            Traffic_Data[switch] = statDict[switch]
    """

    return jsonify(**{
        'success':True
    })
    
    



@app.route(config.MONITOR['METHODS']['FINISH_MIGRATION'][0], methods=[config.MONITOR['METHODS']['FINISH_MIGRATION'][1]])
def change_topo():
    content = request.get_json(silent=True)
    # TODO:
    # update the Topology here




    print content, type(content)



@app.route(config.MONITOR['METHODS']['TOPO_REPORT'][0],methods=[config.MONITOR['METHODS']['TOPO_REPORT'][1]])
def gen_topo():
    # TODO:
    # generate initial topology from config information
    content = request.get_json(silent=True)

    # print content
    # if we have topology here, why do we need to relate the controller info with switch? {dpid: traffic, ...} should be OK.
    Traffic_Data[content['ctrl']] = [{
                                        'switch_id':id,
                                        'traffic':{} ## TODO:
                                                     ## Design the traffic structure
                                      }  for id in content['switches']]
    # read config file to get controller-master map

    # notify controller to change the master-slave state, so the controller should have a data structure to keep state?



    return jsonify(**{
        'success':True
    })



def monitor():
    # print "This is the monitor thread"
    if topo_inited:
        # TODO:
        # Implement the monitoring algorithm here, and notify controller use util.HTTP_Request
        # calculate the total traffic of each controller, if traffic data exceeds the threshold, then notify controller to migrate
        pass
    else:
        # if the topology is not inited, then do nothing
        pass







# MAIN
# gen_topo()
util.Set_Interval(monitor,config.MONITOR['CHECK_INTERVAL'])
app.run(host='0.0.0.0', port=config.MONITOR['PORT'])