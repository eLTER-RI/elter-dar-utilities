import argparse
import logging
import os
from typing import Any

def create_dataset_draft(upload_args: "UploadArgs") -> None:
    """
    Create a dataset draft in the eLTER DAR.

    Args:
        upload_args (UploadArgs): Arguments for uploading the dataset.
    """
    # Placeholder for the actual implementation
    print("Creating dataset draft...")
    pass


def _configure_argparse_subparser(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-m", "--metadata", type=str, required=True, help="Path to metadata file")
    parser.add_argument("-d", "--data", type=str, required=True, help="Path to a directory containing data files")
    parser.add_argument("-t", "--token", type=str, required=False, help="Path to a file containing API token. If not set, the token will be read from the environment variable `DAR_API_TOKEN`.")

    parser.set_defaults(func=__parse_args_and_upload)

    return parser

def __parse_args_and_upload(args: Any) -> None:
    args = __parse_arguments(args)
    create_dataset_draft(args)


def __parse_arguments(args: Any) -> "UploadArgs":
    if args.token is None:
        token = os.environ.get("DAR_API_TOKEN")
        if token is None:
            logging.error("API token must be provided either as a command line argument or via the environment variable `DAR_API_TOKEN`.")
            raise ValueError("API token is required.")
    else:
        if not os.path.isfile(args.token):
            logging.error(f"Token file does not exist: {args.token}")
            raise ValueError("Token file does not exist.")

        with open(args.token) as file:
            token = file.read().strip()

    if not os.path.isfile(args.metadata):
        logging.error(f"Metadata file does not exist: {args.metadata}")
        raise ValueError("Metadata file does not exist.")

    if not os.path.isdir(args.data):
        logging.error(f"Data directory does not exist: {args.data}")
        raise ValueError("Metadata file does not exist.")


    return UploadArgs(token=token, metadata=args.metadata, data=args.data)



class UploadArgs:
    def __init__(self, metadata: str, data: str, token: str):
        self.metadata_path = metadata
        self.data_dir_path = data
        self.token = token