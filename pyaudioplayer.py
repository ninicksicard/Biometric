import pyaudio
import wave


class AudioStream:
    def playfile(self, file):
        self.wf = wave.open(file, 'rb')
        return self.wf

    def readchunk(self, wf):
        self.data = wf.readframes(self.CHUNK)
        return self.data

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

waveform = ok.playfile("KFlay-Blood-In-The-Cut.wav")
ok.setstream(waveform)
ok.readchunk(waveform)

while len(ok.data) > 0:
    ok.streamchunk(ok.readchunk(waveform))