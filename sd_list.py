import queue
import sys
from threading import Lock
import sounddevice as sd

from vosk import Model, KaldiRecognizer


def Speaker_text( look :Lock ,cola :queue.Queue):
    q = queue.Queue()
    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))
    try:
        device_info = sd.query_devices(9, "input")
        print("!DEVICE INFO!")
            # soundfile expects an int, sounddevice provides a float:
        samplerate = int(device_info["default_samplerate"])
        model = Model( r"/home/servidor/Documentos/Speach to text/vosk-model-small-es-0.42")
        with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=None,
                    dtype="int16", channels=1, callback=callback):
            

                rec = KaldiRecognizer(model, samplerate)
                print("*****REC******")
                while True:
                    data = q.get()
                    if rec.AcceptWaveform(data):
                        cola.put(rec.Result())
                    else:
                        cola.put(rec.PartialResult())
    except KeyboardInterrupt:
        print("\nDone")
        exit(0)

 