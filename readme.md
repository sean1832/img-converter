# PIX
a simple image manipulation tool for the terminal

## Features
- [x] Resize
- [x] Crop
- [x] Convert
- [x] Prune (remove low-quality images)
- [x] Caption (add text & metadata to images)
- [ ] Watermark
- [ ] Grayscale

## Installation
```bash
git clone https://github.com/sean1832/pix.git
cd pix
pip install .
```

## Usage

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
| convert | Converts images to a different format            |
| resize  | Resizes images                                   |
| crop    | Crops images                                     |
| prune   | Removes images smaller than specified resolution|
| caption | Captions image or a directory of images          |

### Options for Each Command

#### Convert
Converts images to a different formats. Currently supports `JPEG`, `PNG`, `WEBP`, `TIFF`, `ICO`, `AVIF`, `HEIF`, `BMP`.

```sh
pix convert [OPTIONS]
```

| Option        | Input Type | Description                                | Default     |
|---------------|------------|--------------------------------------------|-------------|
| input         | String     | Input image or directory                   | N/A         |
| -o, --output  | String     | Output image or directory                  | Current dir.|
| -f, --format  | String     | Output format (supported formats listed)   | N/A         |
| -q, --quality | Integer    | Output quality (0-100)                     | 95          |
| --no-optimize | Flag       | Disable optimization                       | N/A         |
| --overwrite   | Flag       | Overwrite existing files                   | N/A         |
| --prefix      | String     | Prefix for the output file name            | ""          |
| --surfix      | String     | Suffix for the output file name            | ""          |

#### Resize
```sh
pix resize [OPTIONS]
```


| Option       | Input Type | Description                      | Default     |
|--------------|------------|----------------------------------|-------------|
| input        | String     | Input image or directory         | N/A         |
| -o, --output | String     | Output image or directory        | Current dir.|
| --overwrite  | Flag       | Overwrite existing files         | N/A         |
| --size       | String     | Output size (WxH)                | N/A         |
| --scale      | Float      | Output scale (0.0-1.0)           | N/A         |

#### Crop
```sh
pix crop [OPTIONS]
```


| Option       | Input Type | Description                                        | Default     |
|--------------|------------|----------------------------------------------------|-------------|
| input        | String     | Input image or directory                           | N/A         |
| -o, --output | String     | Output image or directory                          | Current dir.|
| --overwrite  | Flag       | Overwrite existing files                           | N/A         |
| --ratio      | String     | Aspect ratio (W:H), combined with `--align`        | N/A         |
| --size       | String     | Exact size and position as WxH+X+Y                 | N/A         |
| --align      | String     | Alignment (top, bottom, left, right, center)       | N/A         |

#### Prune
```sh
pix prune [OPTIONS]
```


| Option         | Input Type | Description                                       | Default |
|----------------|------------|---------------------------------------------------|---------|
| input          | String     | Input image or directory                          | N/A     |
| -r, --resolution | String   | Minimum resolution (WxH)                         | N/A     |
| --dry-run      | Flag       | List files to be removed without deleting them    | N/A     |

#### Caption
```sh
pix caption [OPTIONS]
```

| Option          | Input Type | Description                                | Default |
|-----------------|------------|--------------------------------------------|---------|
| input           | String     | Input image or directory                   | N/A     |
| -t, --token     | Integer    | Max token length for captioning            | 32      |
| -b, --batch     | Integer    | Batch size for captioning                  | 1       |
| -p, --prompt    | String     | Prompt for captioning                      | N/A     |
| --temperature   | Float      | Temperature for captioning                 | 1.0     |
| --seed          | Integer    | Seed for reproducibility                   | N/A     |
| --large         | Flag       | Use the large model                        | N/A     |
| --cpu           | Flag       | Use CPU instead of GPU                     | N/A     |
| --metadata      | Flag       | Write caption as metadata for the image    | N/A     |
| --blip2         | Flag       | Use Blip2 model for captioning             | N/A     |
| --verbose       | Flag       | Print verbose output                       | N/A     |



## License
[Apache-2.0](LICENSE)

