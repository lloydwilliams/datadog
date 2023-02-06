#
# PySNMP MIB module WLSX-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/mibdump/asn1/WLSX-STATS-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:14:00 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, snmpModules, Unsigned32, Counter64, Counter32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Integer32, TimeTicks, ModuleIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "snmpModules", "Unsigned32", "Counter64", "Counter32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Integer32", "TimeTicks", "ModuleIdentity", "Gauge32", "Bits")
PhysAddress, TAddress, TextualConvention, DisplayString, TimeInterval, TDomain, TruthValue, MacAddress, TestAndIncr, StorageType, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TAddress", "TextualConvention", "DisplayString", "TimeInterval", "TDomain", "TruthValue", "MacAddress", "TestAndIncr", "StorageType", "RowStatus")
wlsxStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15))
wlsxStatsMIB.setRevisions(('1907-12-10 00:06',))
if mibBuilder.loadTexts: wlsxStatsMIB.setLastUpdated('0712100006Z')
if mibBuilder.loadTexts: wlsxStatsMIB.setOrganization('Aruba Wireless Networks')
wlsxStatsOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1))
wlsxStatsRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1), )
if mibBuilder.loadTexts: wlsxStatsRequestTable.setStatus('current')
wlsxStatsRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1), ).setIndexNames((0, "WLSX-STATS-MIB", "wlsxStatsIndex"))
if mibBuilder.loadTexts: wlsxStatsRequestEntry.setStatus('current')
wlsxStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: wlsxStatsIndex.setStatus('current')
wlsxStatsReqType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsReqType.setStatus('current')
wlsxStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsInterval.setStatus('current')
wlsxStatsCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxStatsCookie.setStatus('current')
mibBuilder.exportSymbols("WLSX-STATS-MIB", wlsxStatsMIB=wlsxStatsMIB, wlsxStatsReqType=wlsxStatsReqType, wlsxStatsInterval=wlsxStatsInterval, wlsxStatsRequestTable=wlsxStatsRequestTable, PYSNMP_MODULE_ID=wlsxStatsMIB, wlsxStatsRequestEntry=wlsxStatsRequestEntry, wlsxStatsIndex=wlsxStatsIndex, wlsxStatsCookie=wlsxStatsCookie, wlsxStatsOpGroup=wlsxStatsOpGroup)
