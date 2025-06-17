import tensorflow as tf

# Load the Keras model
keras_model_path = 'outputs/v1/mildew_detector_model.keras'
model = tf.keras.models.load_model(keras_model_path)

# Convert to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted model
tflite_model_path = 'outputs/v1/mildew_detector_model.tflite'
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)