#
# PySNMP MIB module WLSX-TUNNELEDNODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/mibdump/asn1/WLSX-TUNNELEDNODE-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:14:03 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
snmpModules, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, Unsigned32, Integer32, Bits, MibIdentifier, IpAddress, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "snmpModules", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Unsigned32", "Integer32", "Bits", "MibIdentifier", "IpAddress", "Counter32", "iso")
TextualConvention, RowStatus, StorageType, TAddress, TDomain, PhysAddress, TruthValue, MacAddress, TimeInterval, DisplayString, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "StorageType", "TAddress", "TDomain", "PhysAddress", "TruthValue", "MacAddress", "TimeInterval", "DisplayString", "TestAndIncr")
wlsxTunneledNodeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17))
wlsxTunneledNodeMIB.setRevisions(('1907-08-06 05:19',))
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setLastUpdated('0708060519Z')
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setOrganization('Aruba Wireless Networks')
wlsxTunneledNodeOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1))
wlsxTunneledNodeRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1), )
if mibBuilder.loadTexts: wlsxTunneledNodeRequestTable.setStatus('current')
wlsxTunneledNodeRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1), ).setIndexNames((0, "WLSX-TUNNELEDNODE-MIB", "wlsxTunneledNodeMAC"))
if mibBuilder.loadTexts: wlsxTunneledNodeRequestEntry.setStatus('current')
wlsxTunneledNodeMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: wlsxTunneledNodeMAC.setStatus('current')
wlsxTunneledNodeIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeIp.setStatus('current')
wlsxNumTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumTunnels.setStatus('current')
wlsxTunneledNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("others", 1), ("corvina", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeType.setStatus('current')
mibBuilder.exportSymbols("WLSX-TUNNELEDNODE-MIB", PYSNMP_MODULE_ID=wlsxTunneledNodeMIB, wlsxTunneledNodeMIB=wlsxTunneledNodeMIB, wlsxTunneledNodeIp=wlsxTunneledNodeIp, wlsxTunneledNodeRequestTable=wlsxTunneledNodeRequestTable, wlsxTunneledNodeOpGroup=wlsxTunneledNodeOpGroup, wlsxTunneledNodeType=wlsxTunneledNodeType, wlsxTunneledNodeRequestEntry=wlsxTunneledNodeRequestEntry, wlsxTunneledNodeMAC=wlsxTunneledNodeMAC, wlsxNumTunnels=wlsxNumTunnels)
