from PIL import Image, ImageDraw, ImageFont

def add_mugshot_filter(image_filename, output_filename, serial_number):
    # Use the image and output filenames directly
    image_path = 'photo.JPEG'
    output_path = 'mugged.JPEG'
    
    print(f"Image path: {image_path}")
    print(f"Output path: {output_path}")

    try:
        # Open the image
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        
        # Define steel bars properties
        bars_color = (0, 0, 0)  # Black color for bars
        bar_width = 20  # Width of each bar
        bar_spacing = 30  # Spacing between bars
        
        # Calculate number of bars needed to cover the image
        num_bars = (image.height // (bar_width + bar_spacing)) + 1
        
        # Draw vertical steel bars
        for i in range(num_bars):
            x = i * (bar_width + bar_spacing)
            draw.rectangle([x, 0, x + bar_width, image.height], fill=bars_color)
        
        
        # Load font for serial number
        font = ImageFont.load_default(size = 60)
        
        # Add serial number text
        text = f"Serial Number: {serial_number}"
        
        # Get text size
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Calculate text position
        text_x = (image.width - text_width) // 2
        text_y = image.height - text_height - 50  # 50 pixels from bottom for more visibility
        
        # Draw text
        draw.text((text_x, text_y), text, font=font, fill="white")
        
        # Save the modified image
        image.save(output_path, format='JPEG')  # Explicitly specify JPEG format
        print(f"Mugshot filter applied and saved as {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
add_mugshot_filter('photo.jpeg', 'output_photo.jpeg', '1234567890')
