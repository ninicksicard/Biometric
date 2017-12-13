import pyaudio
import wave



FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "file.wav"

class RecordStream:
    def SetStream(self):
        self.audio = pyaudio.PyAudio()
        self.frames = []
        self.stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                      rate=RATE, input=True,
                                      frames_per_buffer=CHUNK)
    def Record45Secs(self):
        for i in range(0, int(RATE / CHUNK * 5)):
            data = self.stream.read(CHUNK)
            self.frames.append(data)

    def RecordAFrame(self):
        print('recording')
        data = self.stream.read(CHUNK)
        self.frames.append(data)

    def StopStream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        try:
            self.lastrecordstream.stopit()
        except:
            pass
    def playlastrecord(self):
        lastrecordstream = OutputStream()
        lastrecordstream.setstream()
        datachunk = self.frames[0]
        frame = 1
        while len(self.frames) > frame:
            lastrecordstream.streamchunk(datachunk)
            datachunk = self.frames[frame]
            frame += 1

    def SetTrackToLastRecord(self):
        self.lastrecordstream = OutputStream()
        self.lastrecordstream.setstream()
        self.datachunk = self.frames[0]
        self.frame = 1
        self.PlayNextChunkOfTrack()

    def PlayNextChunkOfTrack(self):
        print("playing")
        if len(self.frames) > (self.frame+1):
            self.lastrecordstream.streamchunk(self.datachunk)
            self.datachunk = self.frames[self.frame]
            self.frame += 1


        else:
            self.lastrecordstream.stopit()
            self.SetTrackToLastRecord()


    def saveaudio(self):
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(self.frames))
        waveFile.close()

class OutputStream:
    def setstream(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  output=True)
    def streamchunk(self, data):
        self.stream.write(data)

    def stopit(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()



def playkflay():
    ok = OutputStream()
    wf = wave.open("KFlay-Blood-In-The-Cut.wav", 'rb')
    ok.setstream()
    data = wf.readframes(1024)
    while len(data) > 0:
        ok.streamchunk(wf.readframes(1024))

def playlastrecord():
    lastrecordstream = OutputStream()
    lastrecordstream.setstream()
    datachunk = frames[0]
    frame = 1
    while len(datachunk) > 0:
        lastrecordstream.streamchunk(datachunk)
        datachunk = frames[frame]
        frame += 1

# playthis = RecordStream()
# playthis.SetStream()
# playthis.Record45Secs()
# while True:
#     playthis.playlastrecord()
