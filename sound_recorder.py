import pyaudio
import wave
import os
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 2


audio = pyaudio.PyAudio()
os.system('clear')

path = "data"
print ("Program akan merekam suara sebanyak 10 kali\n")
print ("Mohon untuk mengucapan password dengan suara yang jelas\n")
print ("Durasi tiap perekaman adalah 2 detik\n") 
recdir = input("masukan nama: ")

if not os.path.exists(os.path.join(path, recdir)):
	os.mkdir(os.path.join(path, recdir))

re = True
x = 0

while(re):
	WAVE_OUTPUT_FILENAME = os.path.join(path, recdir, (str(x) + ".wav"))

	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)
	print("Record voice no", x+1)
	print("Recording...")
	frames = []
	 
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)
	print("Finished Recording")
	 
	 
	# stop Recording
	stream.stop_stream()
	stream.close()
	 
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
	x = x + 1

	if(input("Repeat? y/n ") == "n"):
		re = False

audio.terminate()
