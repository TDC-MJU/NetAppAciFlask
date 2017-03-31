import json
import requests



def createTenant(ui_tenant):
	aciUrl = 'https://URL/api/'

	# create credentials structure
	loginCred = {'aaaUser': {'attributes': {'name': 'admin', 'pwd': 'pwd'}}}
	jsonLoginCred = json.dumps(loginCred)

	# log in to API
	loginUrl = aciUrl + 'aaaLogin.json'
	post_response = requests.post(loginUrl, verify=False, data=jsonLoginCred)

	# get token from login response structure
	auth = json.loads(post_response.text)
	loginToken = auth['imdata'][0]['aaaLogin']['attributes']['token']

	# create cookie array from token
	cookies = {}
	cookies['APIC-Cookie'] = loginToken


	#create tenant url
	tenantUrl = 'node/mo/uni/tn-{}.json'



	newUrl = aciUrl + tenantUrl.format(ui_tenant)


	# create tenant structure
	tenantJsonFormat = {"fvTenant":{"attributes":{"dn":"uni/tn-Bogus_TN","name":"Bogus_TN","rn":"tn-Bogus_TN","status":"created"},"children":[]}}
	tenantJsonFormat['fvTenant']['attributes']['dn'] = 'uni/tn-{}'.format(ui_tenant)
	tenantJsonFormat['fvTenant']['attributes']['rn'] = 'tn-{}'.format(ui_tenant)
	tenantJsonFormat['fvTenant']['attributes']['name'] = ui_tenant


	jsonTenant = json.dumps(tenantJsonFormat)

	# Posting Tenant 
	post_response = requests.post(newUrl, verify=False, cookies=cookies, data=jsonTenant)
        print post_response.status_code
        return post_response.status_code






def createsvpool():
    aciUrl = 'https://URL/api/'

# create credentials structure
    loginCred = {'aaaUser': {'attributes': {'name': 'admin', 'pwd': 'acilab1234'}}}
    jsonLoginCred = json.dumps(loginCred)

# log in to API
    loginUrl = aciUrl + 'aaaLogin.json'
    post_response = requests.post(loginUrl, verify=False, data=jsonLoginCred)

# get token from login response structure
    auth = json.loads(post_response.text)
    loginToken = auth['imdata'][0]['aaaLogin']['attributes']['token']

# create cookie array from token
    cookies = {}
    cookies['APIC-Cookie'] = loginToken



#Create URL for Static Vlan Pool

    vpoolurl = 'node/mo/uni/infra/vlanns-[{}]-static.json'.format(spname)

    newurl = aciUrl + vpoolurl
# Create static Vlan pool and Phy Domain

    vPoolJsonFormat = {"fvnsVlanInstP":{"attributes":{"dn":"uni/infra/vlanns-[Amiri-static-pool]-static","name":"Amiri-static-pool","allocMode":"static","rn":"vlanns-[Amiri-static-pool]-static","status":"created"},"children":[{"fvnsEncapBlk":{"attributes":{"dn":"uni/infra/vlanns-[Amiri-static-pool]-static/from-[vlan-202]-to-[vlan-202]","from":"vlan-202","to":"vlan-202","rn":"from-[vlan-202]-to-[vlan-202]","status":"created"},"children":[]}}]}}
    vPoolJsonFormat['fvnsVlanInstP']['attributes']['dn'] = 'uni/infra/vlanns-[{}]-static'.format(spname)
    vPoolJsonFormat['fvnsVlanInstP']['attributes']['name'] = spname
    vPoolJsonFormat['fvnsVlanInstP']['attributes']['rn'] = 'vlanns-[{}]-static'.format(spname)
    vPoolJsonFormat['fvnsVlanInstP']['children'][0]['fvnsEncapBlk']['attributes']['dn'] = 'uni/infra/vlanns-[{}]-static/from-[{}]-to-[{}]'.format(spname, v1, v1)
    vPoolJsonFormat['fvnsVlanInstP']['children'][0]['fvnsEncapBlk']['attributes']['from'] = v1
    vPoolJsonFormat['fvnsVlanInstP']['children'][0]['fvnsEncapBlk']['attributes']['to'] = v2
    vPoolJsonFormat['fvnsVlanInstP']['children'][0]['fvnsEncapBlk']['attributes']['rn'] = 'from-[{}]-to-[{}]'.format(v1, v2)


    jsonvPool = json.dumps(vPoolJsonFormat)

# Posting Static Vlan Pool
    post_response = requests.post(newUrl, verify=False, cookies=cookies, data=jsonvPool)



