import time
# audio file create
import pyaudio
import wave
def create_audio_file():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "./output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# audio to text
import speech_recognition as sr
def create_audio_text():
    time.sleep(1)
    # import library

    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile('./output.wav') as source:
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text, language="zh")
            print('Converting audio transcripts into text ...')
            if text:
                with open('./output.txt', 'w+', encoding='UTF-8') as fp:
                    fp.write(text)
        except:
            print('Sorry.. run again...')
