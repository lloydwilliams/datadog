#
# PySNMP MIB module ARUBA-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/mibdump/asn1/ARUBA-MGMT-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:13:51 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
arubaMgmt, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMgmt")
ArubaEnableValue, = mibBuilder.importSymbols("ARUBA-TC", "ArubaEnableValue")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Bits, snmpModules, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectName, TimeTicks, NotificationType, Unsigned32, iso, IpAddress, Counter32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Bits", "snmpModules", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectName", "TimeTicks", "NotificationType", "Unsigned32", "iso", "IpAddress", "Counter32", "ObjectIdentity", "Counter64")
DisplayString, PhysAddress, TestAndIncr, TruthValue, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TestAndIncr", "TruthValue", "TimeStamp", "TextualConvention")
arubaMgmtExtensions = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 3, 3))
if mibBuilder.loadTexts: arubaMgmtExtensions.setLastUpdated('0804160206Z')
if mibBuilder.loadTexts: arubaMgmtExtensions.setOrganization('Aruba Wireless Networks')
arubaMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1))
arubaGetTable = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: arubaGetTable.setStatus('current')
arubaNumberOfRows = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: arubaNumberOfRows.setStatus('current')
arubaRowInstance = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 3), ObjectIdentifier())
if mibBuilder.loadTexts: arubaRowInstance.setStatus('current')
arubaGetTableStatus = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("endTable", 1), ("moreTable", 2), ("retrieveError", 3), ("noAmpSupport", 4), ("invalidColumnID", 5), ("resourceAllocationFailure", 6))))
if mibBuilder.loadTexts: arubaGetTableStatus.setStatus('current')
arubaNumberOfColumns = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: arubaNumberOfColumns.setStatus('current')
arubaSwitchAMPSupport = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 6), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaSwitchAMPSupport.setStatus('current')
mibBuilder.exportSymbols("ARUBA-MGMT-MIB", arubaSwitchAMPSupport=arubaSwitchAMPSupport, arubaGetTableStatus=arubaGetTableStatus, arubaMgmtExtensions=arubaMgmtExtensions, arubaGetTable=arubaGetTable, arubaNumberOfRows=arubaNumberOfRows, PYSNMP_MODULE_ID=arubaMgmtExtensions, arubaMgmtGroup=arubaMgmtGroup, arubaNumberOfColumns=arubaNumberOfColumns, arubaRowInstance=arubaRowInstance)
