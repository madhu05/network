import random
import json
def test(data, data2):
    """
    Converts a NetJSON 'NetworkGraph' object
    to a NetworkX Graph object,which is then returned.
    Additionally checks for protocol version, revision and metric.
    """
    net = {}
    network = {}
    network1 = []
    network2 = []
    with open(data) as json1:
        data1 = json.load(json1)
    with open(data2) as json2:
        data3 = json.load(json2)
        # ensure is NetJSON NetworkGraph object
        d = {}
        l = {}
        a = {}
        b = {}
        c = {}
    with open('./result_al1.json', 'w') as json_data:
        net["type"] = "NetworkGraph"
        for node in data1["openstack_ports"]:
            if node['device_owner'] != "network:floatingip" and node['device_owner'] != "network:router_gateway" and node['device_id'] != "":
                for data2 in node["fixed_ips"]:
                    b["ip_address"] = (data2['ip_address'])
                    b["mac_address"] = (node['mac_address'])
                d["id"] = (node['network_id'])
                d["id"] = (node['device_id'])
                d["type"] = (node['device_owner'])
                b["imageSrc"] = "assets/img/" + str(random.randint(1, 11)) + ".png"
                b["alerts"] = "10"
                b["imageSize"] = 50
                d["properties"] = b.copy()
                network1.append(d.copy())
        for node in data1["openstack_ports"]:
            if node["device_owner"] == "network:dhcp":
                for data2 in node["fixed_ips"]:
                    b["ip_address"] = (data2['ip_address'])
                    b["mac_address"] = (node['mac_address'])
                d["id"] = (node['network_id'])
                d["type"] = (node['device_owner'])
                b["imageSrc"] = "assets/img/" + str(random.randint(1, 11)) + ".png"
                b["alerts"] = str(random.randint(1, 10))
                b["imageSize"] = 50
                d["properties"] = b.copy()
                network1.append(d.copy())
        for node in data3["openstack_routers"]:
            for data2 in node["external_gateway_info"]["external_fixed_ips"]:
                c["ip_address"] = (data2['ip_address'])
                c["router_name"] = (node['name'])
            d["id"] = (node['external_gateway_info']['network_id'])
            d["type"] = (node['availability_zones'][0])
            c["imageSrc"] = "assets/img/" + str(random.randint(1, 11)) + ".png"
            c["alerts"] = str(random.randint(1, 10))
            c["imageSize"] = 50
            d["properties"] = c.copy()
            network1.append(d.copy())
        network["nodes"] = network1
        for link in data1["openstack_ports"]:
            if link['device_owner'] != "network:floatingip" and link['device_owner'] != "network:router_gateway" and link['device_id'] != "":
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


clean('ports_238.json', 'result-port_238')
clean('routers_238.json', 'result-router_238')
test("result-port_238.json", "result-router_238.json")
