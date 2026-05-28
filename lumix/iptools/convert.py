import ipaddress


def cidr_to_range(cidr: str) -> tuple:
    """
    Data una notazione CIDR (es. '192.168.1.0/24'), restituisce il primo e l'ultimo indirizzo IP.
    """
    net = ipaddress.ip_network(cidr, strict=False)
    return str(net.network_address), str(net.broadcast_address)

def ip_to_bin(ip: str) -> str:
    """
    Converte un indirizzo IPv4 in rappresentazione binaria a 32 bit (punti ogni 8 bit).
    """
    ip_obj = ipaddress.ip_address(ip)
    # Ottiene la rappresentazione binaria come intero, poi formatta
    bin_str = format(int(ip_obj), '032b')
    # Inserisce un punto ogni 8 bit per leggibilità
    return '.'.join(bin_str[i:i+8] for i in range(0, 32, 8))

def bin_to_ip(bin_str: str) -> str:
    """
    Converte una stringa binaria di 32 bit (con o senza punti) in indirizzo IPv4.
    """
    # Rimuovi eventuali punti
    clean = bin_str.replace('.', '')
    if len(clean) != 32 or not all(c in '01' for c in clean):
        raise ValueError("La stringa binaria deve essere di 32 bit (solo 0 e 1)")
    ip_int = int(clean, 2)
    return str(ipaddress.ip_address(ip_int))

def netmask_from_cidr(cidr: str) -> str:
    """
    Restituisce la netmask in dotted decimal da una notazione CIDR.
    """
    net = ipaddress.ip_network(cidr, strict=False)
    return str(net.netmask)

def subnet_info(cidr: str) -> dict:
    """
    Restituisce un dizionario con informazioni sulla subnet.
    """
    net = ipaddress.ip_network(cidr, strict=False)
    return {
        'network': str(net.network_address),
        'netmask': str(net.netmask),
        'broadcast': str(net.broadcast_address),
        'num_hosts': net.num_addresses - 2 if net.num_addresses > 2 else 0,
        'wildcard': str(net.hostmask),
    }
