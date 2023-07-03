import wave
import numpy as np

# Carregar o arquivo WAV
#filename = 'sin.wav'
filename = './input.wav'
wav_file = wave.open(filename, 'rb')

# Obter os parâmetros do arquivo WAV
params = wav_file.getparams()
num_frames = params.nframes
sample_width = params.sampwidth

# Ler os dados do arquivo WAV
wave_data = wav_file.readframes(num_frames)

# Converter os dados do arquivo WAV em um array NumPy
audio_array = np.frombuffer(wave_data, dtype=np.int16)

# Inverter a fase da onda de áudio
inverted_audio_array = -audio_array

# Criar um novo arquivo WAV para o som de fase invertida
output_filename = 'output.wav'
output_file = wave.open(output_filename, 'wb')
output_file.setparams(params)

# Escrever os dados do som de fase invertida no arquivo WAV
output_file.writeframes(inverted_audio_array.tobytes())

# Fechar os arquivos
wav_file.close()
output_file.close()


