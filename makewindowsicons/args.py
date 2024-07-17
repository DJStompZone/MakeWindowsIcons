import os
from argparse import ArgumentParser

def _parse_args(arg_parser = ArgumentParser) -> ArgumentParser:
    """
    Parse command line arguments for resizing images and creating Windows app icons.

    Returns:
        An instance of `argparse.ArgumentParser` with the defined command line arguments.
    """
    parser = arg_parser(
        description="Resize image and create Windows app icons."
    )
    parser.add_argument(
        "-i", "--input_image", required=True, help="Path to the 1024px input image."
    )
    parser.add_argument(
        "-a",
        "--app_name",
        default="app",
        help="Name of the application. Default is 'app'.",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        default=".",
        help="Directory to save the output resources. Default is the current directory.",
    )
    parser.add_argument(
        "-n",
        "--no_dir",
        action="store_true",
        help="Do not create a 'resources' directory, save images directly to the specified output directory.",
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        action="append",
        help="Optional additional sizes to resize the image to. Can be specified multiple times.",
    )

    if len(os.sys.argv) == 1:
        parser.print_help(os.sys.stderr)
        os.sys.exit(1)

    return parser

if __name__ == "__main__":
    args = _parse_args().parse_args()
    print(args)