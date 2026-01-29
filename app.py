"""Streamlit image classification app."""
import streamlit as st
from PIL import Image
from classifier import get_classifier

# Page configuration
st.set_page_config(
    page_title="Image Classifier",
    page_icon="🖼️",
    layout="centered"
)

# Title and description
st.title("🖼️ Image Classifier")
st.write("Upload an image to classify it using MobileNetV2 trained on ImageNet.")

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.write(
        "This app uses a pretrained MobileNetV2 model to classify images "
        "into 1000 ImageNet categories."
    )
    st.header("Settings")
    top_k = st.slider("Number of predictions", min_value=1, max_value=10, value=5)


# Load model (cached)
@st.cache_resource
def load_model():
    """Load and cache the classifier."""
    return get_classifier()


classifier = load_model()

# File uploader
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png", "webp"],
    help="Upload an image to classify"
)

# Process uploaded image
if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Classify button
    if st.button("🔍 Classify Image", type="primary"):
        with st.spinner("Classifying..."):
            predictions = classifier.predict(image, top_k=top_k)
        
        # Display results
        st.subheader("Predictions")
        
        for i, pred in enumerate(predictions, 1):
            confidence_pct = pred["confidence"] * 100
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{i}. {pred['label']}**")
                st.progress(pred["confidence"])
            with col2:
                st.write(f"{confidence_pct:.1f}%")

else:
    # Show placeholder
    st.info("👆 Upload an image to get started!")
    
    # Demo section
    st.subheader("How it works")
    st.write(
        """
        1. Upload a JPG, PNG, or WebP image
        2. Click "Classify Image"
        3. View the top predictions with confidence scores
        
        The model recognizes 1000 categories including animals, objects, 
        vehicles, food, and more.
        """
    )