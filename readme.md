# PIX
[![PyPI - Version](https://img.shields.io/pypi/v/zz-pix)](https://pypi.org/project/zz-pix)
[![PyPI - License](https://img.shields.io/pypi/l/zz-pix)](LICENSE)
[![Downloads](https://static.pepy.tech/badge/zz-pix)](https://pepy.tech/project/zz-pix)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zz-pix)

A simple image manipulation tool for the terminal.

> ⭐️ Like this repo? please consider a star!

> 💡 This project is still earily in its development. Please report any bugs or issues you encounter.

## 🌟 Features
- [x] Resize
- [x] Crop
- [x] Convert
- [x] Prune (remove low-quality images)
- [x] Caption (add text & metadata to images)
- [ ] Watermark
- [ ] Grayscale

## 💻 Installation

### Using pip (Recommended)
```sh
pip install zz-pix
```

### From Source
```bash
git clone https://github.com/sean1832/pix.git
cd pix
pip install .
```

## 🔨 Usage

### Basic Usage

```sh
pix [COMMAND] [OPTIONS]
```

Replace `[COMMAND]` with the desired operation and `[OPTIONS]` with the relevant options for your command.

### Global Options

- `-v`, `--version`: Display the version of the tool.
- `-h`, `--help`: Display the help message.

### Commands

| Command | Description                                      |
|---------|--------------------------------------------------|
| [convert](#convert) | Converts images to a different format            |
| [resize](#resize)  | Resizes images                                   |
| [crop](#crop)    | Crops images                                     |
| [prune](#prune)   | Removes images smaller than specified resolution|
| [caption](#caption) | Captions image or a directory of images          |

### Command Options

#### Convert
Converts images to a different formats. Currently supports `JPEG`, `PNG`, `WEBP`, `TIFF`, `ICO`, `AVIF`, `HEIF`, `BMP`.

```sh
pix convert [OPTIONS]
```

| Option        | Input Type | Description                                | Default     |
|---------------|------------|--------------------------------------------|-------------|
| `input`         | String     | Input image or directory                   | N/A         |
| `-o`, `--output`  | String     | Output image or directory                  | Current dir.|
| `-f`, `--format`  | String     | Output format (supported formats listed)   | N/A         |
| `-q`, `--quality` | Integer    | Output quality (0-100)                     | 95          |
| `--no-optimize` | Flag       | Disable optimization                       | N/A         |
| `--overwrite`   | Flag       | Overwrite existing files                   | N/A         |
| `--prefix`      | String     | Prefix for the output file name            | ""          |
| `--surfix`      | String     | Suffix for the output file name            | ""          |

#### Resize
Resizes images to a specified size or scale.
```sh
pix resize [OPTIONS]
```

| Option       | Input Type | Description                      | Default     |
|--------------|------------|----------------------------------|-------------|
| `input`        | String     | Input image or directory         | N/A         |
| `-o`, `--output` | String     | Output image or directory        | Current dir.|
| `--overwrite`  | Flag       | Overwrite existing files         | N/A         |
| `--size`       | String     | Output size (WxH)                | N/A         |
| `--scale`      | Float      | Output scale (0.0-1.0)           | N/A         |

#### Crop
Crops images to a specified size and position.
```sh
pix crop [OPTIONS]
```


| Option       | Input Type | Description                                        | Default     |
|--------------|------------|----------------------------------------------------|-------------|
| `input`        | String     | Input image or directory                           | N/A         |
| `-o`, `--output` | String     | Output image or directory                          | Current dir.|
| `--overwrite`  | Flag       | Overwrite existing files                           | N/A         |
| `--ratio`      | String     | Aspect ratio (W:H), combined with `--align`        | N/A         |
| `--size`       | String     | Exact size and position as WxH+X+Y                 | N/A         |
| `--align`      | String     | Alignment (top, bottom, left, right, center)       | N/A         |

#### Prune
Removes images smaller than a specified resolution.
```sh
pix prune [OPTIONS]
```


| Option         | Input Type | Description                                       | Default |
|----------------|------------|---------------------------------------------------|---------|
| input          | String     | Input image or directory                          | N/A     |
| `-r`, `--resolution` | String   | Minimum resolution (WxH)                         | N/A     |
| `--dry-run`      | Flag       | List files to be removed without deleting them    | N/A     |

#### ~~Caption~~ 
(Removed this feature, implemented in a separate tool [zz-img-caption](https://github.com/sean1832/zz-img-caption))




## License
[Apache-2.0](LICENSE)

