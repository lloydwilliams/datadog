#
# PySNMP MIB module RMON2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/github/mibs.snmplabs.com/asn1/RMON2-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:13:59 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
hostControlEntry, matrixControlEntry, OwnerString, channelEntry, historyControlEntry, filterEntry, history, etherStatsEntry, hosts, filter, matrix, statistics = mibBuilder.importSymbols("RMON-MIB", "hostControlEntry", "matrixControlEntry", "OwnerString", "channelEntry", "historyControlEntry", "filterEntry", "history", "etherStatsEntry", "hosts", "filter", "matrix", "statistics")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Unsigned32, NotificationType, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32, iso, MibIdentifier, Counter32, Bits, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Unsigned32", "NotificationType", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32", "iso", "MibIdentifier", "Counter32", "Bits", "Counter64", "IpAddress")
TimeStamp, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "TextualConvention", "DisplayString")
rmon = ModuleIdentity((1, 3, 6, 1, 2, 1, 16))
if mibBuilder.loadTexts: rmon.setLastUpdated('9605270000Z')
if mibBuilder.loadTexts: rmon.setOrganization('IETF RMON MIB Working Group')
protocolDir = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 11))
protocolDist = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 12))
addressMap = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 13))
nlHost = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 14))
nlMatrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 15))
alHost = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 16))
alMatrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 17))
usrHistory = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 18))
probeConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 19))
rmonConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20))
class ZeroBasedCounter32(TextualConvention, Gauge32):
    status = 'current'

class LastCreateTime(TimeStamp):
    status = 'current'

class TimeFilter(TextualConvention, TimeTicks):
    status = 'current'

class DataSource(TextualConvention, ObjectIdentifier):
    status = 'current'

mibBuilder.exportSymbols("RMON2-MIB", DataSource=DataSource, rmon=rmon, protocolDist=protocolDist, usrHistory=usrHistory, alMatrix=alMatrix, ZeroBasedCounter32=ZeroBasedCounter32, LastCreateTime=LastCreateTime, nlHost=nlHost, probeConfig=probeConfig, PYSNMP_MODULE_ID=rmon, addressMap=addressMap, rmonConformance=rmonConformance, nlMatrix=nlMatrix, protocolDir=protocolDir, TimeFilter=TimeFilter, alHost=alHost)
