# "Hey Zepp Flow" Wake Word Detectation

## Acknowledgment 
This repo is based on OHF-Voice/pymicro-wakeword. Our Tensorflow Lite voice model is trained using kahrendt/microWakeWord. Users should refer to the former for details on running the model for inference (in python), the latter for details on the training process, and how live streaming works with the model.

## Install 

``` sh
python -m pip install -e .
```

## Tensorflow Lite Voice Model

Input audio must be 16-bit mono at 16Khz. Alternative models (those performing worse on synthetic datasets) are included in pymicro_wakeword/models.

## Python Usage 

inference.py provides basic usage in python. tests/test_microwakeword.py provides more test cases.

## Command-Line Usage

### Full-Context Mode (WAVE files)

``` sh
python -m pymicro_wakeword --config 'hey_zepp_flow' tests/hey_zepp_flow/01.wav
```

### Live Streaming Mode

``` sh
arecord -r 16000 -c 1 -f S16_LE -t raw | \
  python -m pymicro_wakeword --config 'hey_zepp_flow'
```
## Helpful Tips for Converting the Inference Script to C (and Running the Model on Microcontrollers)

To get started and for an overview of the C libraries required for on-board inference:

* [LiteRT for Microcontrollers](https://ai.google.dev/edge/litert/microcontrollers/get_started)

* [Sample Speech Recognition Model with TFLite](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/micro_speech)

The most important external python library used by our inference script is [pymicro-features](https://github.com/rhasspy/pymicro-features), which is in fact built from C, borrowed from the same tensorflow lite libraries (see below for notes on dependencies).

For more information on how live streaming works with the model, refer to kahrendt/microWakeWord.

## Notes on Dependencies

inference.py imports pymicro_wakeword. pymicro_wakeword depends on tensorflow, numpy, and pymicro_features. [pymicro-features](https://github.com/rhasspy/pymicro-features) depends on [micro_features_cpp](https://github.com/rhasspy/pymicro-features/blob/master/pymicro_features/__init__.py) which is [compiled from tensorflow lite C libraries ](https://github.com/rhasspy/pymicro-features/blob/master/setup.py) and [repackaged into a python library](https://github.com/rhasspy/pymicro-features/blob/master/python.cpp). The tensorflow library, of which we only use tf.lite, can be found [here](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite). Numpy can be converted directly to C using elementary vector operations. 
