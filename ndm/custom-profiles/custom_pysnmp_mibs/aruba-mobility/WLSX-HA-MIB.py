#
# PySNMP MIB module WLSX-HA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/mibdump/asn1/WLSX-HA-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:13:55 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ArubaHaConnectivityStatus, ArubaEnableValue, ArubaHaRole = mibBuilder.importSymbols("ARUBA-TC", "ArubaHaConnectivityStatus", "ArubaEnableValue", "ArubaHaRole")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, ObjectIdentity, Gauge32, MibIdentifier, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, TimeTicks, Counter64, ModuleIdentity, Integer32, IpAddress, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Gauge32", "MibIdentifier", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "TimeTicks", "Counter64", "ModuleIdentity", "Integer32", "IpAddress", "iso", "NotificationType")
StorageType, RowStatus, TDomain, TextualConvention, MacAddress, DisplayString, TimeInterval, TruthValue, TestAndIncr, TAddress, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "TDomain", "TextualConvention", "MacAddress", "DisplayString", "TimeInterval", "TruthValue", "TestAndIncr", "TAddress", "PhysAddress")
wlsxHaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20))
wlsxHaMIB.setRevisions(('1916-06-07 20:30',))
if mibBuilder.loadTexts: wlsxHaMIB.setLastUpdated('1606072030Z')
if mibBuilder.loadTexts: wlsxHaMIB.setOrganization('Aruba Wireless Networks')
wlsxHighAvalabilityInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1))
wlsxHighAvalabilityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2))
wlsxHighAvalabilityConfigTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1), )
if mibBuilder.loadTexts: wlsxHighAvalabilityConfigTable.setStatus('current')
wlsxHighAvalabilityConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1), ).setIndexNames((0, "WLSX-HA-MIB", "haProfileName"))
if mibBuilder.loadTexts: wlsxHighAvalabilityConfigEntry.setStatus('current')
haProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)))
if mibBuilder.loadTexts: haProfileName.setStatus('current')
haMembership = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haMembership.setStatus('current')
haState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 3), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haState.setStatus('current')
haRole = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 4), ArubaHaRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haRole.setStatus('current')
haPreemption = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 5), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haPreemption.setStatus('current')
haOversubscription = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 6), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haOversubscription.setStatus('current')
haStateSync = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 7), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haStateSync.setStatus('current')
haPresharedKey = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haPresharedKey.setStatus('current')
haIntercontrollerHbt = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 9), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haIntercontrollerHbt.setStatus('current')
haHbtThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haHbtThreshold.setStatus('current')
haHbtInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haHbtInterval.setStatus('current')
wlsxHighAvalabilityApTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2), )
if mibBuilder.loadTexts: wlsxHighAvalabilityApTable.setStatus('current')
wlsxHighAvalabilityApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1), ).setIndexNames((0, "WLSX-HA-MIB", "haProfileName"))
if mibBuilder.loadTexts: wlsxHighAvalabilityApEntry.setStatus('current')
haActiveAPs = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haActiveAPs.setStatus('current')
haStandbyAPs = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haStandbyAPs.setStatus('current')
haTotalAPs = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haTotalAPs.setStatus('current')
wlsxIntercontrollerHbtTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3), )
if mibBuilder.loadTexts: wlsxIntercontrollerHbtTable.setStatus('current')
wlsxIntercontrollerHbtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1), ).setIndexNames((0, "WLSX-HA-MIB", "haActiveCtrl"))
if mibBuilder.loadTexts: wlsxIntercontrollerHbtEntry.setStatus('current')
haActiveCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: haActiveCtrl.setStatus('current')
haActiveCtrlIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haActiveCtrlIp.setStatus('current')
haReferenceCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haReferenceCnt.setStatus('current')
haTotalHbtRequestsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haTotalHbtRequestsSent.setStatus('current')
haTotalHbtResponsesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haTotalHbtResponsesRcvd.setStatus('current')
haLastMissedHbtCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haLastMissedHbtCnt.setStatus('current')
haLastHbtMissedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 3, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: haLastHbtMissedTime.setStatus('current')
wlsxStateSyncTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4), )
if mibBuilder.loadTexts: wlsxStateSyncTable.setStatus('current')
wlsxStateSyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1), ).setIndexNames((0, "WLSX-HA-MIB", "haProfileName"))
if mibBuilder.loadTexts: wlsxStateSyncEntry.setStatus('current')
haActivePmkCacheEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haActivePmkCacheEntries.setStatus('current')
haReplicatedPmkCacheEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haReplicatedPmkCacheEntries.setStatus('current')
haTotalPmkCacheEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haTotalPmkCacheEntries.setStatus('current')
haActiveKeyCacheEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haActiveKeyCacheEntries.setStatus('current')
haReplicatedKeyCacheEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haReplicatedKeyCacheEntries.setStatus('current')
haTotalKeyCacheEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haTotalKeyCacheEntries.setStatus('current')
wlsxHighAvalabilityTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5), )
if mibBuilder.loadTexts: wlsxHighAvalabilityTunnelTable.setStatus('current')
wlsxHighAvalabilityTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1), ).setIndexNames((0, "WLSX-HA-MIB", "haProfileName"))
if mibBuilder.loadTexts: wlsxHighAvalabilityTunnelEntry.setStatus('current')
haActiveVapTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haActiveVapTunnels.setStatus('current')
haStandbyVapTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haStandbyVapTunnels.setStatus('current')
haTotalVapTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haTotalVapTunnels.setStatus('current')
haAPHbtTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 1, 5, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haAPHbtTunnels.setStatus('current')
wlsxHaTrapObjectsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1))
wlsxHaTrapDefinitionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2))
wlsxHaV4Status = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 1), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxHaV4Status.setStatus('current')
wlsxHaV4Role = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 2), ArubaHaRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxHaV4Role.setStatus('current')
wlsxHaV6Status = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 3), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxHaV6Status.setStatus('current')
wlsxHaV6Role = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 4), ArubaHaRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxHaV6Role.setStatus('current')
wlsxHaAPName = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxHaAPName.setStatus('current')
wlsxHaActiveControllerIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxHaActiveControllerIp.setStatus('current')
wlsxHaStandbyControllerIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxHaStandbyControllerIp.setStatus('current')
wlsxTrapHaConnectivityStatus = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 8), ArubaHaConnectivityStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTrapHaConnectivityStatus.setStatus('current')
wlsxTrapHaIntercontrollerHbtMissCnt = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTrapHaIntercontrollerHbtMissCnt.setStatus('current')
wlsxTrapHaHbtMissTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTrapHaHbtMissTimeStamp.setStatus('current')
wlsxTrapHaStandbyApCnt = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTrapHaStandbyApCnt.setStatus('current')
wlsxHaState = NotificationType((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 1)).setObjects(("WLSX-HA-MIB", "wlsxHaV4Status"), ("WLSX-HA-MIB", "wlsxHaV4Role"), ("WLSX-HA-MIB", "wlsxHaV6Status"), ("WLSX-HA-MIB", "wlsxHaV6Role"))
if mibBuilder.loadTexts: wlsxHaState.setStatus('current')
wlsxHaStandbyIpSentFailed = NotificationType((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 2)).setObjects(("WLSX-HA-MIB", "wlsxHaStandbyControllerIp"), ("WLSX-HA-MIB", "wlsxHaAPName"))
if mibBuilder.loadTexts: wlsxHaStandbyIpSentFailed.setStatus('current')
wlsxHaStandbyConnectivityState = NotificationType((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 3)).setObjects(("WLSX-HA-MIB", "wlsxHaAPName"), ("WLSX-HA-MIB", "wlsxHaStandbyControllerIp"), ("WLSX-HA-MIB", "wlsxTrapHaConnectivityStatus"))
if mibBuilder.loadTexts: wlsxHaStandbyConnectivityState.setStatus('current')
wlsxHaIntercontrollerHbtMiss = NotificationType((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 4)).setObjects(("WLSX-HA-MIB", "wlsxTrapHaIntercontrollerHbtMissCnt"), ("WLSX-HA-MIB", "wlsxHaActiveControllerIp"), ("WLSX-HA-MIB", "wlsxTrapHaHbtMissTimeStamp"))
if mibBuilder.loadTexts: wlsxHaIntercontrollerHbtMiss.setStatus('current')
wlsxHaFailoverTrigger = NotificationType((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 5)).setObjects(("WLSX-HA-MIB", "wlsxHaActiveControllerIp"), ("WLSX-HA-MIB", "wlsxTrapHaStandbyApCnt"))
if mibBuilder.loadTexts: wlsxHaFailoverTrigger.setStatus('current')
wlsxHaFailoverRequestFromAp = NotificationType((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 20, 2, 2, 6)).setObjects(("WLSX-HA-MIB", "wlsxHaAPName"))
if mibBuilder.loadTexts: wlsxHaFailoverRequestFromAp.setStatus('current')
mibBuilder.exportSymbols("WLSX-HA-MIB", haPreemption=haPreemption, wlsxTrapHaIntercontrollerHbtMissCnt=wlsxTrapHaIntercontrollerHbtMissCnt, haStandbyVapTunnels=haStandbyVapTunnels, haLastMissedHbtCnt=haLastMissedHbtCnt, wlsxHaFailoverTrigger=wlsxHaFailoverTrigger, haStateSync=haStateSync, wlsxIntercontrollerHbtTable=wlsxIntercontrollerHbtTable, haActiveCtrl=haActiveCtrl, wlsxHaStandbyConnectivityState=wlsxHaStandbyConnectivityState, haAPHbtTunnels=haAPHbtTunnels, wlsxTrapHaHbtMissTimeStamp=wlsxTrapHaHbtMissTimeStamp, PYSNMP_MODULE_ID=wlsxHaMIB, haRole=haRole, haStandbyAPs=haStandbyAPs, wlsxStateSyncEntry=wlsxStateSyncEntry, haTotalKeyCacheEntries=haTotalKeyCacheEntries, wlsxHaTrapDefinitionGroup=wlsxHaTrapDefinitionGroup, haMembership=haMembership, haIntercontrollerHbt=haIntercontrollerHbt, wlsxHighAvalabilityConfigTable=wlsxHighAvalabilityConfigTable, wlsxIntercontrollerHbtEntry=wlsxIntercontrollerHbtEntry, haTotalHbtRequestsSent=haTotalHbtRequestsSent, haTotalPmkCacheEntries=haTotalPmkCacheEntries, wlsxHighAvalabilityTunnelTable=wlsxHighAvalabilityTunnelTable, haReplicatedKeyCacheEntries=haReplicatedKeyCacheEntries, haReplicatedPmkCacheEntries=haReplicatedPmkCacheEntries, haState=haState, haHbtThreshold=haHbtThreshold, wlsxHighAvalabilityTunnelEntry=wlsxHighAvalabilityTunnelEntry, wlsxHighAvalabilityApTable=wlsxHighAvalabilityApTable, wlsxHaActiveControllerIp=wlsxHaActiveControllerIp, haTotalAPs=haTotalAPs, haOversubscription=haOversubscription, wlsxHaMIB=wlsxHaMIB, wlsxHaAPName=wlsxHaAPName, haActiveAPs=haActiveAPs, wlsxHighAvalabilityConfigEntry=wlsxHighAvalabilityConfigEntry, wlsxHighAvalabilityApEntry=wlsxHighAvalabilityApEntry, wlsxHighAvalabilityTraps=wlsxHighAvalabilityTraps, haActiveKeyCacheEntries=haActiveKeyCacheEntries, wlsxHaV6Status=wlsxHaV6Status, haHbtInterval=haHbtInterval, wlsxHaV6Role=wlsxHaV6Role, haTotalVapTunnels=haTotalVapTunnels, wlsxHaState=wlsxHaState, haActivePmkCacheEntries=haActivePmkCacheEntries, haTotalHbtResponsesRcvd=haTotalHbtResponsesRcvd, wlsxStateSyncTable=wlsxStateSyncTable, wlsxTrapHaConnectivityStatus=wlsxTrapHaConnectivityStatus, haActiveVapTunnels=haActiveVapTunnels, haPresharedKey=haPresharedKey, wlsxHaV4Role=wlsxHaV4Role, wlsxHaStandbyIpSentFailed=wlsxHaStandbyIpSentFailed, wlsxTrapHaStandbyApCnt=wlsxTrapHaStandbyApCnt, wlsxHaIntercontrollerHbtMiss=wlsxHaIntercontrollerHbtMiss, wlsxHighAvalabilityInfoGroup=wlsxHighAvalabilityInfoGroup, haProfileName=haProfileName, haReferenceCnt=haReferenceCnt, wlsxHaStandbyControllerIp=wlsxHaStandbyControllerIp, wlsxHaFailoverRequestFromAp=wlsxHaFailoverRequestFromAp, haActiveCtrlIp=haActiveCtrlIp, haLastHbtMissedTime=haLastHbtMissedTime, wlsxHaTrapObjectsGroup=wlsxHaTrapObjectsGroup, wlsxHaV4Status=wlsxHaV4Status)
