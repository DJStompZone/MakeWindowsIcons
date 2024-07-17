import os
from typing import Dict, List, Tuple
from PIL import Image

def prompt_overwrite() -> bool:
    """
    Prompt the user to confirm whether they want to overwrite the 'resources' directory.

    Returns:
        bool: True if the user wants to overwrite, False otherwise.
    """
    while True:
        response = input("The directory 'resources' already exists. Do you want to overwrite it? [y/n]: ").lower()
        if not response or response[:1] not in ['y', 'n']:
            print("Please enter 'y' or 'n'.")
            continue
        return response.startswith('y')

def create_resources_dir(output_dir: str, no_dir: bool) -> str:
    """
    Creates a resources directory within the specified output directory.

    Args:
        output_dir (str): The path of the output directory.
        no_dir (bool): If True, the resources directory will not be created.

    Returns:
        str: The path of the resources directory.

    Raises:
        FileExistsError: If the resources directory already exists and was not overwritten.
    """
    if no_dir:
        return output_dir
    resources_dir = os.path.join(output_dir, "resources")
    if os.path.exists(resources_dir):
        if prompt_overwrite():
            for filename in os.listdir(resources_dir):
                file_path = os.path.join(resources_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        else:
            raise FileExistsError(f"The directory '{resources_dir}' already exists and was not overwritten.")
    else:
        os.makedirs(resources_dir)
    return resources_dir

def resize_images(input_image_path: str, sizes: List[int]) -> Dict[int, Image.Image]:
    """
    Resize the input image to the specified sizes.

    Args:
        input_image_path (str): The path to the input image file.
        sizes (List[int]): A list of sizes (integers) to resize the image to.

    Returns:
        Dict[int, Image.Image]: A dictionary containing the resized images, where the keys are the sizes and the values are the resized images.
    """
    original_image = Image.open(input_image_path)
    resized_images = {}
    for size in sizes:
        resized_image = original_image.resize((size, size), Image.LANCZOS)
        resized_images[size] = resized_image
    return resized_images

def save_images(resized_images: Dict[int, Image.Image], resources_dir: str, app_name: str) -> None:
    """
    Save the resized images to the specified resources directory.

    Args:
        resized_images (Dict[int, Image.Image]): A dictionary containing the resized images.
        resources_dir (str): The path to the resources directory.
        app_name (str): The name of the application.

    Returns:
        None
    """
    for size, image in resized_images.items():
        image.save(os.path.join(resources_dir, f"{app_name.replace(' ', '_')}-{size}.png"))

def sort_numeric(items: List[Tuple[int, Image.Image]]) -> List[Tuple[int, Image.Image]]:
    """
    Sort a list of tuples containing numeric sizes and images.

    Args:
        items (List[Tuple[int, Image.Image]]): A list of tuples where the first element is a numeric size and the second element is an image.

    Returns:
        List[Tuple[int, Image.Image]]: The sorted list of tuples.
    """
    return sorted(items, key=lambda x: x[0])

def create_ico_file(resized_images: Dict[int, Image.Image], resources_dir: str, app_name: str) -> None:
    """
    Create an ICO file from a list of resized images.

    Args:
        resized_images (Dict[int, Image.Image]): A dictionary containing resized images as values and their corresponding sizes as keys.
        resources_dir (str): The directory where the ICO file will be saved.
        app_name (str): The name of the application.

    Returns:
        None
    """
    ico_path = os.path.join(resources_dir, f"{app_name.replace(' ', '_')}.ico")
    
    sorted_items = sort_numeric(list(resized_images.items()))
    sorted_sizes = [(size, size) for size, _ in sorted_items]
    sorted_images = [image.resize((size, size), Image.LANCZOS).convert("RGBA") for size, image in sorted_items]

    sorted_sizes.reverse()
    sorted_images.reverse()

    sorted_images[0].save(
        ico_path,
        format='ICO',
        sizes=sorted_sizes,
        append_images=sorted_images[1:]
    )
