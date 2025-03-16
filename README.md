# "Hey Zepp Flow" Wake Word Detectation

## Acknowledgment 
This repo is based on OHF-Voice/pymicro-wakeword. Our Tensorflow Lite voice model is trained using kahrendt/microWakeWord. 

## Install 

``` sh
python -m pip install -e .
```

## Python Usage 

Input audio must be 16-bit mono at 16Khz. 

inference.py provides basic usage in python.

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
