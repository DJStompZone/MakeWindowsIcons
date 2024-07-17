import argparse
import os

import makewindowsicons.util as mwi_util
import makewindowsicons.args as arg_parser


def main():
    args = argparse.Namespace()
    parser = arg_parser._parse_args(argparse.ArgumentParser)

    if len(os.sys.argv) == 1:
        parser.print_help(os.sys.stderr)
        os.sys.exit(1)

    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        parser.print_help(os.sys.stderr)
        os.sys.exit(1)

    output_dir = os.path.abspath(args.output_dir)
    default_sizes = [10, 16, 20, 24, 30, 32, 36, 40, 48, 60, 64, 72, 80, 96, 128, 256]
    sizes = list(
        set(
            default_sizes
            + [
                size
                for size in (args.size if args.size else [])
                if isinstance(size, int) and 2**12 >= size > 0
            ]
        )
    )

    try:
        resources_dir = mwi_util.create_resources_dir(output_dir, args.no_dir)
        resized_images = mwi_util.resize_images(args.input_image, sizes)
        mwi_util.save_images(resized_images, resources_dir, args.app_name)
        mwi_util.create_ico_file(resized_images, resources_dir, args.app_name)
        print(f"Icons have been saved in '{resources_dir}'")
    except FileExistsError as e:
        print(e)


if __name__ == "__main__":
    main()
