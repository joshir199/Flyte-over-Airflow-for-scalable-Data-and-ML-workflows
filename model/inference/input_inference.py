
import base64
import json

# Read and encode the image file
with open("xray_input_data.png", "rb") as image_file:
  image_data = base64.b64encode(image_file.read())

# Create the payload with image as string data for inference on Web.
payload = {"image_data": image_data.decode("utf-8"), "prompt": [58, 23, 219, 107]}

if __name__ == "__main__":
  # copy to inference file
  print(json.dumps(payload))
