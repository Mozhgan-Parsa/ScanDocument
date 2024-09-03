# Document Scanner with OpenCV

This project demonstrates how to build a simple document scanner using OpenCV in Python. The scanner detects the edges of a document in an image, finds its contour, and applies a perspective transform to produce a top-down view of the document, similar to how a flatbed scanner would.

## Features

- **Edge Detection**: Automatically detects the edges of documents in an image.
- **Contour Detection**: Identifies the contour (outline) of the document based on the detected edges.
- **Perspective Transform**: Warps the image to provide a top-down view of the document, effectively "scanning" it.

## Steps to Build the Document Scanner

Building a document scanner with OpenCV can be accomplished in just three simple steps:

1. **Detect Edges**: Use image processing techniques to find the edges in the image. This helps in identifying the boundaries of the document.

2. **Find Contour**: Use the detected edges to find the contour (outline) representing the piece of paper being scanned.

3. **Apply Perspective Transform**: Apply a perspective transform to obtain a top-down view of the document, making it appear as if it were scanned with a flatbed scanner.

## Usage

### Clone the repository:

```bash
git clone https://github.com/yourusername/document-scanner.git
cd document-scanner
```

### Run the script:

```bash
python scanDocument.py --image images/example_01.jpeg

```

Replace images/example_02.png with the path to your image file 
