# "Hey Zepp Flow" Wake Word Detectation

## Acknowledgment 
This repo is based on OHF-Voice/pymicro-wakeword. Our Tensorflow Lite voice model is trained using kahrendt/microWakeWord. Users should refer to the former for details on running the model for inference, the latter for training similar models.

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

The most important external python library used by our inference script is [pymicro-features](https://github.com/rhasspy/pymicro-features), which is in fact built from C.
