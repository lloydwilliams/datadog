#
# PySNMP MIB module IANA-ADDRESS-FAMILY-NUMBERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/lloyd.williams/u01/snmp/github/mibs.snmplabs.com/asn1/IANA-ADDRESS-FAMILY-NUMBERS-MIB
# Produced by pysmi-0.3.4 at Tue Jan 31 16:13:59 2023
# On host COMP-C02DW0E1ML87 platform Darwin version 21.6.0 by user lloyd.williams
# Using Python version 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Unsigned32, NotificationType, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32, iso, MibIdentifier, Counter32, Bits, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Unsigned32", "NotificationType", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32", "iso", "MibIdentifier", "Counter32", "Bits", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaAddressFamilyNumbers = ModuleIdentity((1, 3, 6, 1, 2, 1, 72))
ianaAddressFamilyNumbers.setRevisions(('2014-09-02 00:00', '2013-09-25 00:00', '2013-07-16 00:00', '2013-06-26 00:00', '2013-06-18 00:00', '2002-03-14 00:00', '2000-09-08 00:00', '2000-03-01 00:00', '2000-02-04 00:00', '1999-08-26 00:00',))
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setLastUpdated('201409020000Z')
if mibBuilder.loadTexts: ianaAddressFamilyNumbers.setOrganization('IANA')
class AddressFamilyNumbers(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 16384, 16385, 16386, 16387, 16388, 16389, 16390, 16391, 16392, 16393, 16394, 16395, 16396, 65535))
    namedValues = NamedValues(("other", 0), ("ipV4", 1), ("ipV6", 2), ("nsap", 3), ("hdlc", 4), ("bbn1822", 5), ("all802", 6), ("e163", 7), ("e164", 8), ("f69", 9), ("x121", 10), ("ipx", 11), ("appleTalk", 12), ("decnetIV", 13), ("banyanVines", 14), ("e164withNsap", 15), ("dns", 16), ("distinguishedName", 17), ("asNumber", 18), ("xtpOverIpv4", 19), ("xtpOverIpv6", 20), ("xtpNativeModeXTP", 21), ("fibreChannelWWPN", 22), ("fibreChannelWWNN", 23), ("gwid", 24), ("afi", 25), ("mplsTpSectionEndpointIdentifier", 26), ("mplsTpLspEndpointIdentifier", 27), ("mplsTpPseudowireEndpointIdentifier", 28), ("eigrpCommonServiceFamily", 16384), ("eigrpIpv4ServiceFamily", 16385), ("eigrpIpv6ServiceFamily", 16386), ("lispCanonicalAddressFormat", 16387), ("bgpLs", 16388), ("fortyeightBitMac", 16389), ("sixtyfourBitMac", 16390), ("oui", 16391), ("mac24", 16392), ("mac40", 16393), ("ipv664", 16394), ("rBridgePortID", 16395), ("trillNickname", 16396), ("reserved", 65535))

mibBuilder.exportSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", PYSNMP_MODULE_ID=ianaAddressFamilyNumbers, ianaAddressFamilyNumbers=ianaAddressFamilyNumbers, AddressFamilyNumbers=AddressFamilyNumbers)
