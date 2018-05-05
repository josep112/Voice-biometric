# ome time ago I wrote some of the steps

# Record audio input on a n% gate threshold
# A: Start a Boolean variable type for "Silence" and you can calculate RMS to decide if Silence is true or False, Set one RMS Threshold

# stop recording after so many seconds of silence
# A: Do you need calculate one timeout, for it get the Frame Rate, Chunk Size and how many seconds do you want, to calculate your timeout make (FrameRate / chunk * Max_Seconds)

# keep recording for so many seconds after audio
# A: If Silence is false == (RMS > Threshold) get the last chunk of data of audio (LastBlock) and just keep record :-)

# Phase 2: input data into MySQL database to search the recordings
# A: This step is up to you


import pyaudio
import math
import struct
import wave



#Assuming Energy threshold upper than 30 dB
Threshold = 30

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2
Max_Seconds = 2
TimeoutSignal=((RATE / chunk * Max_Seconds) + 2)
silence = True
FileNameTmp = '/home/ubuntu/Desktop/4.wav'
Time=0
all =[]

def GetStream(chunk):
    return stream.read(chunk)



def rms(frame):
        count = len(frame)/swidth
        format = "%dh"%(count)
        shorts = struct.unpack( format, frame )

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n*n
        rms = math.pow(sum_squares/count,0.5);

        return rms * 1000



def WriteSpeech(WriteData):
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(FileNameTmp, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(WriteData)
    wf.close()



def KeepRecord(TimeoutSignal, LastBlock):


    all.append(LastBlock)
    for i in range(0, TimeoutSignal):
        try:
            data = GetStream(chunk)
        except:
            continue
        #I chage here (new Ident)
        all.append(data)

    print ("end record after timeout")
    data = ''.join(all)
    print ("write to File")
    WriteSpeech(data)
    silence = True
    Time=0
    listen(silence,Time)     

def listen(silence,Time):
    print ("waiting for Speech")
    while silence:

        try:

            input = GetStream(chunk)

        except:

            continue


        rms_value = rms(input)

        if (rms_value > Threshold):

            silence=False

            LastBlock=input

            print ("I'm Recording....")
            KeepRecord(TimeoutSignal, LastBlock)

        Time = Time + 1

        if (Time > TimeoutSignal):
            print ("Time Out No Speech Detected")
            sys.exit()






p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk)




listen(silence,Time) 
