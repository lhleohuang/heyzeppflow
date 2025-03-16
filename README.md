# "Hey Zepp Flow" Wake Word Detectation

## Acknowledgment 
This is a repo cloned from OHF-Voice/pymicro-wakeword. Our Tensorflow Lite voice model is trained using kahrendt/microWakeWord. 

## Install 

``` sh
pip3 install pymicro-wakeword
```

## Python Usage 

Input audio must be 16-bit mono at 16Khz. 

inference.py provides basic usage in python.

## Command-Line Usage

### WAVE files (Full- Context Mode)

``` sh
python3 -m pymicro_wakeword --model 'okay_nabu' /path/to/*.wav
```

### Live Streaming Mode

``` sh
arecord -r 16000 -c 1 -f S16_LE -t raw | \
  python3 -m pymicro_wakeword --model 'okay_nabu'
```
