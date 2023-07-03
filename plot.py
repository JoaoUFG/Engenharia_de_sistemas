import wave
import numpy as np
import matplotlib.pyplot as plt

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

# Cria um array de tempo para o eixo x
tempo = np.linspace(0, len(audio_data1) / params1.framerate, num=len(audio_data1))

# Plota os gráficos dos dois arquivos de áudio
plt.plot(tempo, audio_data1, color='blue', label='Audio 1')
plt.plot(tempo, audio_data2, color='red', label='Audio 2')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Gráfico das ondas dos arquivos de áudio')
plt.legend()
plt.show()
