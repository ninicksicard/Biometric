import pyaudio
import wave

class AudioStream:
    def setstream(self, wf, chunk=1024):
        self.CHUNK = chunk
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                                  channels=wf.getnchannels(),
                                  rate=wf.getframerate(),
                                  output=True)
    def streamchunk(self, data):
        self.stream.write(data)

    def stopit(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


ok = AudioStream()
wf = wave.open("KFlay-Blood-In-The-Cut.wav", 'rb')
ok.setstream(wf)
data = wf.readframes(1024)
while len(data) > 0:
    ok.streamchunk(wf.readframes(1024))
