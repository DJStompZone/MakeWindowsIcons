# Make Windows Icons

This script resizes a given image to various sizes and creates a set of icons for a Windows application. The generated icons are saved in PNG format, and an ICO file is created that packs all the icons together.

## Features

- Resize a single source image to multiple sizes.
- Save the resized images in PNG format.
- Create an ICO file containing all the resized icons.
- Optionally, specify additional sizes to resize the image to.

## Requirements

- Python 3.11+

## Installation

1. Install with pip:

```sh
python3 -m pip install makewindowsicons
```

## Usage

```sh
python3 -m makewindowsicons -i <input_image> -a <app_name> [-o <output_directory>] [--no_dir] [-s <size>]...
```

### Arguments

- `-i <input_image>`, `--input_image <input_image>`: Path to the source image.

### Options

- `-a <app_name>`, `--app_name <app_name>`: Name of the application. Default is 'app'.
- `-o <output_directory>`, `--output_dir <output_directory>`: Directory to save the output resources. Default is the current directory.
- `-n`, `--no_dir`: Do not create a 'resources' directory; save images directly to the specified output directory.
- `-s <size>`, `--size <size>`: Optional additional sizes to resize the image to. Can be specified multiple times. Sizes over 256px will be ignored, as this is the largest size supported by Windows for .ICO files.

### Examples

1. **Default behavior**:
   
   Resize the image to the default sizes and save in the `resources` directory within the current directory:

   ```sh
   python3 -m makewindowsicons -i your_source_image.png -a YourAppName
   ```

2. **Specify output directory**:

   Resize the image to the default sizes and save in the `resources` directory within the specified output directory:

   ```sh
   python3 -m makewindowsicons -i your_source_image.png -a YourAppName -o output_path
   ```

3. **Without creating `resources` directory**:

   Resize the image to the default sizes and save directly in the specified output directory:

   ```sh
   python3 -m makewindowsicons -i your_source_image.png -a YourAppName -o output_path -n
   ```

4. **Add additional sizes**:

   Resize the image to the default sizes plus additional sizes (e.g., 37px, 69px) and save in the `resources` directory within the specified output directory:

   ```sh
   python3 -m makewindowsicons -i your_source_image.png -a YourAppName -o output_path -s 42 -s 69 -s 77
   ```

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.