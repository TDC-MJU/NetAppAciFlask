
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.fvns
import cobra.model.infra
import cobra.model.pol
import cobra.model.draw
import cobra.model.vz
import cobra.model.phys
from cobra.internal.codec.xmlcodec import toXMLStr
import csv, time, os, sys, re
from pprint import pprint as pp
from colorama import init, Fore, Back, Style
from tabulate import tabulate
from netmiko import ConnectHandler



init(autoreset=True)




def banner_app():
    print (Fore.YELLOW + '''
    **********************************************************
    *                                                        *
    *                 CISCO ACI APPLICATION                  *
    **********************************************************
    '''
    )






def userBuildTenant():
	

	tnname = raw_input('What is the Tenant Name?  ')
	if ('_TN' not in tname):
		tname = tname + '_TN'
	
	print ('The Tenant name is {}'.format(tname))
	


	# the top level object on which operations will be made
	

	topMo = cobra.model.pol.Uni('')


	# Create Tenant
	fvTenant = cobra.model.fv.Tenant(topMo, name=tnName)


	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(fvTenant)
	md.commit(c)

def buildTenant(md, tnName):
	# the top level object on which operations will be made
	topMo = cobra.model.pol.Uni('')


	# Create Tenant
	fvTenant = cobra.model.fv.Tenant(topMo, name=tnName)


	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(fvTenant)
	md.commit(c)



def buildVrf(md, tnName, vrf, vrfdes):
	topMo = cobra.model.pol.Uni('')
	fvTenant = cobra.model.fv.Tenant(topMo, tnName)

	# build the request using cobra syntax
	if vrfdes:
		fvCtx = cobra.model.fv.Ctx(fvTenant, name=vrf, descr=vrfdes)
	else:
		fvCtx = cobra.model.fv.Ctx(fvTenant, name=vrf)


	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(fvTenant)
	md.commit(c)


def buildApp(md, tnName, appName):
	## Build Application Profile

	# the top level object on which operations will be made
	polUni = cobra.model.pol.Uni('')
	fvTenant = cobra.model.fv.Tenant(polUni, tnName)

	# build the request using cobra syntax
	fvAp = cobra.model.fv.Ap(fvTenant, name=appName)


	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(fvTenant)
	md.commit(c)

def epgs(md, tnName, appName, bdName, epg1, epg2):
	
	epglist = [epg1, epg2]

	# the top level object on which operations will be made
	polUni = cobra.model.pol.Uni('')
	
	for epg in epglist:
		fvTenant = cobra.model.fv.Tenant(polUni, tnName)
		fvAp = cobra.model.fv.Ap(fvTenant, appName)

		# build the request using cobra syntax
		fvAEPg = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', name=epg, descr=u'', fwdCtrl=u'', prefGrMemb=u'exclude', prio=u'unspecified', pcEnfPref=u'unenforced')
		fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, tnQosCustomPolName=u'')
		fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=bdName)


		# commit the generated code to APIC
		c = cobra.mit.request.ConfigRequest()
		c.addMo(fvAp)
		md.commit(c)

def buildFilter(md, tnName, fltName, fltEntry):
	# the top level object on which operations will be made
	polUni = cobra.model.pol.Uni('')
	fvTenant = cobra.model.fv.Tenant(polUni, tnName)

	# build the request using cobra syntax
	vzFilter = cobra.model.vz.Filter(fvTenant, ownerKey=u'', name=fltName, descr=u'', ownerTag=u'')
	vzEntry = cobra.model.vz.Entry(vzFilter, tcpRules=u'', arpOpc=u'unspecified', applyToFrag=u'no', dToPort=u'unspecified', descr=u'', matchDscp=u'unspecified', prot=u'unspecified', icmpv4T=u'unspecified', sFromPort=u'unspecified', stateful=u'no', icmpv6T=u'unspecified', sToPort=u'unspecified', etherT=u'unspecified', dFromPort=u'unspecified', name='any')


	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(fvTenant)
	md.commit(c)

def buildAep(md, aep, phyName):
	# the top level object on which operations will be made
	polUni = cobra.model.pol.Uni('')
	infraInfra = cobra.model.infra.Infra(polUni)

	# build the request using cobra syntax
	infraAttEntityP = cobra.model.infra.AttEntityP(infraInfra, ownerKey=u'', name=aep, descr=u'', ownerTag=u'')
	infraRsDomP = cobra.model.infra.RsDomP(infraAttEntityP, tDn=u'uni/phys-{}'.format(phyName))


	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(infraInfra)
	md.commit(c)



def bdSubnet(md, tnName, vrf, bdname, bdsubnet):
	
	try:

		# the top level object on which operations will be made
		topMo = cobra.model.pol.Uni('')
		fvTenant = cobra.model.fv.Tenant(topMo, tnName)

		# build the request using cobra syntax
		fvBD = cobra.model.fv.BD(fvTenant, ownerKey=u'', vmac=u'not-applicable', unkMcastAct=u'flood', name=bdname, descr=u'', unkMacUcastAct=u'proxy', arpFlood=u'no', limitIpLearnToSubnets=u'no', llAddr=u'::', mcastAllow=u'no', mac=u'00:22:BD:F8:19:FF', epMoveDetectMode=u'', unicastRoute=u'yes', ownerTag=u'', multiDstPktAct=u'bd-flood', type=u'regular', ipLearning=u'yes')
		fvRsBDToNdP = cobra.model.fv.RsBDToNdP(fvBD, tnNdIfPolName=u'')
		fvRsCtx = cobra.model.fv.RsCtx(fvBD, tnFvCtxName=vrf)
		fvRsIgmpsn = cobra.model.fv.RsIgmpsn(fvBD, tnIgmpSnoopPolName=u'')
		fvSubnet = cobra.model.fv.Subnet(fvBD, name=u'', descr=u'', ctrl=u'', ip=bdsubnet, preferred=u'no', virtual=u'no')
		fvRsBdToEpRet = cobra.model.fv.RsBdToEpRet(fvBD, resolveAct=u'resolve', tnFvEpRetPolName=u'')


		# commit the generated code to APIC
		c = cobra.mit.request.ConfigRequest()
		c.addMo(fvTenant)
		md.commit(c)
	except:
		print ('Could not create Tenant {}'.format(tnName))



def dynamicpool(md, dynPool, start, stop):
    # the top level object on which operations will be made
    polUni = cobra.model.pol.Uni('')
    infraInfra = cobra.model.infra.Infra(polUni)
	
    # Determin if pool is static or dynamic
    if start == stop:
        fvnsVlanInstP = cobra.model.fvns.VlanInstP(infraInfra, ownerKey=u'', name=dynPool, descr=u'', ownerTag=u'', allocMode=u'static')
	fvnsEncapBlk = cobra.model.fvns.EncapBlk(fvnsVlanInstP, to='vlan-{}'.format(stop), from_='vlan-{}'.format(start), name=u'', descr=u'', allocMode=u'static')

    else:
        # build the request using cobra syntax
	fvnsVlanInstP = cobra.model.fvns.VlanInstP(infraInfra, ownerKey=u'', name=dynPool, descr=u'', ownerTag=u'', allocMode=u'dynamic')
	fvnsEncapBlk = cobra.model.fvns.EncapBlk(fvnsVlanInstP, to='vlan-{}'.format(stop), from_='vlan-{}'.format(start), name=u'', descr=u'', allocMode=u'dynamic')
    
    # commit the generated code to APIC
    c = cobra.mit.request.ConfigRequest()
    c.addMo(infraInfra)
    md.commit(c)


def buildPhy(md, phyName, dynPool):
	topMo = cobra.model.pol.Uni('')

	# build the request using cobra syntax
	physDomP = cobra.model.phys.DomP(topMo, name=phyName)
	infraRsVlanNs = cobra.model.infra.RsVlanNs(physDomP, tDn=u'uni/infra/vlanns-[{}]-dynamic'.format(dynPool))
	

	c = cobra.mit.request.ConfigRequest()
	c.addMo(physDomP)
	md.commit(c)



def buildContract(md, tnName, appName, contract, subject, epgPro, epgCon, fltName):

	# the top level object on which operations will be made
	polUni = cobra.model.pol.Uni('')
	fvTenant = cobra.model.fv.Tenant(polUni, tnName)

	# build the request using cobra syntax
	vzBrCP = cobra.model.vz.BrCP(fvTenant, ownerKey=u'', name=contract, prio=u'unspecified', targetDscp=u'unspecified', ownerTag=u'', descr=u'')
	vzSubj = cobra.model.vz.Subj(vzBrCP, revFltPorts=u'yes', name=subject, prio=u'unspecified', targetDscp=u'unspecified', descr=u'', consMatchT=u'AtleastOne', provMatchT=u'AtleastOne')
	vzRsSubjFiltAtt = cobra.model.vz.RsSubjFiltAtt(vzSubj, directives=u'', tnVzFilterName=fltName)

	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(fvTenant)
	md.commit(c)


	topMo = cobra.model.pol.Uni('')


	# build the request using cobra syntax
	fvTenant = cobra.model.fv.Tenant(topMo, tnName)
	fvAp = cobra.model.fv.Ap(fvTenant, appName)
	fvAEPg = cobra.model.fv.AEPg(fvAp, epgPro)
	fvRsCons = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=contract)
	fvAEPg2 = cobra.model.fv.AEPg(fvAp, epgCon)
	fvRsProv = cobra.model.fv.RsProv(fvAEPg2, tnVzBrCPName=contract)
	drawCont = cobra.model.draw.Cont(fvTenant)
#	drawInst = cobra.model.draw.Inst(drawCont, info="{'{fvAp/epg}-{}'".format(epgPro)+":{'x':65,'y':348.5},'{fvAp/epg}-{}'".format(epgCon) + ":{'x':185,'y':348.5},'{fvAp/contract}-{}'".format(contract) + ":{'x':152,'y':10}}", oDn='uni/tn-{}/ap-{}'.format(tnName, appName))


	# commit the generated code to APIC
	c = cobra.mit.request.ConfigRequest()
	c.addMo(fvTenant)
	md.commit(c)



def acilogin():
	# Login to ACI

	userid = 'admin'
	passwd = 'acilab1234'
	ipaddress = 'https://10.2.21.230'



	# log into an APIC and create a directory object
	ls = cobra.mit.session.LoginSession(ipaddress, userid, passwd)
	md = cobra.mit.access.MoDirectory(ls)
	md.login()
	return md


def inventoryFile(file):
	row_count = 0
	aci = acilogin()
	with open(file,'r') as fh:
		fhreader = csv.reader(fh)
		for row in fhreader:
			if row_count != 0:
				buildTenant(aci,row[0])
				buildVrf(aci, row[0], row[1], row[2])
				buildApp(aci, row[0], row[10])
				dynamicpool(aci, row[7], row[8], row[9])
				buildPhy(aci, row[14], row[7])
				buildAep(aci, row[11], row[14])
				bdSubnet(aci, row[0], row[1], row[4], row[6])
				epgs(aci, row[0], row[10], row[4], row[12], row[14])
				buildFilter(aci, row[0], row[17], row[18])
				buildContract(aci, row[0], row[10], row[16], row[19], row[12], row[14], row[17])

			
			else:
				print('HEADER ROW:\n', row)
				row_count += 1
		fh.close()



if __name__ == '__main__': main()

