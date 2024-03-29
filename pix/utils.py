import pathlib


def get_supported_formats(str=False):

    supported_formats = ["png", "jpeg", "webp", "avif", "heif", "tiff", "bmp", "ico"]
    if str:
        return ", ".join(supported_formats)
    else:
        return supported_formats


def is_file_supported(file):
    supported_formats = get_supported_formats()
    ext = pathlib.Path(file).suffix
    ext = ext[1:]
    return ext in supported_formats