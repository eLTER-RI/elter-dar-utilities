import argparse
from .upload import _configure_argparse_subparser


def _configure_creator_subparser(parser: argparse.ArgumentParser):
    subparsers = parser.add_subparsers(required=True)

    upload_parser = subparsers.add_parser("upload", help="Upload a dataset draft to the eLTER DAR")
    _configure_argparse_subparser(upload_parser)

    return parser
