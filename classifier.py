"""Image classification using pretrained MobileNetV2."""
import torch
from torchvision import models, transforms
from PIL import Image

# ImageNet class labels (simplified - top 20 common classes)
IMAGENET_CLASSES = {
    0: "tench", 1: "goldfish", 2: "great white shark",
    207: "golden retriever", 208: "Labrador retriever",
    281: "tabby cat", 282: "tiger cat", 283: "Persian cat",
    291: "lion", 292: "tiger",
    409: "analog clock", 530: "digital clock",
    817: "sports car", 751: "racing car",
    954: "banana", 948: "orange", 950: "strawberry",
    999: "toilet paper"
}


class ImageClassifier:
    """Lightweight image classifier using MobileNetV2."""
    
    def __init__(self):
        self.model = None
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            ),
        ])
        self.labels = self._load_labels()
        
    def _load_labels(self) -> list[str]:
        """Load ImageNet class labels."""
        # Using torchvision's built-in weights for labels
        weights = models.MobileNet_V2_Weights.IMAGENET1K_V1
        return weights.meta["categories"]
    
    def load_model(self):
        """Load the pretrained model."""
        if self.model is None:
            self.model = models.mobilenet_v2(
                weights=models.MobileNet_V2_Weights.IMAGENET1K_V1
            )
            self.model.eval()
        return self
    
    def predict(self, image: Image.Image, top_k: int = 5) -> list[dict]:
        """
        Classify an image and return top-k predictions.
        
        Args:
            image: PIL Image to classify
            top_k: Number of top predictions to return
            
        Returns:
            List of dicts with 'label' and 'confidence' keys
        """
        if self.model is None:
            self.load_model()
        
        # Preprocess image
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        input_tensor = self.transform(image).unsqueeze(0)
        
        # Run inference
        with torch.no_grad():
            outputs = self.model(input_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
        
        # Get top-k predictions
        top_probs, top_indices = torch.topk(probabilities, top_k)
        
        results = []
        for prob, idx in zip(top_probs, top_indices):
            results.append({
                "label": self.labels[idx.item()],
                "confidence": prob.item()
            })
        
        return results


# Singleton instance for caching
_classifier = None

def get_classifier() -> ImageClassifier:
    """Get or create the classifier singleton."""
    global _classifier
    if _classifier is None:
        _classifier = ImageClassifier()
        _classifier.load_model()
    return _classifier