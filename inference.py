from pymicro_wakeword import MicroWakeWord, Model

if __name__=="__main__":
    config_path = "./pymicro_wakeword/models/hey_zepp_flow.json"
    mww = MicroWakeWord.from_config(config_path)
    with open("./tests/hey_zepp_flow/01.wav", "rb") as f:
        audio_bytes = f.read()
        result = mww.process_clip(audio_bytes)
        print(result.detected, result.detected_seconds)
        mww.reset()

    # for sample models:
    # mww = MicroWakeWord.from_builtin(Model.HEY_MYCROFT)
    # with open("./tests/hey_mycroft/hey_mycroft.wav", "rb") as f:
    #     audio_bytes = f.read()
    #     result = mww.process_clip(audio_bytes)
    #     print(result.detected, result.detected_seconds)
    #     mww.reset()

    