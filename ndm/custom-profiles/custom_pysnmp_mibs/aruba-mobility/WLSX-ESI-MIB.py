#
# PySNMP MIB module WLSX-ESI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/mibdump/asn1/WLSX-ESI-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:13:54 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ArubaESIServerMode, ArubaESIServerStatus = mibBuilder.importSymbols("ARUBA-TC", "ArubaESIServerMode", "ArubaESIServerStatus")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, Gauge32, IpAddress, snmpModules, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, iso, Bits, MibIdentifier, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "IpAddress", "snmpModules", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "iso", "Bits", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32")
RowStatus, TestAndIncr, TAddress, TDomain, StorageType, MacAddress, PhysAddress, DisplayString, TimeInterval, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TestAndIncr", "TAddress", "TDomain", "StorageType", "MacAddress", "PhysAddress", "DisplayString", "TimeInterval", "TextualConvention", "TruthValue")
wlsxESIMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10))
wlsxESIMIB.setRevisions(('1910-01-26 18:06',))
if mibBuilder.loadTexts: wlsxESIMIB.setLastUpdated('1001261806Z')
if mibBuilder.loadTexts: wlsxESIMIB.setOrganization('Aruba Wireless Networks')
wlsxESIConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1))
wlsxESIServerTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1), )
if mibBuilder.loadTexts: wlsxESIServerTable.setStatus('current')
wlsxESIServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1), ).setIndexNames((0, "WLSX-ESI-MIB", "esiServerName"))
if mibBuilder.loadTexts: wlsxESIServerEntry.setStatus('current')
esiServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: esiServerName.setStatus('current')
esiServerGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerGroup.setStatus('current')
esiServerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 3), ArubaESIServerMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerMode.setStatus('current')
esiServerTrustedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedIP.setStatus('current')
esiServerUntrustedIP = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedIP.setStatus('current')
esiServerTrustedSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedSlot.setStatus('current')
esiServerTrustedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedPort.setStatus('current')
esiServerUntrustedSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedSlot.setStatus('current')
esiServerUntrustedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedPort.setStatus('current')
esiServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 10), ArubaESIServerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerStatus.setStatus('current')
esiServerTrustedModule = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerTrustedModule.setStatus('current')
esiServerUntrustedModule = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esiServerUntrustedModule.setStatus('current')
mibBuilder.exportSymbols("WLSX-ESI-MIB", esiServerStatus=esiServerStatus, wlsxESIServerTable=wlsxESIServerTable, esiServerGroup=esiServerGroup, esiServerTrustedSlot=esiServerTrustedSlot, esiServerUntrustedPort=esiServerUntrustedPort, esiServerUntrustedModule=esiServerUntrustedModule, wlsxESIMIB=wlsxESIMIB, esiServerTrustedPort=esiServerTrustedPort, esiServerUntrustedSlot=esiServerUntrustedSlot, wlsxESIConfigGroup=wlsxESIConfigGroup, esiServerUntrustedIP=esiServerUntrustedIP, esiServerName=esiServerName, esiServerTrustedIP=esiServerTrustedIP, esiServerMode=esiServerMode, PYSNMP_MODULE_ID=wlsxESIMIB, wlsxESIServerEntry=wlsxESIServerEntry, esiServerTrustedModule=esiServerTrustedModule)
