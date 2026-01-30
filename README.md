# GitHub Profile Header Generator

This repository contains a Python script to generate a professional GitHub profile header image with your name and the current date/time.

## Features

- 🎨 Beautiful gradient background (dark blue to purple)
- ✨ Decorative circular elements for visual interest
- 📝 Displays your name prominently
- ⏰ Shows current date and time
- 🖼️ Generates a 1920x400 PNG image perfect for GitHub profiles

## Generated Header

![Header Image](header.png)

## Usage

### Prerequisites

- Python 3.x
- Pillow library

### Installation

```bash
pip install Pillow
```

### Generate Your Header

```bash
python3 generate_header.py
```

This will create a `header.png` file in the current directory with:
- Your name: **Diego Wolder**
- Current date and time
- Professional styling suitable for GitHub profiles

## Customization

You can edit the `generate_header.py` file to customize:
- Image dimensions (default: 1920x400)
- Name text
- Subtitle text
- Colors and gradients
- Font sizes
- Background style

## Output

The script generates a PNG image with:
- **Width:** 1920 pixels
- **Height:** 400 pixels
- **Format:** PNG with high quality
- **Text:** White name, blue subtitle, gray date/time

## License

Free to use and modify for your GitHub profile!