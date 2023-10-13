from flask import json
import queue
import sys
from threading import Lock
import threading
import sounddevice as sd

from vosk import Model, KaldiRecognizer


class SPeaker :
    q = queue.Queue()
    cola=queue.Queue()
    lock = Lock()
    def __init__(self) -> None:
        t2 = threading.Thread(target=self._Speaker_text, args=[self.lock])
        t2.start()

    def Get_data(self) -> str:
        
        return  str(self.cola.get())
    def _Speaker_text(self, look :Lock ) ->None:
        
        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)
            self.q.put(bytes(indata))
        try:
            device_info = sd.query_devices(0, "input")
            print("!DEVICE INFO!")
                # soundfile expects an int, sounddevice provides a float:
            samplerate = int(device_info["default_samplerate"])
            model = Model( r"/home/servidor/Documentos/Speach to text/vosk-model-small-es-0.42")
            with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=None,
                        dtype="int16", channels=1, callback=callback):
                

                    rec = KaldiRecognizer(model, samplerate)
                    print("*****REC******")
                    while True:
                        data = self.q.get()
                        if rec.AcceptWaveform(data):
                            self.cola.put(rec.Result())
                        else:
                            self.cola.put(rec.PartialResult())
        except KeyboardInterrupt:
            print("\nDone")
            exit(0)

 
