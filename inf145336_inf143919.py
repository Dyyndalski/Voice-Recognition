import glob
from scipy.io import wavfile
from pylab import *
import sys
import numpy as np
from numpy.fft import *
import copy
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
from pydub import AudioSegment
import pydub


def HPS(rate, data_sound):

    parts = []
    result_parts = []

    for i in range(int(len(data_sound) / rate)):
        parts.append(data_sound[i * rate: (i + 1) * rate])

    for part_data in parts:
        if len(part_data) != 0:

            #transformata furiera
            window = np.hamming(len(part_data))
            data = part_data * window
            fftV = abs(fft(part_data)) / rate
            fftR = copy.copy(fftV)

            #iloczyn spektrum i harmoniczne
            for i in range(2, 5):
                tab = copy.copy(fftV[::i])
                fftR = fftR[:len(tab)]
                fftR = fftR * tab
            result_parts.append(fftR)

    result = [0]*len(result_parts[(int(len(result_parts)/2))])

    #suma
    for res in result_parts:
        if len(res) == len(result):
            result = result + res
    return result

def checkGender(result):
    men_min = 50 #przedział f dla mezczyzn
    men_max = 160
    wom_min = 180 #przedzail f dla kobiet
    wom_max = 270

    #szacowanie płci
    if sum(result[wom_min:wom_max]) < sum(result[men_min:men_max]):
        return "M"
    return "K"

def checkEfficiency(folderName): #funkcja do porównywania otrzymanego wyniku do rzeczywistego
    found_m = 0
    found_k = 0

    real_m = 0
    real_k = 0

    files = glob.glob(str(folderName)+"/*.wav") #NAZWA FOLDERU
    for file in files:
        originalSound = AudioSegment.from_wav(file)
        sound = originalSound.set_channels(1)
        sound.export(file, format="wav")
        rate, array = wavfile.read(file)
        originalSound.export(file, format="wav")
        found = HPS(rate, array)
        found = checkGender(found)

        if(file.replace("/", "_").replace(".", "_").split("_")[1] == "M"):
            real_m = real_m + 1
        else:
            real_k = real_k + 1

        if(found == "M"):
            found_m = found_m + 1
        else:
            found_k = found_k + 1

    print("Znaleziono męskich głosów:", found_m, " było:", real_m)
    print("Znaleziono damskich głosów:", found_k, " było:", real_k)

    if(found_m != found_k):
        if(found_m > real_m):
            eff = (real_m + real_k) - (found_m - real_m) / (real_m + real_k)
        else:
            eff = (real_m + real_k) - (found_k - real_k) / (real_m + real_k)

    print("Skutecznosc algorytmu wynosi:", eff, "%")

if __name__ == "__main__":

    if(str(sys.argv[1])) == "folder":
        checkEfficiency(sys.argv[2])
    else:
        originalSound = AudioSegment.from_wav(str(sys.argv[1]))
        sound = originalSound.set_channels(1)
        sound.export(str(sys.argv[1]), format="wav")
        rate, array = wavfile.read(str(sys.argv[1]))
        originalSound.export(str(sys.argv[1]), format="wav")
        result = HPS(rate, array)
        solution = checkGender(result)
        print(solution)
