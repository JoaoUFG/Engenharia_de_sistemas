######################

import wave
import sounddevice as sd
import numpy as np

# Carregar os arquivos de áudio
audio1 = 'input.wav'
audio2 = 'output.wav'



# Ler o primeiro arquivo de áudio usando a biblioteca wave
with wave.open(audio1, 'rb') as wave_file:
    params1 = wave_file.getparams()
    frames1 = wave_file.readframes(params1.nframes)
    audio_data1 = np.frombuffer(frames1, dtype=np.int16)

# Ler o segundo arquivo de áudio usando a biblioteca wave
with wave.open(audio2, 'rb') as wave_file:
    params2 = wave_file.getparams()
    frames2 = wave_file.readframes(params2.nframes)
    audio_data2 = np.frombuffer(frames2, dtype=np.int16)

# Verificar se as taxas de amostragem são iguais
if params1.framerate != params2.framerate:
    print('As taxas de amostragem dos arquivos são diferentes. Não é possível comparar.')
    exit()

# Verificar se os tamanhos dos sinais são iguais
if len(audio_data1) != len(audio_data2):
    print('Os tamanhos dos sinais são diferentes. Não é possível comparar.')
    exit()

# Somar os sinais
combined_audio = audio_data1 + audio_data2

# Reproduzir os sinais combinados
sd.play(combined_audio, params1.framerate)

# Aguardar a reprodução terminar
sd.wait()