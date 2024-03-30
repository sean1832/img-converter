# PIX
a simple image manipulation tool for the terminal

## Features
- [x] Resize
- [x] Crop
- [x] Convert
- [x] Prune (remove low-quality images)
- [ ] Rotate
- [ ] Flip
- [ ] Watermark
- [ ] Text
- [ ] Blur
- [ ] Grayscale
- [ ] Invert

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

Replace `[COMMAND]` with the desired operation (`convert`, `resize`, or `crop`) and `[OPTIONS]` with the relevant options for your command.

### Global Options

- `-v`, `--version`: Display the version of the tool.
- `command`: Specify the command to execute (`convert`, `resize`, or `crop`).

### Commands

#### Convert

Converts images to a different format.

```sh
pix convert input [OPTIONS]
```

**Options:**

- `input`: Input image or directory.
- `-o`, `--output`: Output image or directory (default: current directory).
- `-f`, `--format`: Output format (supported formats will be listed).
- `-q`, `--quality`: Output quality (0-100, default: 95).
- `--no-optimize`: Disable optimization.
- `--overwrite`: Overwrite existing files.
- `--prefix`: Prefix for the output file name.
- `--surfix`: Suffix for the output file name.

#### Resize

Resizes images.

```sh
pix resize input [OPTIONS]
```

**Options:**

- `input`: Input image or directory.
- `-o`, `--output`: Output image or directory (default: current directory).
- `--overwrite`: Overwrite existing files.
- `--size`: Output size in width x height format (WxH).
- `--scale`: Output scale (0.0-1.0).

#### Crop

Crops images.

```sh
pix crop input [OPTIONS]
```

**Options:**

- `input`: Input image or directory.
- `-o`, `--output`: Output image or directory (default: current directory).
- `--overwrite`: Overwrite existing files.
- `--ratio`: Aspect ratio (W:H), to be used with `--align`.
- `--size`: Exact size and position as WxH+X+Y (e.g., 800x600+100+150).
- `--align`: Alignment (top, bottom, left, right, center).

#### Prune
```sh
pix prune input [OPTIONS]
```

**Options:**
- `input`: Input image or directory.
- `-r`, `--resolution`: Minimum resolution (e.g. 512x512).
- `--dry-run`: List files to be removed without deleting them.

## License
[Apache-2.0](LICENSE)

