# Image Captioning Project

An AI-powered image captioning application that generates natural language descriptions for images using the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model.

## Features

✨ **Automatic Caption Generation** - Generate descriptive captions for any image  
🎨 **Web Interface** - Easy-to-use Gradio interface for image uploading  
⚡ **Fast Processing** - GPU-accelerated caption generation  
🔧 **CLI Support** - Command-line script for batch processing  
🤖 **State-of-the-Art Model** - Uses Salesforce's BLIP model for high-quality captions  

## Installation

### Prerequisites
- Python 3.8 or higher
- CUDA 11.8+ (optional, for GPU acceleration)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Malek-Ayarii/Image-captioning-project.git
cd Image-captioning-project
```

2. Create a virtual environment:
```bash
python -m venv my_env
my_env\Scripts\activate  # On Windows
source my_env/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Interface

Run the Gradio web app:
```bash
python image_captioning_app.py
```

Then open your browser and go to `http://localhost:7860`

### Command Line

Generate a caption for an image from URL:
```bash
python image_cap.py
```

## Project Structure

```
Image-captioning-project/
├── image_captioning_app.py    # Gradio web interface
├── image_cap.py               # CLI caption generation
├── hello.py                   # Sample script
├── requirements.txt           # Dependencies
└── my_env/                    # Virtual environment
```

## Requirements

```
torch
transformers
pillow
gradio
numpy
requests
```

## Model Details

- **Model**: Salesforce BLIP Image Captioning Base
- **Task**: Image-to-Text (Caption Generation)
- **Input**: Images (any size, auto-converted to RGB)
- **Output**: Natural language captions (max 50 tokens)

## How It Works

1. Load an image (from file or URL)
2. Preprocess the image using BLIP processor
3. Generate caption using the pre-trained model
4. Decode and return the caption text

## Example Output

```
Input: Image of a cat
Output: "a cat sitting on a table"
```

## Requirements & Dependencies

- Python 3.8+
- PyTorch
- Transformers (Hugging Face)
- Gradio
- PIL/Pillow
- NumPy
- Requests

## Performance

- **Speed**: ~1-2 seconds per image (CPU), <1 second (GPU)
- **Memory**: ~2GB GPU memory required

## Future Improvements

- [ ] Support for longer captions
- [ ] Batch image processing
- [ ] Model fine-tuning option
- [ ] API endpoint
- [ ] Docker support

## License

This project is open source. Feel free to use it for educational and commercial purposes.

## Contributing

Contributions are welcome! Feel free to open issues and submit pull requests.

## Author

**Malek Ayarii**  
[GitHub](https://github.com/Malek-Ayarii)

## References

- [BLIP: Bootstrapping Language-Image Pre-training](https://huggingface.co/Salesforce/blip-image-captioning-base)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Gradio Documentation](https://www.gradio.app/docs)
