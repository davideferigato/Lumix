# lumix/currency/parser.py

import argparse
import gettext
import os

from .convert import convert_currency


def get_parser(lang: str = "en") -> argparse.ArgumentParser:
    localedir = os.path.join(os.path.dirname(__file__), "languages")
    gettext.bindtextdomain("messages", localedir)
    gettext.textdomain("messages")
    _ = gettext.gettext

    parser = argparse.ArgumentParser(
        description=_("Convert currencies between EUR, USD, and GBP.")
    )

    parser.add_argument("--amount", type=float, required=True, help=_("Amount to convert"))
    parser.add_argument(
        "--from", "--da", "--de", "--de_", "--から",
        dest="src", required=True, choices=["EUR", "USD", "GBP"],
        help=_("Source currency")
    )
    parser.add_argument(
        "--to", "--a", "--a_", "--à", "--へ",
        dest="dst", required=True, choices=["EUR", "USD", "GBP"],
        help=_("Target currency")
    )

    return parser


def main(args):
    value = convert_currency(args.amount, args.src, args.dst)
    print(f"{args.amount:.2f} {args.src} → {value:.2f} {args.dst}")
