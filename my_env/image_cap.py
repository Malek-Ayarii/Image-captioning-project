import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Real test image (Hugging Face hosted sample image)
image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/cat.jpg"

# Load image from URL
image = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")

# Process image (no need for custom text prompt for basic captioning)
inputs = processor(images=image, return_tensors="pt")

# Generate caption
outputs = model.generate(**inputs, max_length=50)

# Decode result
caption = processor.decode(outputs[0], skip_special_tokens=True)

# Print caption
print("Generated Caption:", caption)