#
# PySNMP MIB module LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/github/mibs.snmplabs.com/asn1/LLDP-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:13:59 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
TimeFilter, ZeroBasedCounter32 = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter", "ZeroBasedCounter32")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32, iso, MibIdentifier, Counter32, Bits, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32", "iso", "MibIdentifier", "Counter32", "Bits", "Counter64", "IpAddress")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
lldpMIB = ModuleIdentity((1, 0, 8802, 1, 1, 2))
lldpMIB.setRevisions(('2005-05-06 00:00',))
if mibBuilder.loadTexts: lldpMIB.setLastUpdated('200505060000Z')
if mibBuilder.loadTexts: lldpMIB.setOrganization('IEEE 802.1 Working Group')
lldpNotifications = MibIdentifier((1, 0, 8802, 1, 1, 2, 0))
lldpObjects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1))
lldpConformance = MibIdentifier((1, 0, 8802, 1, 1, 2, 2))
lldpConfiguration = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 1))
lldpStatistics = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 2))
lldpLocalSystemData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 3))
lldpRemoteSystemsData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 4))
lldpExtensions = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5))
class LldpChassisIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class LldpChassisId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpPortIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class LldpPortId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpManAddrIfSubtype(TextualConvention, Integer32):
    reference = 'IEEE 802.1AB-2005 9.5.9.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3))

class LldpManAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class LldpSystemCapabilitiesMap(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("other", 0), ("repeater", 1), ("bridge", 2), ("wlanAccessPoint", 3), ("router", 4), ("telephone", 5), ("docsisCableDevice", 6), ("stationOnly", 7))

class LldpPortNumber(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4096)

class LldpPortList(TextualConvention, OctetString):
    reference = 'IETF RFC 2674 section 5'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 512)

lldpMessageTxInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 32768)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpMessageTxInterval.setStatus('current')
lldpMessageTxHoldMultiplier = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpMessageTxHoldMultiplier.setStatus('current')
lldpReinitDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpReinitDelay.setStatus('current')
lldpTxDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8192)).clone(2)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpTxDelay.setStatus('current')
lldpNotificationInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpNotificationInterval.setStatus('current')
lldpPortConfigTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 6), )
if mibBuilder.loadTexts: lldpPortConfigTable.setStatus('current')
lldpPortConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1), ).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
if mibBuilder.loadTexts: lldpPortConfigEntry.setStatus('current')
lldpPortConfigPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpPortConfigPortNum.setStatus('current')
lldpPortConfigAdminStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4))).clone('txAndRx')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpPortConfigAdminStatus.setStatus('current')
lldpPortConfigNotificationEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpPortConfigNotificationEnable.setStatus('current')
lldpPortConfigTLVsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 4), Bits().clone(namedValues=NamedValues(("portDesc", 0), ("sysName", 1), ("sysDesc", 2), ("sysCap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpPortConfigTLVsTxEnable.setStatus('current')
lldpConfigManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 7), )
if mibBuilder.loadTexts: lldpConfigManAddrTable.setStatus('current')
lldpConfigManAddrPortsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1, 1), LldpPortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpConfigManAddrPortsTxEnable.setStatus('current')
lldpStatsRemTablesLastChangeTime = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesLastChangeTime.setStatus('current')
lldpStatsRemTablesInserts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 2), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesInserts.setStatus('current')
lldpStatsRemTablesDeletes = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 3), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesDeletes.setStatus('current')
lldpStatsRemTablesDrops = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 4), ZeroBasedCounter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesDrops.setStatus('current')
lldpStatsRemTablesAgeouts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 5), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRemTablesAgeouts.setStatus('current')
lldpStatsTxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 6), )
if mibBuilder.loadTexts: lldpStatsTxPortTable.setStatus('current')
lldpStatsTxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1), ).setIndexNames((0, "LLDP-MIB", "lldpStatsTxPortNum"))
if mibBuilder.loadTexts: lldpStatsTxPortEntry.setStatus('current')
lldpStatsTxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpStatsTxPortNum.setStatus('current')
lldpStatsTxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsTxPortFramesTotal.setStatus('current')
lldpStatsRxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 7), )
if mibBuilder.loadTexts: lldpStatsRxPortTable.setStatus('current')
lldpStatsRxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1), ).setIndexNames((0, "LLDP-MIB", "lldpStatsRxPortNum"))
if mibBuilder.loadTexts: lldpStatsRxPortEntry.setStatus('current')
lldpStatsRxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpStatsRxPortNum.setStatus('current')
lldpStatsRxPortFramesDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortFramesDiscardedTotal.setStatus('current')
lldpStatsRxPortFramesErrors = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortFramesErrors.setStatus('current')
lldpStatsRxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortFramesTotal.setStatus('current')
lldpStatsRxPortTLVsDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortTLVsDiscardedTotal.setStatus('current')
lldpStatsRxPortTLVsUnrecognizedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortTLVsUnrecognizedTotal.setStatus('current')
lldpStatsRxPortAgeoutsTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpStatsRxPortAgeoutsTotal.setStatus('current')
lldpLocChassisIdSubtype = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 1), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocChassisIdSubtype.setStatus('current')
lldpLocChassisId = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 2), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocChassisId.setStatus('current')
lldpLocSysName = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysName.setStatus('current')
lldpLocSysDesc = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysDesc.setStatus('current')
lldpLocSysCapSupported = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 5), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysCapSupported.setStatus('current')
lldpLocSysCapEnabled = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 6), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocSysCapEnabled.setStatus('current')
lldpLocPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 7), )
if mibBuilder.loadTexts: lldpLocPortTable.setStatus('current')
lldpLocPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpLocPortEntry.setStatus('current')
lldpLocPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: lldpLocPortNum.setStatus('current')
lldpLocPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 2), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocPortIdSubtype.setStatus('current')
lldpLocPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 3), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocPortId.setStatus('current')
lldpLocPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocPortDesc.setStatus('current')
lldpLocManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 8), )
if mibBuilder.loadTexts: lldpLocManAddrTable.setStatus('current')
lldpLocManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocManAddrSubtype"), (0, "LLDP-MIB", "lldpLocManAddr"))
if mibBuilder.loadTexts: lldpLocManAddrEntry.setStatus('current')
lldpConfigManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1), )
lldpLocManAddrEntry.registerAugmentions(("LLDP-MIB", "lldpConfigManAddrEntry"))
lldpConfigManAddrEntry.setIndexNames(*lldpLocManAddrEntry.getIndexNames())
if mibBuilder.loadTexts: lldpConfigManAddrEntry.setStatus('current')
lldpLocManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: lldpLocManAddrSubtype.setStatus('current')
lldpLocManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 2), LldpManAddress())
if mibBuilder.loadTexts: lldpLocManAddr.setStatus('current')
lldpLocManAddrLen = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrLen.setStatus('current')
lldpLocManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 4), LldpManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrIfSubtype.setStatus('current')
lldpLocManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrIfId.setStatus('current')
lldpLocManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpLocManAddrOID.setStatus('current')
lldpRemTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 1), )
if mibBuilder.loadTexts: lldpRemTable.setStatus('current')
lldpRemEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpRemEntry.setStatus('current')
lldpRemTimeMark = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: lldpRemTimeMark.setStatus('current')
lldpRemLocalPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 2), LldpPortNumber())
if mibBuilder.loadTexts: lldpRemLocalPortNum.setStatus('current')
lldpRemIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpRemIndex.setStatus('current')
lldpRemChassisIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 4), LldpChassisIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemChassisIdSubtype.setStatus('current')
lldpRemChassisId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 5), LldpChassisId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemChassisId.setStatus('current')
lldpRemPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 6), LldpPortIdSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemPortIdSubtype.setStatus('current')
lldpRemPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 7), LldpPortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemPortId.setStatus('current')
lldpRemPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemPortDesc.setStatus('current')
lldpRemSysName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysName.setStatus('current')
lldpRemSysDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysDesc.setStatus('current')
lldpRemSysCapSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 11), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysCapSupported.setStatus('current')
lldpRemSysCapEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 12), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemSysCapEnabled.setStatus('current')
lldpRemManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 2), )
if mibBuilder.loadTexts: lldpRemManAddrTable.setStatus('current')
lldpRemManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemManAddrSubtype"), (0, "LLDP-MIB", "lldpRemManAddr"))
if mibBuilder.loadTexts: lldpRemManAddrEntry.setStatus('current')
lldpRemManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 1), AddressFamilyNumbers())
if mibBuilder.loadTexts: lldpRemManAddrSubtype.setStatus('current')
lldpRemManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 2), LldpManAddress())
if mibBuilder.loadTexts: lldpRemManAddr.setStatus('current')
lldpRemManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 3), LldpManAddrIfSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemManAddrIfSubtype.setStatus('current')
lldpRemManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemManAddrIfId.setStatus('current')
lldpRemManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemManAddrOID.setStatus('current')
lldpRemUnknownTLVTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 3), )
if mibBuilder.loadTexts: lldpRemUnknownTLVTable.setStatus('current')
lldpRemUnknownTLVEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemUnknownTLVType"))
if mibBuilder.loadTexts: lldpRemUnknownTLVEntry.setStatus('current')
lldpRemUnknownTLVType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(9, 126)))
if mibBuilder.loadTexts: lldpRemUnknownTLVType.setStatus('current')
lldpRemUnknownTLVInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemUnknownTLVInfo.setStatus('current')
lldpRemOrgDefInfoTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 4), )
if mibBuilder.loadTexts: lldpRemOrgDefInfoTable.setStatus('current')
lldpRemOrgDefInfoEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemOrgDefInfoOUI"), (0, "LLDP-MIB", "lldpRemOrgDefInfoSubtype"), (0, "LLDP-MIB", "lldpRemOrgDefInfoIndex"))
if mibBuilder.loadTexts: lldpRemOrgDefInfoEntry.setStatus('current')
lldpRemOrgDefInfoOUI = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3))
if mibBuilder.loadTexts: lldpRemOrgDefInfoOUI.setStatus('current')
lldpRemOrgDefInfoSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: lldpRemOrgDefInfoSubtype.setStatus('current')
lldpRemOrgDefInfoIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: lldpRemOrgDefInfoIndex.setStatus('current')
lldpRemOrgDefInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 507))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpRemOrgDefInfo.setStatus('current')
lldpNotificationPrefix = MibIdentifier((1, 0, 8802, 1, 1, 2, 0, 0))
lldpRemTablesChange = NotificationType((1, 0, 8802, 1, 1, 2, 0, 0, 1)).setObjects(("LLDP-MIB", "lldpStatsRemTablesInserts"), ("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"))
if mibBuilder.loadTexts: lldpRemTablesChange.setStatus('current')
lldpCompliances = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 1))
lldpGroups = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 2))
lldpCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 2, 2, 1, 1)).setObjects(("LLDP-MIB", "lldpConfigGroup"), ("LLDP-MIB", "lldpConfigRxGroup"), ("LLDP-MIB", "lldpConfigTxGroup"), ("LLDP-MIB", "lldpStatsRxGroup"), ("LLDP-MIB", "lldpStatsTxGroup"), ("LLDP-MIB", "lldpLocSysGroup"), ("LLDP-MIB", "lldpRemSysGroup"), ("LLDP-MIB", "lldpNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpCompliance = lldpCompliance.setStatus('current')
lldpConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 1)).setObjects(("LLDP-MIB", "lldpPortConfigAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpConfigGroup = lldpConfigGroup.setStatus('current')
lldpConfigRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 2)).setObjects(("LLDP-MIB", "lldpNotificationInterval"), ("LLDP-MIB", "lldpPortConfigNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpConfigRxGroup = lldpConfigRxGroup.setStatus('current')
lldpConfigTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 3)).setObjects(("LLDP-MIB", "lldpMessageTxInterval"), ("LLDP-MIB", "lldpMessageTxHoldMultiplier"), ("LLDP-MIB", "lldpReinitDelay"), ("LLDP-MIB", "lldpTxDelay"), ("LLDP-MIB", "lldpPortConfigTLVsTxEnable"), ("LLDP-MIB", "lldpConfigManAddrPortsTxEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpConfigTxGroup = lldpConfigTxGroup.setStatus('current')
lldpStatsRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 4)).setObjects(("LLDP-MIB", "lldpStatsRemTablesLastChangeTime"), ("LLDP-MIB", "lldpStatsRemTablesInserts"), ("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"), ("LLDP-MIB", "lldpStatsRxPortFramesDiscardedTotal"), ("LLDP-MIB", "lldpStatsRxPortFramesErrors"), ("LLDP-MIB", "lldpStatsRxPortFramesTotal"), ("LLDP-MIB", "lldpStatsRxPortTLVsDiscardedTotal"), ("LLDP-MIB", "lldpStatsRxPortTLVsUnrecognizedTotal"), ("LLDP-MIB", "lldpStatsRxPortAgeoutsTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpStatsRxGroup = lldpStatsRxGroup.setStatus('current')
lldpStatsTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 5)).setObjects(("LLDP-MIB", "lldpStatsTxPortFramesTotal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpStatsTxGroup = lldpStatsTxGroup.setStatus('current')
lldpLocSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 6)).setObjects(("LLDP-MIB", "lldpLocChassisIdSubtype"), ("LLDP-MIB", "lldpLocChassisId"), ("LLDP-MIB", "lldpLocPortIdSubtype"), ("LLDP-MIB", "lldpLocPortId"), ("LLDP-MIB", "lldpLocPortDesc"), ("LLDP-MIB", "lldpLocSysDesc"), ("LLDP-MIB", "lldpLocSysName"), ("LLDP-MIB", "lldpLocSysCapSupported"), ("LLDP-MIB", "lldpLocSysCapEnabled"), ("LLDP-MIB", "lldpLocManAddrLen"), ("LLDP-MIB", "lldpLocManAddrIfSubtype"), ("LLDP-MIB", "lldpLocManAddrIfId"), ("LLDP-MIB", "lldpLocManAddrOID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpLocSysGroup = lldpLocSysGroup.setStatus('current')
lldpRemSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 7)).setObjects(("LLDP-MIB", "lldpRemChassisIdSubtype"), ("LLDP-MIB", "lldpRemChassisId"), ("LLDP-MIB", "lldpRemPortIdSubtype"), ("LLDP-MIB", "lldpRemPortId"), ("LLDP-MIB", "lldpRemPortDesc"), ("LLDP-MIB", "lldpRemSysName"), ("LLDP-MIB", "lldpRemSysDesc"), ("LLDP-MIB", "lldpRemSysCapSupported"), ("LLDP-MIB", "lldpRemSysCapEnabled"), ("LLDP-MIB", "lldpRemManAddrIfSubtype"), ("LLDP-MIB", "lldpRemManAddrIfId"), ("LLDP-MIB", "lldpRemManAddrOID"), ("LLDP-MIB", "lldpRemUnknownTLVInfo"), ("LLDP-MIB", "lldpRemOrgDefInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpRemSysGroup = lldpRemSysGroup.setStatus('current')
lldpNotificationsGroup = NotificationGroup((1, 0, 8802, 1, 1, 2, 2, 2, 8)).setObjects(("LLDP-MIB", "lldpRemTablesChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpNotificationsGroup = lldpNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("LLDP-MIB", lldpPortConfigAdminStatus=lldpPortConfigAdminStatus, lldpPortConfigEntry=lldpPortConfigEntry, lldpRemTablesChange=lldpRemTablesChange, lldpConfigManAddrEntry=lldpConfigManAddrEntry, lldpRemUnknownTLVType=lldpRemUnknownTLVType, lldpLocPortDesc=lldpLocPortDesc, lldpLocPortNum=lldpLocPortNum, lldpConfigRxGroup=lldpConfigRxGroup, lldpStatsRxPortFramesDiscardedTotal=lldpStatsRxPortFramesDiscardedTotal, lldpExtensions=lldpExtensions, lldpStatsRxPortNum=lldpStatsRxPortNum, lldpRemOrgDefInfoSubtype=lldpRemOrgDefInfoSubtype, lldpStatsRemTablesInserts=lldpStatsRemTablesInserts, lldpPortConfigNotificationEnable=lldpPortConfigNotificationEnable, lldpStatsTxPortEntry=lldpStatsTxPortEntry, lldpConfigGroup=lldpConfigGroup, lldpRemPortId=lldpRemPortId, LldpPortNumber=LldpPortNumber, lldpRemSysName=lldpRemSysName, lldpRemOrgDefInfo=lldpRemOrgDefInfo, lldpLocSysGroup=lldpLocSysGroup, lldpStatsRxPortEntry=lldpStatsRxPortEntry, lldpStatsRxPortFramesErrors=lldpStatsRxPortFramesErrors, lldpStatsRxPortTLVsUnrecognizedTotal=lldpStatsRxPortTLVsUnrecognizedTotal, lldpMessageTxInterval=lldpMessageTxInterval, LldpSystemCapabilitiesMap=LldpSystemCapabilitiesMap, lldpStatsTxPortTable=lldpStatsTxPortTable, lldpGroups=lldpGroups, lldpLocChassisIdSubtype=lldpLocChassisIdSubtype, lldpStatsRemTablesLastChangeTime=lldpStatsRemTablesLastChangeTime, lldpRemManAddrOID=lldpRemManAddrOID, lldpConfigManAddrTable=lldpConfigManAddrTable, lldpLocManAddrEntry=lldpLocManAddrEntry, lldpStatsRemTablesAgeouts=lldpStatsRemTablesAgeouts, lldpRemChassisIdSubtype=lldpRemChassisIdSubtype, lldpNotificationInterval=lldpNotificationInterval, lldpLocManAddrLen=lldpLocManAddrLen, lldpNotificationsGroup=lldpNotificationsGroup, lldpLocManAddr=lldpLocManAddr, lldpRemManAddrIfSubtype=lldpRemManAddrIfSubtype, lldpConfigManAddrPortsTxEnable=lldpConfigManAddrPortsTxEnable, lldpRemEntry=lldpRemEntry, lldpLocManAddrTable=lldpLocManAddrTable, lldpRemUnknownTLVInfo=lldpRemUnknownTLVInfo, lldpPortConfigTLVsTxEnable=lldpPortConfigTLVsTxEnable, lldpRemOrgDefInfoIndex=lldpRemOrgDefInfoIndex, lldpNotificationPrefix=lldpNotificationPrefix, lldpRemManAddrEntry=lldpRemManAddrEntry, lldpCompliances=lldpCompliances, LldpChassisIdSubtype=LldpChassisIdSubtype, lldpLocPortId=lldpLocPortId, lldpRemLocalPortNum=lldpRemLocalPortNum, lldpRemOrgDefInfoEntry=lldpRemOrgDefInfoEntry, lldpMIB=lldpMIB, lldpRemUnknownTLVEntry=lldpRemUnknownTLVEntry, LldpPortList=LldpPortList, lldpRemOrgDefInfoTable=lldpRemOrgDefInfoTable, LldpPortIdSubtype=LldpPortIdSubtype, lldpStatsRemTablesDeletes=lldpStatsRemTablesDeletes, lldpRemManAddrIfId=lldpRemManAddrIfId, LldpManAddress=LldpManAddress, lldpRemChassisId=lldpRemChassisId, lldpStatistics=lldpStatistics, PYSNMP_MODULE_ID=lldpMIB, lldpRemTimeMark=lldpRemTimeMark, lldpStatsRxPortTable=lldpStatsRxPortTable, lldpPortConfigPortNum=lldpPortConfigPortNum, lldpStatsTxGroup=lldpStatsTxGroup, lldpLocalSystemData=lldpLocalSystemData, lldpObjects=lldpObjects, lldpMessageTxHoldMultiplier=lldpMessageTxHoldMultiplier, lldpLocManAddrSubtype=lldpLocManAddrSubtype, lldpCompliance=lldpCompliance, lldpStatsRxPortFramesTotal=lldpStatsRxPortFramesTotal, lldpReinitDelay=lldpReinitDelay, lldpConfigTxGroup=lldpConfigTxGroup, lldpStatsRemTablesDrops=lldpStatsRemTablesDrops, lldpLocPortIdSubtype=lldpLocPortIdSubtype, lldpStatsRxPortTLVsDiscardedTotal=lldpStatsRxPortTLVsDiscardedTotal, lldpRemoteSystemsData=lldpRemoteSystemsData, lldpRemSysDesc=lldpRemSysDesc, lldpLocManAddrOID=lldpLocManAddrOID, lldpStatsTxPortNum=lldpStatsTxPortNum, lldpNotifications=lldpNotifications, lldpLocManAddrIfSubtype=lldpLocManAddrIfSubtype, lldpRemSysCapSupported=lldpRemSysCapSupported, lldpRemSysCapEnabled=lldpRemSysCapEnabled, lldpRemManAddr=lldpRemManAddr, lldpRemUnknownTLVTable=lldpRemUnknownTLVTable, lldpStatsTxPortFramesTotal=lldpStatsTxPortFramesTotal, LldpChassisId=LldpChassisId, lldpRemManAddrTable=lldpRemManAddrTable, lldpLocPortEntry=lldpLocPortEntry, lldpLocChassisId=lldpLocChassisId, lldpRemIndex=lldpRemIndex, lldpRemSysGroup=lldpRemSysGroup, lldpRemOrgDefInfoOUI=lldpRemOrgDefInfoOUI, lldpStatsRxGroup=lldpStatsRxGroup, lldpRemPortIdSubtype=lldpRemPortIdSubtype, lldpStatsRxPortAgeoutsTotal=lldpStatsRxPortAgeoutsTotal, lldpLocSysCapEnabled=lldpLocSysCapEnabled, lldpLocSysName=lldpLocSysName, lldpLocSysDesc=lldpLocSysDesc, lldpPortConfigTable=lldpPortConfigTable, lldpRemPortDesc=lldpRemPortDesc, lldpLocManAddrIfId=lldpLocManAddrIfId, lldpLocPortTable=lldpLocPortTable, lldpRemTable=lldpRemTable, lldpLocSysCapSupported=lldpLocSysCapSupported, LldpManAddrIfSubtype=LldpManAddrIfSubtype, lldpConfiguration=lldpConfiguration, lldpRemManAddrSubtype=lldpRemManAddrSubtype, lldpConformance=lldpConformance, lldpTxDelay=lldpTxDelay, LldpPortId=LldpPortId)
