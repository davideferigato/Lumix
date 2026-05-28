#!/usr/bin/env python3
"""
Parser per il modulo iptools.
Sintassi: <lang> iptools <comando> <argomenti>
Comandi supportati:
  cidr-to-range <cidr>
  ip-to-bin <ip>
  bin-to-ip <bin>
  netmask <cidr>
  subnet-info <cidr>
"""
import sys

from .convert import (
    bin_to_ip,
    cidr_to_range,
    ip_to_bin,
    netmask_from_cidr,
    subnet_info,
)

SUPPORTED_COMMANDS = {
    'cidr-to-range': {'args': 1, 'func': cidr_to_range},
    'ip-to-bin': {'args': 1, 'func': ip_to_bin},
    'bin-to-ip': {'args': 1, 'func': bin_to_ip},
    'netmask': {'args': 1, 'func': netmask_from_cidr},
    'subnet-info': {'args': 1, 'func': subnet_info},
}

LANG_CONFIG = {
    'en': {
        'errors': {
            'syntax': "❌ Syntax: {lang} iptools <command> <arguments>",
            'unknown_cmd': "❌ Unknown command. Available: cidr-to-range, ip-to-bin, bin-to-ip, netmask, subnet-info",
            'arg_count': "❌ Wrong number of arguments for command '{cmd}'",
            'invalid_cidr': "❌ Invalid CIDR notation",
            'invalid_ip': "❌ Invalid IP address",
            'invalid_bin': "❌ Invalid binary string (must be 32 bits)",
        },
        'output': {
            'cidr-to-range': "First IP: {first}\nLast IP: {last}",
            'ip-to-bin': "{ip} → {binary}",
            'bin-to-ip': "{binary} → {ip}",
            'netmask': "Netmask for {cidr}: {mask}",
            'subnet-info': """Network: {network}
Netmask: {netmask}
Broadcast: {broadcast}
Hosts: {num_hosts}
Wildcard: {wildcard}""",
        }
    },
    'it': {
        'errors': {
            'syntax': "❌ Sintassi: {lang} iptools <comando> <argomenti>",
            'unknown_cmd': "❌ Comando sconosciuto. Disponibili: cidr-to-range, ip-to-bin, bin-to-ip, netmask, subnet-info",
            'arg_count': "❌ Numero di argomenti errato per il comando '{cmd}'",
            'invalid_cidr': "❌ Notazione CIDR non valida",
            'invalid_ip': "❌ Indirizzo IP non valido",
            'invalid_bin': "❌ Stringa binaria non valida (deve essere 32 bit)",
        },
        'output': {
            'cidr-to-range': "Primo IP: {first}\nUltimo IP: {last}",
            'ip-to-bin': "{ip} → {binary}",
            'bin-to-ip': "{binary} → {ip}",
            'netmask': "Maschera per {cidr}: {mask}",
            'subnet-info': """Rete: {network}
Maschera: {netmask}
Broadcast: {broadcast}
Host: {num_hosts}
Wildcard: {wildcard}""",
        }
    },
    'fr': {
        'errors': {
            'syntax': "❌ Syntaxe : {lang} iptools <commande> <arguments>",
            'unknown_cmd': "❌ Commande inconnue. Disponibles : cidr-to-range, ip-to-bin, bin-to-ip, netmask, subnet-info",
            'arg_count': "❌ Nombre d'arguments incorrect pour la commande '{cmd}'",
            'invalid_cidr': "❌ Notation CIDR invalide",
            'invalid_ip': "❌ Adresse IP invalide",
            'invalid_bin': "❌ Chaîne binaire invalide (doit être 32 bits)",
        },
        'output': {
            'cidr-to-range': "Premier IP : {first}\nDernier IP : {last}",
            'ip-to-bin': "{ip} → {binary}",
            'bin-to-ip': "{binary} → {ip}",
            'netmask': "Masque pour {cidr} : {mask}",
            'subnet-info': """Réseau : {network}
Masque : {netmask}
Broadcast : {broadcast}
Hôtes : {num_hosts}
Wildcard : {wildcard}""",
        }
    },
    'es': {
        'errors': {
            'syntax': "❌ Sintaxis: {lang} iptools <comando> <argumentos>",
            'unknown_cmd': "❌ Comando desconocido. Disponibles: cidr-to-range, ip-to-bin, bin-to-ip, netmask, subnet-info",
            'arg_count': "❌ Número de argumentos incorrecto para el comando '{cmd}'",
            'invalid_cidr': "� Notación CIDR inválida",
            'invalid_ip': "❌ Dirección IP inválida",
            'invalid_bin': "❌ Cadena binaria inválida (debe ser 32 bits)",
        },
        'output': {
            'cidr-to-range': "Primer IP: {first}\nÚltimo IP: {last}",
            'ip-to-bin': "{ip} → {binary}",
            'bin-to-ip': "{binary} → {ip}",
            'netmask': "Máscara para {cidr}: {mask}",
            'subnet-info': """Red: {network}
Máscara: {netmask}
Broadcast: {broadcast}
Hosts: {num_hosts}
Wildcard: {wildcard}""",
        }
    },
    'jp': {
        'errors': {
            'syntax': "❌ 構文: {lang} iptools <コマンド> <引数>",
            'unknown_cmd': "❌ 不明なコマンド。利用可能: cidr-to-range, ip-to-bin, bin-to-ip, netmask, subnet-info",
            'arg_count': "❌ コマンド '{cmd}' の引数が正しくありません",
            'invalid_cidr': "❌ 無効なCIDR表記",
            'invalid_ip': "❌ 無効なIPアドレス",
            'invalid_bin': "❌ 無効なバイナリ文字列（32ビットである必要があります）",
        },
        'output': {
            'cidr-to-range': "最初のIP: {first}\n最後のIP: {last}",
            'ip-to-bin': "{ip} → {binary}",
            'bin-to-ip': "{binary} → {ip}",
            'netmask': "{cidr} のネットマスク: {mask}",
            'subnet-info': """ネットワーク: {network}
ネットマスク: {netmask}
ブロードキャスト: {broadcast}
ホスト数: {num_hosts}
ワイルドカード: {wildcard}""",
        }
    },
}

# noqa: C901
def parse(lang: str, params: str):  # noqa: C901  # noqa: C901
    cfg = LANG_CONFIG.get(lang)
    if not cfg:
        print(f"❌ Lingua non supportata: {lang}")
        sys.exit(1)

    parts = params.split()
    if len(parts) < 1:
        print(cfg['errors']['syntax'].format(lang=lang))
        sys.exit(1)

    cmd = parts[0]
    args = parts[1:]

    if cmd not in SUPPORTED_COMMANDS:
        print(cfg['errors']['unknown_cmd'])
        sys.exit(1)

    cmd_info = SUPPORTED_COMMANDS[cmd]
    if len(args) != cmd_info['args']:
        print(cfg['errors']['arg_count'].format(cmd=cmd))
        sys.exit(1)

    try:
        if cmd == 'cidr-to-range':
            first, last = cmd_info['func'](args[0])
            print(cfg['output'][cmd].format(first=first, last=last))
        elif cmd == 'ip-to-bin':
            binary = cmd_info['func'](args[0])
            print(cfg['output'][cmd].format(ip=args[0], binary=binary))
        elif cmd == 'bin-to-ip':
            ip = cmd_info['func'](args[0])
            print(cfg['output'][cmd].format(binary=args[0], ip=ip))
        elif cmd == 'netmask':
            mask = cmd_info['func'](args[0])
            print(cfg['output'][cmd].format(cidr=args[0], mask=mask))
        elif cmd == 'subnet-info':
            info = cmd_info['func'](args[0])
            print(cfg['output'][cmd].format(**info))
    except ValueError as e:
        # Mappa l'eccezione al tipo di errore
        if 'CIDR' in str(e) or 'network' in str(e):
            print(cfg['errors']['invalid_cidr'])
        elif 'address' in str(e):
            print(cfg['errors']['invalid_ip'])
        elif 'binary' in str(e).lower():
            print(cfg['errors']['invalid_bin'])
        else:
            print(f"❌ Errore: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: iptools_parser.py <lang> '<params>'")
        sys.exit(1)
    lang = sys.argv[1]
    params = sys.argv[2]
    parse(lang, params)
