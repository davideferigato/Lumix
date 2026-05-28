from lumix.iptools.convert import bin_to_ip, cidr_to_range, ip_to_bin, netmask_from_cidr


def test_cidr_to_range():
    first, last = cidr_to_range("192.168.1.0/24")
    assert first == "192.168.1.0"
    assert last == "192.168.1.255"

def test_ip_to_bin():
    assert ip_to_bin("192.168.1.1") == "11000000.10101000.00000001.00000001"

def test_bin_to_ip():
    assert bin_to_ip("11000000.10101000.00000001.00000001") == "192.168.1.1"

def test_netmask_from_cidr():
    assert netmask_from_cidr("192.168.1.0/24") == "255.255.255.0"

