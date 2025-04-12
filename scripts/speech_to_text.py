import speech_recognition as sr
import time
import pyaudio
import wave
import threading

def test_microphone(device_index, duration=3):
    """Records audio and plays it back to test the microphone."""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "test_mic.wav"

    audio = pyaudio.PyAudio()

    try:
        print(f"\n🎤 Testing microphone (index {device_index})... Speak now!")
        
        # Record audio
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            input_device_index=device_index,
            frames_per_buffer=CHUNK
        )
        
        frames = []
        for _ in range(0, int(RATE / CHUNK * duration)):
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("✅ Recording complete. Playing back...")
        
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        
        # Save the recorded data as a WAV file
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        # Play back the recorded audio
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            output=True,
            output_device_index=None  # Default playback device
        )
        
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
        data = wf.readframes(CHUNK)
        
        while data:
            stream.write(data)
            data = wf.readframes(CHUNK)
        
        stream.stop_stream()
        stream.close()
        print("🔊 Playback finished. Did you hear your voice clearly?")
        return True
        
    except Exception as e:
        print(f"❌ Microphone test failed: {e}")
        return False
    finally:
        audio.terminate()

def list_microphones():
    """List all available microphones with indices."""
    print("\nAvailable microphones:")
    mics = sr.Microphone.list_microphone_names()
    for index, name in enumerate(mics):
        print(f"{index}: {name}")
    return mics

def run_speech_to_text(mic_index):
    """Run speech recognition on selected microphone with early exit option."""
    recognizer = sr.Recognizer()
    stop_listening = False
    
    def wait_for_enter():
        nonlocal stop_listening
        input("Press Enter to stop listening...\n")
        stop_listening = True
    
    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("\n🔊 Adjusting for ambient noise (wait 2 sec)...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            
            # Start thread to watch for Enter key
            stop_thread = threading.Thread(target=wait_for_enter)
            stop_thread.daemon = True
            stop_thread.start()
            
            print("🎤 Speak now (listening for up to 60 seconds, press Enter to stop early)...")
            
            start_time = time.time()
            audio_frames = []
            
            while not stop_listening and (time.time() - start_time) < 60:
                try:
                    audio = recognizer.listen(source, timeout=1, phrase_time_limit=1)
                    audio_frames.append(audio)
                except sr.WaitTimeoutError:
                    continue
            
            if audio_frames:
                # Combine all audio frames
                combined_audio = sr.AudioData(b''.join([a.get_raw_data() for a in audio_frames]),
                                            audio_frames[0].sample_rate,
                                            audio_frames[0].sample_width)
                
                print("✅ Audio captured! Processing...")
                
                try:
                    text = recognizer.recognize_google(combined_audio)
                    print(f"\n🎙️ You said: {text}")
                    return text
                except sr.UnknownValueError:
                    print("❌ Google could not understand audio (too quiet/unclear?)")
                except sr.RequestError as e:
                    print(f"❌ Google API error: {e}")
            else:
                print("⏳ No speech detected")
                
    except Exception as e:
        print(f"❌ Error with microphone: {e}")
    return None

def main_menu():
    """Main menu for microphone testing and speech recognition."""
    print("\n" + "="*40)
    print("Microphone Tool")
    print("="*40)
    
    mics = list_microphones()
    
    while True:
        print("\nMain Menu:")
        print("1. Test Microphone")
        print("2. Speech to Text (up to 60 sec)")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            # Test Microphone
            try:
                mic_index = int(input(f"Enter microphone index (0-{len(mics)-1}): "))
                if 0 <= mic_index < len(mics):
                    test_microphone(mic_index)
                else:
                    print("❌ Invalid index!")
            except ValueError:
                print("❌ Please enter a number!")
                
        elif choice == "2":
            # Speech to Text
            try:
                mic_index = int(input(f"Enter microphone index (0-{len(mics)-1}): "))
                if 0 <= mic_index < len(mics):
                    run_speech_to_text(mic_index)
                else:
                    print("❌ Invalid index!")
            except ValueError:
                print("❌ Please enter a number!")
                
        elif choice == "3":
            print("👋 Exiting...")
            break
            
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n👋 Exiting...")