import tensorflow as tf

# Load the Keras model
keras_model_path = 'outputs/v1/mildew_detector_model.keras'
model = tf.keras.models.load_model(keras_model_path)

# Build the model with the input shape
model.build(input_shape=(None, 256, 256, 3))

# Convert the model to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open('outputs/v1/mildew_detector_model.tflite', 'wb') as f:
    f.write(tflite_model)