from PIL import Image, ImageFilter

def blur_image(image_path, output_path, radius):
  image = Image.open(image_path)
  blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
  blurred_image.save(output_path)

blur_image('barcode_image.png', 'barcode_out.jpg', 3)
Image.open('barcode_out.jpg')
