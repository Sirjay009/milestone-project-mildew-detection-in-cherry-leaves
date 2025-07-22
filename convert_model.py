import tensorflow as tf
import os

# Load the Keras model from file
model = tf.keras.models.load_model("outputs/v1/mildew_detector_model.keras")

# Convert it to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save it to disk
with open("outputs/v1/mildew_detector_model.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Converted to mildew_detector_model.tflite")

# Check file size
file_path = "outputs/v1/mildew_detector_model.tflite"
file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
print(f"📦 File size: {file_size:.2f} MB")