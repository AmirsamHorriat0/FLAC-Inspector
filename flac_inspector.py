import sys
import librosa
import os
from mutagen.flac import FLAC
from utils import audio_score

def inspect_flac(flac_file) :
    audio = FLAC(flac_file)
    sample_rate = audio.info.sample_rate
    bit_depth = audio.info.bits_per_sample
    channels = audio.info.channels
    bitrate = audio.info.bitrate
    length = audio.info.length

    print('''
                                                                                                                     
@@@@@@@@ @@@       @@@@@@   @@@@@@@    @@@ @@@  @@@  @@@@@@ @@@@@@@  @@@@@@@@  @@@@@@@ @@@@@@@  @@@@@@  @@@@@@@  
@@!      @@!      @@!  @@@ !@@         @@! @@!@!@@@ !@@     @@!  @@@ @@!      !@@        @!!   @@!  @@@ @@!  @@@ 
@!!!:!   @!!      @!@!@!@! !@!         !!@ @!@@!!@!  !@@!!  @!@@!@!  @!!!:!   !@!        @!!   @!@  !@! @!@!!@!  
!!:      !!:      !!:  !!! :!!         !!: !!:  !!!     !:! !!:      !!:      :!!        !!:   !!:  !!! !!: :!!  
 :       : ::.: :  :   : :  :: :: :    :   ::    :  ::.: :   :       : :: ::   :: :: :    :     : :. :   :   : : 
                                                                                                                 ''')
    print(f"\nFLAC Inspector")
    print(f"-------------------")
    print(f"File       : {flac_file}")
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Bit Depth  : {bit_depth}-bit")
    print(f"Channels   : {channels}")
    print(f"Bitrate    : {bitrate} bps")
    print(f"Length     : {length:.2f} sec")

    # load the audio file
    y , sr = librosa.load(flac_file , sr=None , duration=180 )

    # Audio Score
    score = audio_score(sample_rate, bit_depth, bitrate)
    print(f"Score: {score} / 100")

    # Calculate expected bitrate
    file_size_bits = os.path.getsize(flac_file) * 8
    expected_bitrate = file_size_bits / length

    # Max PCM bitrate
    max_pcm_bitrate = sample_rate * channels * bit_depth

    min_bitrate = max_pcm_bitrate * 0.25

    print(f"\nExpected bitrate: {expected_bitrate / 1000:.1f} kbps")
    print(f"Max PCM bitrate : {max_pcm_bitrate / 1000:.1f} kbps")

    # Verdict based on expected bitrate and audio score
    if expected_bitrate < min_bitrate:
        print("Fake FLAC 💩")
    elif score > 80:
        print("High-Res Lossless ⭐⭐⭐⭐⭐")
    elif score > 70:
        print("Good Quality  ⭐⭐⭐")
    else:
        print(" CD FLAC ⭐⭐")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 flac_inspector.py path/to/file.flac")
        sys.exit(1)
    inspect_flac(sys.argv[1])






