#!/usr/bin/env python3
"""
Script to generate a GitHub profile header image with name and current date/time.
"""

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

def generate_header(width=1920, height=400, output_file='header.png'):
    """
    Generate a header image with name and current date/time.
    
    Args:
        width: Width of the image in pixels
        height: Height of the image in pixels
        output_file: Output filename for the generated image
    """
    # Create a new image with a gradient background
    image = Image.new('RGB', (width, height), color='#0D1117')
    draw = ImageDraw.Draw(image)
    
    # Create a gradient background (dark blue to purple)
    for y in range(height):
        # Calculate color gradient from dark blue to purple
        r = int(13 + (88 - 13) * (y / height))
        g = int(17 + (28 - 17) * (y / height))
        b = int(23 + (135 - 23) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Add decorative elements
    # Draw some circles for visual interest
    for i in range(5):
        x = int(width * (0.2 + i * 0.15))
        y = height // 2
        radius = 100 - i * 15
        alpha = 30 - i * 5
        
        # Create a semi-transparent overlay
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius],
            fill=(88, 166, 255, alpha)
        )
        image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    
    draw = ImageDraw.Draw(image)
    
    # Try to use a nice font, fall back to default if not available
    try:
        # Try to find a good system font
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)
    except:
        # Fallback to default font
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    # Text content
    name = "Diego Wolder"
    subtitle = "Software Developer | GitHub"
    
    # Calculate text positions (center alignment)
    # Name
    name_bbox = draw.textbbox((0, 0), name, font=font_large)
    name_width = name_bbox[2] - name_bbox[0]
    name_x = (width - name_width) // 2
    name_y = height // 2 - 80
    
    # Subtitle
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_medium)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = name_y + 120
    
    # Date and time
    datetime_text = f"{date_str} • {time_str}"
    datetime_bbox = draw.textbbox((0, 0), datetime_text, font=font_small)
    datetime_width = datetime_bbox[2] - datetime_bbox[0]
    datetime_x = (width - datetime_width) // 2
    datetime_y = subtitle_y + 70
    
    # Draw text with shadow for better readability
    # Shadow
    shadow_offset = 3
    draw.text((name_x + shadow_offset, name_y + shadow_offset), name, 
              fill='#000000', font=font_large)
    draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle, 
              fill='#000000', font=font_medium)
    draw.text((datetime_x + shadow_offset, datetime_y + shadow_offset), datetime_text, 
              fill='#000000', font=font_small)
    
    # Main text
    draw.text((name_x, name_y), name, fill='#FFFFFF', font=font_large)
    draw.text((subtitle_x, subtitle_y), subtitle, fill='#58A6FF', font=font_medium)
    draw.text((datetime_x, datetime_y), datetime_text, fill='#8B949E', font=font_small)
    
    # Save the image
    image.save(output_file, 'PNG', quality=95)
    print(f"Header image generated successfully: {output_file}")
    print(f"Dimensions: {width}x{height}")
    print(f"Name: {name}")
    print(f"Date/Time: {datetime_text}")
    
    return output_file

if __name__ == "__main__":
    generate_header()
