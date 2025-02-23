#
# PySNMP MIB module WLSX-SYSTEMEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/mibdump/asn1/WLSX-SYSTEMEXT-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:14:01 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ArubaCardType, ArubaActiveState, ArubaSwitchRole = mibBuilder.importSymbols("ARUBA-TC", "ArubaCardType", "ArubaActiveState", "ArubaSwitchRole")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, MibIdentifier, Integer32, iso, Counter64, Unsigned32, snmpModules, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "MibIdentifier", "Integer32", "iso", "Counter64", "Unsigned32", "snmpModules", "Bits")
TextualConvention, DisplayString, MacAddress, TruthValue, TestAndIncr, RowStatus, TDomain, StorageType, TAddress, PhysAddress, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "TruthValue", "TestAndIncr", "RowStatus", "TDomain", "StorageType", "TAddress", "PhysAddress", "TimeInterval")
wlsxSystemExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2))
wlsxSystemExtMIB.setRevisions(('1908-12-11 21:08',))
if mibBuilder.loadTexts: wlsxSystemExtMIB.setLastUpdated('0812112108Z')
if mibBuilder.loadTexts: wlsxSystemExtMIB.setOrganization('Aruba Wireless Networks')
wlsxSystemExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1))
wlsxSystemExtTableGenNumberGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2))
wlsxSysExtSwitchIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchIp.setStatus('current')
wlsxSysExtHostname = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtHostname.setStatus('current')
wlsxSysExtModelName = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtModelName.setStatus('current')
wlsxSysExtSwitchRole = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 4), ArubaSwitchRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchRole.setStatus('current')
wlsxSysExtSwitchMasterIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchMasterIp.setStatus('current')
wlsxSysExtSwitchDate = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxSysExtSwitchDate.setStatus('current')
wlsxSysExtSwitchBaseMacaddress = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchBaseMacaddress.setStatus('current')
wlsxSysExtFanTrayAssemblyNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtFanTrayAssemblyNumber.setStatus('current')
wlsxSysExtFanTraySerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtFanTraySerialNumber.setStatus('current')
wlsxSysExtInternalTemparature = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtInternalTemparature.setStatus('current')
wlsxSysExtLicenseSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLicenseSerialNumber.setStatus('current')
wlsxSysExtSwitchLicenseCount = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseCount.setStatus('current')
wlsxSysExtProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13), )
if mibBuilder.loadTexts: wlsxSysExtProcessorTable.setStatus('current')
wlsxSysExtProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtProcessorID"))
if mibBuilder.loadTexts: wlsxSysExtProcessorEntry.setStatus('current')
sysExtProcessorID = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtProcessorID.setStatus('current')
sysExtProcessorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtProcessorDescr.setStatus('current')
sysExtProcessorLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtProcessorLoad.setStatus('current')
wlsxSysExtStorageTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14), )
if mibBuilder.loadTexts: wlsxSysExtStorageTable.setStatus('current')
wlsxSysExtStorageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtStorageIndex"))
if mibBuilder.loadTexts: wlsxSysExtStorageEntry.setStatus('current')
sysExtStorageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtStorageIndex.setStatus('current')
sysExtStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ram", 1), ("flashMemory", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageType.setStatus('current')
sysExtStorageSize = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageSize.setStatus('current')
sysExtStorageUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageUsed.setStatus('current')
sysExtStorageName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtStorageName.setStatus('current')
wlsxSysExtMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15), )
if mibBuilder.loadTexts: wlsxSysExtMemoryTable.setStatus('current')
wlsxSysExtMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtMemoryIndex"))
if mibBuilder.loadTexts: wlsxSysExtMemoryEntry.setStatus('current')
sysExtMemoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtMemoryIndex.setStatus('current')
sysExtMemorySize = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemorySize.setStatus('current')
sysExtMemoryUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemoryUsed.setStatus('current')
sysExtMemoryFree = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtMemoryFree.setStatus('current')
wlsxSysExtCardTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16), )
if mibBuilder.loadTexts: wlsxSysExtCardTable.setStatus('current')
wlsxSysExtCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtCardSlot"))
if mibBuilder.loadTexts: wlsxSysExtCardEntry.setStatus('current')
sysExtCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtCardSlot.setStatus('current')
sysExtCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 2), ArubaCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardType.setStatus('current')
sysExtCardNumOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfPorts.setStatus('current')
sysExtCardNumOfFastethernetPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfFastethernetPorts.setStatus('current')
sysExtCardNumOfGigPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardNumOfGigPorts.setStatus('current')
sysExtCardSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardSerialNo.setStatus('current')
sysExtCardAssemblyNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardAssemblyNo.setStatus('current')
sysExtCardManufacturingDate = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardManufacturingDate.setStatus('current')
sysExtCardHwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardHwRevision.setStatus('current')
sysExtCardFpgaRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardFpgaRevision.setStatus('current')
sysExtCardSwitchChip = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardSwitchChip.setStatus('current')
sysExtCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 12), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardStatus.setStatus('current')
sysExtCardUserSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardUserSlot.setStatus('current')
sysExtCardServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardServiceTag.setStatus('current')
sysExtCardPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtCardPartNumber.setStatus('current')
wlsxSysExtFanTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17), )
if mibBuilder.loadTexts: wlsxSysExtFanTable.setStatus('current')
wlsxSysExtFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtFanIndex"))
if mibBuilder.loadTexts: wlsxSysExtFanEntry.setStatus('current')
sysExtFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtFanIndex.setStatus('current')
sysExtFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 2), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtFanStatus.setStatus('current')
wlsxSysExtPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18), )
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyTable.setStatus('current')
wlsxSysExtPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtPowerSupplyIndex"))
if mibBuilder.loadTexts: wlsxSysExtPowerSupplyEntry.setStatus('current')
sysExtPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtPowerSupplyIndex.setStatus('current')
sysExtPowerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 2), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtPowerSupplyStatus.setStatus('current')
wlsxSysExtSwitchListTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19), )
if mibBuilder.loadTexts: wlsxSysExtSwitchListTable.setStatus('current')
wlsxSysExtSwitchListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtSwitchIPAddress"))
if mibBuilder.loadTexts: wlsxSysExtSwitchListEntry.setStatus('current')
sysExtSwitchIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 1), IpAddress())
if mibBuilder.loadTexts: sysExtSwitchIPAddress.setStatus('current')
sysExtSwitchRole = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 2), ArubaSwitchRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchRole.setStatus('current')
sysExtSwitchLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchLocation.setStatus('current')
sysExtSwitchSWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchSWVersion.setStatus('current')
sysExtSwitchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 5), ArubaActiveState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchStatus.setStatus('current')
sysExtSwitchName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchName.setStatus('current')
sysExtSwitchSerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtSwitchSerNo.setStatus('current')
wlsxSysExtSwitchLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20), )
if mibBuilder.loadTexts: wlsxSysExtSwitchLicenseTable.setStatus('current')
wlsxSysExtLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1), ).setIndexNames((0, "WLSX-SYSTEMEXT-MIB", "sysExtLicenseIndex"))
if mibBuilder.loadTexts: wlsxSysExtLicenseEntry.setStatus('current')
sysExtLicenseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 1), Integer32())
if mibBuilder.loadTexts: sysExtLicenseIndex.setStatus('current')
sysExtLicenseKey = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseKey.setStatus('current')
sysExtLicenseInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseInstalled.setStatus('current')
sysExtLicenseExpires = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseExpires.setStatus('current')
sysExtLicenseFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseFlags.setStatus('current')
sysExtLicenseService = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysExtLicenseService.setStatus('current')
wlsxSysExtMMSCompatLevel = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMMSCompatLevel.setStatus('current')
wlsxSysExtMMSConfigID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMMSConfigID.setStatus('current')
wlsxSysExtControllerConfigID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtControllerConfigID.setStatus('current')
wlsxSysExtIsMMSConfigUpdateEnabled = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 24), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxSysExtIsMMSConfigUpdateEnabled.setStatus('current')
wlsxSysExtSwitchLastReload = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchLastReload.setStatus('current')
wlsxSysExtLastStatsReset = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 26), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLastStatsReset.setStatus('current')
wlsxSysExtHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtHwVersion.setStatus('current')
wlsxSysExtSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwVersion.setStatus('current')
wlsxSysExtSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSerialNumber.setStatus('current')
wlsxSysExtCpuUsedPercent = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 30), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtCpuUsedPercent.setStatus('current')
wlsxSysExtMemoryUsedPercent = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 31), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMemoryUsedPercent.setStatus('current')
wlsxSysExtPacketLossPercent = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 32), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtPacketLossPercent.setStatus('current')
wlsxSysExtUserTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtUserTableGenNumber.setStatus('deprecated')
wlsxSysExtAPBssidTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPBssidTableGenNumber.setStatus('deprecated')
wlsxSysExtAPRadioTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPRadioTableGenNumber.setStatus('deprecated')
wlsxSysExtAPTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtAPTableGenNumber.setStatus('deprecated')
wlsxSysExtSwitchListTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtSwitchListTableGenNumber.setStatus('deprecated')
wlsxSysExtPortTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtPortTableGenNumber.setStatus('deprecated')
wlsxSysExtVlanTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtVlanTableGenNumber.setStatus('deprecated')
wlsxSysExtVlanInterfaceTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtVlanInterfaceTableGenNumber.setStatus('deprecated')
wlsxSysExtLicenseTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtLicenseTableGenNumber.setStatus('deprecated')
wlsxSysExtMonAPTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMonAPTableGenNumber.setStatus('deprecated')
wlsxSysExtMonStationTableGenNumber = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtMonStationTableGenNumber.setStatus('deprecated')
wlsxSysExtPoweredViaPoe = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxSysExtPoweredViaPoe.setStatus('current')
wlsxAuthFailIp = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 38), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxAuthFailIp.setStatus('current')
mibBuilder.exportSymbols("WLSX-SYSTEMEXT-MIB", wlsxSysExtPowerSupplyEntry=wlsxSysExtPowerSupplyEntry, sysExtSwitchSWVersion=sysExtSwitchSWVersion, wlsxSysExtPoweredViaPoe=wlsxSysExtPoweredViaPoe, wlsxSysExtPortTableGenNumber=wlsxSysExtPortTableGenNumber, sysExtCardServiceTag=sysExtCardServiceTag, sysExtMemorySize=sysExtMemorySize, wlsxSysExtSwitchRole=wlsxSysExtSwitchRole, wlsxSysExtStorageTable=wlsxSysExtStorageTable, wlsxSysExtFanEntry=wlsxSysExtFanEntry, sysExtSwitchLocation=sysExtSwitchLocation, sysExtLicenseExpires=sysExtLicenseExpires, wlsxSysExtCardTable=wlsxSysExtCardTable, wlsxSysExtSwitchMasterIp=wlsxSysExtSwitchMasterIp, wlsxSysExtHwVersion=wlsxSysExtHwVersion, sysExtLicenseKey=sysExtLicenseKey, sysExtSwitchIPAddress=sysExtSwitchIPAddress, wlsxSysExtSwitchListEntry=wlsxSysExtSwitchListEntry, sysExtStorageSize=sysExtStorageSize, wlsxSysExtIsMMSConfigUpdateEnabled=wlsxSysExtIsMMSConfigUpdateEnabled, wlsxSysExtMonAPTableGenNumber=wlsxSysExtMonAPTableGenNumber, wlsxSysExtLicenseTableGenNumber=wlsxSysExtLicenseTableGenNumber, wlsxSysExtStorageEntry=wlsxSysExtStorageEntry, sysExtCardSerialNo=sysExtCardSerialNo, wlsxSysExtFanTraySerialNumber=wlsxSysExtFanTraySerialNumber, wlsxSysExtPowerSupplyTable=wlsxSysExtPowerSupplyTable, wlsxSysExtSwitchLicenseTable=wlsxSysExtSwitchLicenseTable, sysExtLicenseInstalled=sysExtLicenseInstalled, wlsxSysExtFanTable=wlsxSysExtFanTable, wlsxSysExtAPBssidTableGenNumber=wlsxSysExtAPBssidTableGenNumber, sysExtMemoryUsed=sysExtMemoryUsed, sysExtCardAssemblyNo=sysExtCardAssemblyNo, wlsxSysExtLastStatsReset=wlsxSysExtLastStatsReset, wlsxSysExtCpuUsedPercent=wlsxSysExtCpuUsedPercent, wlsxSysExtSwitchDate=wlsxSysExtSwitchDate, wlsxSysExtVlanTableGenNumber=wlsxSysExtVlanTableGenNumber, wlsxSysExtUserTableGenNumber=wlsxSysExtUserTableGenNumber, wlsxSysExtFanTrayAssemblyNumber=wlsxSysExtFanTrayAssemblyNumber, PYSNMP_MODULE_ID=wlsxSystemExtMIB, sysExtLicenseFlags=sysExtLicenseFlags, sysExtSwitchSerNo=sysExtSwitchSerNo, wlsxSysExtLicenseSerialNumber=wlsxSysExtLicenseSerialNumber, wlsxSysExtAPRadioTableGenNumber=wlsxSysExtAPRadioTableGenNumber, sysExtStorageUsed=sysExtStorageUsed, wlsxSysExtLicenseEntry=wlsxSysExtLicenseEntry, wlsxSysExtSwitchBaseMacaddress=wlsxSysExtSwitchBaseMacaddress, sysExtMemoryFree=sysExtMemoryFree, wlsxSysExtSwVersion=wlsxSysExtSwVersion, sysExtSwitchRole=sysExtSwitchRole, sysExtCardNumOfGigPorts=sysExtCardNumOfGigPorts, sysExtFanIndex=sysExtFanIndex, wlsxSystemExtTableGenNumberGroup=wlsxSystemExtTableGenNumberGroup, wlsxSysExtMMSCompatLevel=wlsxSysExtMMSCompatLevel, sysExtCardNumOfFastethernetPorts=sysExtCardNumOfFastethernetPorts, wlsxSysExtMemoryEntry=wlsxSysExtMemoryEntry, sysExtCardFpgaRevision=sysExtCardFpgaRevision, wlsxSysExtSwitchLastReload=wlsxSysExtSwitchLastReload, sysExtMemoryIndex=sysExtMemoryIndex, sysExtCardManufacturingDate=sysExtCardManufacturingDate, sysExtStorageType=sysExtStorageType, wlsxSystemExtMIB=wlsxSystemExtMIB, sysExtLicenseIndex=sysExtLicenseIndex, wlsxSysExtSwitchListTableGenNumber=wlsxSysExtSwitchListTableGenNumber, wlsxSysExtSerialNumber=wlsxSysExtSerialNumber, sysExtPowerSupplyIndex=sysExtPowerSupplyIndex, sysExtCardStatus=sysExtCardStatus, wlsxSysExtModelName=wlsxSysExtModelName, sysExtCardType=sysExtCardType, wlsxSysExtPacketLossPercent=wlsxSysExtPacketLossPercent, sysExtSwitchStatus=sysExtSwitchStatus, sysExtProcessorDescr=sysExtProcessorDescr, wlsxSysExtMonStationTableGenNumber=wlsxSysExtMonStationTableGenNumber, wlsxSysExtInternalTemparature=wlsxSysExtInternalTemparature, wlsxSysExtMMSConfigID=wlsxSysExtMMSConfigID, wlsxSysExtControllerConfigID=wlsxSysExtControllerConfigID, wlsxSysExtVlanInterfaceTableGenNumber=wlsxSysExtVlanInterfaceTableGenNumber, sysExtProcessorLoad=sysExtProcessorLoad, wlsxSysExtHostname=wlsxSysExtHostname, sysExtLicenseService=sysExtLicenseService, sysExtCardPartNumber=sysExtCardPartNumber, sysExtCardHwRevision=sysExtCardHwRevision, wlsxSysExtSwitchListTable=wlsxSysExtSwitchListTable, sysExtCardUserSlot=sysExtCardUserSlot, wlsxSysExtAPTableGenNumber=wlsxSysExtAPTableGenNumber, sysExtStorageIndex=sysExtStorageIndex, wlsxSysExtSwitchLicenseCount=wlsxSysExtSwitchLicenseCount, wlsxSysExtProcessorEntry=wlsxSysExtProcessorEntry, sysExtFanStatus=sysExtFanStatus, wlsxSysExtCardEntry=wlsxSysExtCardEntry, wlsxSysExtMemoryTable=wlsxSysExtMemoryTable, wlsxAuthFailIp=wlsxAuthFailIp, sysExtCardSlot=sysExtCardSlot, wlsxSystemExtGroup=wlsxSystemExtGroup, wlsxSysExtProcessorTable=wlsxSysExtProcessorTable, sysExtSwitchName=sysExtSwitchName, sysExtPowerSupplyStatus=sysExtPowerSupplyStatus, wlsxSysExtMemoryUsedPercent=wlsxSysExtMemoryUsedPercent, sysExtStorageName=sysExtStorageName, sysExtCardNumOfPorts=sysExtCardNumOfPorts, sysExtProcessorID=sysExtProcessorID, wlsxSysExtSwitchIp=wlsxSysExtSwitchIp, sysExtCardSwitchChip=sysExtCardSwitchChip)
