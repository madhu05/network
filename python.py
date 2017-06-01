import random
import json
#import requests
def test(data, data2, data4, data6):
    """
    Converts a NetJSON 'NetworkGraph' object
    to a NetworkX Graph object,which is then returned.
    Additionally checks for protocol version, revision and metric.
    link = "http://192.168.20.137:5010/vm/livedata?ip=192.168.20.137&key=net&from_dt=2017-05-30T15:50:00&to_dt=2017-05-30T16:00:00"
    f = requests.get(link)
    print f.text
    """
    net = {}
    network = {}
    network1 = []
    network2 = []
    network3 = []
    with open(data) as json1:
        data1 = json.load(json1)
    with open(data2) as json2:
        data3 = json.load(json2)
    with open(data4) as json3:
        data5 = json.load(json3)
    with open(data6) as json4:
        data7 = json.load(json4)
        # ensure is NetJSON NetworkGraph object
        d = {}
        l = {}
        a = {}
        b = {}
        c = {}
        done = set()

    with open('./result_all3.json', 'w') as json_data:
        net["type"] = "NetworkGraph"
        for node in data1["openstack_ports"]:
            if node['device_owner'] != "network:floatingip" and node['device_owner'] != "network:router_gateway" and node['device_id'] != "":
                if node['device_owner'] != "network:dhcp":
                    d["id"] = (node['device_id'])
                else:
                    d['id'] = (node['network_id'])
                d["type"] = (node['device_owner'])
                for data2 in node["fixed_ips"]:
                    b["ip_address"] = (data2['ip_address'])
                    b["mac_address"] = (node['mac_address'])
                b["imageSrc"] = "assets/img/" + str(random.randint(1, 4)) + ".png"
                b["alerts"] = "10"
                b["imageSize"] = 50
                d["properties"] = b.copy()
                network3.append(d.copy())
                for d in network3:
                    if d['id'] not in done:
                        done.add(d['id'])
                        network1.append(d.copy())
        for node in data5["openstack_ports"]:
            if node['device_owner'] != "network:floatingip" and node['device_owner'] != "network:router_gateway" and \
                            node['device_id'] != "":
                if node['device_owner'] != "network:dhcp":
                    d["id"] = (node['device_id'])
                else:
                    d['id'] = (node['network_id'])
                d["type"] = (node['device_owner'])
                for data2 in node["fixed_ips"]:
                    b["ip_address"] = (data2['ip_address'])
                    b["mac_address"] = (node['mac_address'])
                b["imageSrc"] = "assets/img/" + str(random.randint(1, 4)) + ".png"
                b["alerts"] = "10"
                b["imageSize"] = 50
                d["properties"] = b.copy()
                network3.append(d.copy())
                for d in network3:
                    if d['id'] not in done:
                        done.add(d['id'])
                        network1.append(d.copy())
        for node in data3["openstack_routers"]:
            for data2 in node["external_gateway_info"]["external_fixed_ips"]:
                c["ip_address"] = (data2['ip_address'])
                c["router_name"] = (node['name'])
            d["id"] = (node['external_gateway_info']['network_id'])
            d["type"] = (node['availability_zones'][0])
            c["imageSrc"] = "assets/img/" + str(random.randint(1, 4)) + ".png"
            c["alerts"] = "10"
            c["imageSize"] = 50
            d["properties"] = c.copy()
            network1.append(d.copy())
            break
        for node in data7["openstack_routers"]:
            for data2 in node["external_gateway_info"]["external_fixed_ips"]:
                c["ip_address"] = (data2['ip_address'])
                c["router_name"] = (node['name'])
            d["id"] = (node['external_gateway_info']['network_id'])
            d["type"] = (node['availability_zones'][0])
            c["imageSrc"] = "assets/img/" + str(random.randint(1, 4)) + ".png"
            c["alerts"] = "10"
            c["imageSize"] = 50
            d["properties"] = c.copy()
            network1.append(d.copy())
            break
        d["id"] = "5cf6c558-e8b8-413c-b745-9ac391cnetfd"
        d["type"] = "network:switch"
        c["ip_address"] = "192.168.0.0"
        c["router_name"] = "cisco_switch200g"
        c["imageSrc"] = "assets/img/" + str(random.randint(1, 4)) + ".png"
        c["alerts"] = "10"
        c["imageSize"] = 50
        d["properties"] = c.copy()
        network1.append(d.copy())
        network["nodes"] = network1
        for link in data1["openstack_ports"]:
            if link['device_owner'] not in ("network:floatingip", "network:router_gateway", "network:dhcp") and link['device_id'] != "":
                a["status"] = link["status"]
                a["admin_state_up"] = link["admin_state_up"]
                if link['device_owner'] in ("network:dhcp", "network:router_interface"):
                    a["lq"] = 0.0
                    a["nlq"] = 0.0
                    a["bitrate"] = "0 mbit/s"
                    a["latency"] = "na"
                elif link['device_owner'] == "compute:nova":
                    a["lq"] = 1.0
                    a["nlq"] = 1.0
                    a["bitrate"] = "35 mbit/s"
                    a["latency"] = "low"
                a["strokeWidth"] = "1px"
                a["strokeDasharray"] = "solid"
                l["source"] = link["network_id"]
                l["target"] = link["device_id"]
                l["properties"] = a.copy()
                network2.append(l.copy())
        for link in data5["openstack_ports"]:
            if link['device_owner'] not in ("network:floatingip", "network:router_gateway", "network:dhcp") and link['device_id'] != "":
                a["status"] = link["status"]
                a["admin_state_up"] = link["admin_state_up"]
                if link['device_owner'] in ("network:dhcp", "network:router_interface"):
                    a["lq"] = 0.0
                    a["nlq"] = 0.0
                    a["bitrate"] = "0 mbit/s"
                    a["latency"] = "na"
                elif link['device_owner'] == "compute:nova":
                    a["lq"] = 1.0
                    a["nlq"] = 1.0
                    a["bitrate"] = "35 mbit/s"
                    a["latency"] = "low"
                a["strokeWidth"] = "1px"
                a["strokeDasharray"] = "solid"
                l["source"] = link["network_id"]
                l["target"] = link["device_id"]
                l["properties"] = a.copy()
                network2.append(l.copy())
        for link in data3["openstack_routers"]:
            a["status"] = link["status"]
            a["admin_state_up"] = link["admin_state_up"]
            a["lq"] = 0.0
            a["nlq"] = 0.0
            a["bitrate"] = "0 mbit/s"
            a["latency"] = "na"
            a["strokeWidth"] = "1px"
            a["strokeDasharray"] = "solid"
            l["source"] = link['external_gateway_info']["network_id"]
            l["target"] = link["id"]
            l["properties"] = a.copy()
            network2.append(l.copy())
        for link in data7["openstack_routers"]:
            a["status"] = link["status"]
            a["admin_state_up"] = link["admin_state_up"]
            a["lq"] = 0.0
            a["nlq"] = 0.0
            a["bitrate"] = "0 mbit/s"
            a["latency"] = "na"
            a["strokeWidth"] = "1px"
            a["strokeDasharray"] = "solid"
            l["source"] = link['external_gateway_info']["network_id"]
            l["target"] = link["id"]
            l["properties"] = a.copy()
            network2.append(l.copy())
        a["status"] = "ACTIVE"
        a["admin_state_up"] = "true"
        a["lq"] = 0.0
        a["nlq"] = 0.0
        a["bitrate"] = "0 mbit/s"
        a["latency"] = "na"
        a["strokeWidth"] = "1px"
        a["strokeDasharray"] = "solid"
        l["source"] = "5cf6c558-e8b8-413c-b745-9ac391cnetfd"
        l["target"] = "b7fcb9e2-fa96-465c-9f9d-9435ab003205"
        l["properties"] = a.copy()
        network2.append(l.copy())
        a["status"] = "ACTIVE"
        a["admin_state_up"] = "true"
        a["lq"] = 0.0
        a["nlq"] = 0.0
        a["bitrate"] = "0 mbit/s"
        a["latency"] = "na"
        a["strokeWidth"] = "1px"
        a["strokeDasharray"] = "solid"
        l["source"] = "5cf6c558-e8b8-413c-b745-9ac391cnetfd"
        l["target"] = "b36c3ed8-2597-49a2-96fe-9a1f57300c2c"
        l["properties"] = a.copy()
        network2.append(l.copy())
        network["links"] = network2
        net["network"] = network
        json.dump(net, json_data)

def clean(data, file_name):
    name = file_name
    f = open(data,"r")
    g = open("%s.json" %name,"w+")
    g.seek(0)
    g.write('{')
    for i, line in enumerate(f):
        if i == 0 or not line.startswith('PLAY'):
            if i == 0 or not line.startswith('TASK'):
                if i == 0 or not line.startswith('ok: '):
                    line = line.replace('    "changed": false,', "")
                    cleanedLine = line.strip()
                    if cleanedLine:  # is not empty
                        g.write(line)
    f.close()
    g.close()


#test('new.json')
clean('port_208.json', 'result-port_208')
clean('port_238.json', 'result-port_238')
clean('router_208.json', 'result-router_208')
clean('router_238.json', 'result-router_238')
test("result-port_208.json", "result-router_208.json", "result-port_238.json", "result-router_238.json")
