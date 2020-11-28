import argparse
import csv
import librosa
import numpy as np
import os


def store_mfccs(mfccs, sound_file):
    mfcc_outf = os.path.join(
        "data", "mfcc_output", sound_file + "-mfccs.csv"
    )

    np.savetxt(mfcc_outf, mfccs, delimiter=",")


def store_delta_mfccs(mfccs, sound_file, order):
    delta_mfccs = librosa.feature.delta(mfccs, order=order)

    delta_mfcc_outf = os.path.join(
        "data",
        "mfcc_" + "delta" * order + "_output",
        sound_file + "-delta" * order + "-mfccs.csv",
    )

    np.savetxt(delta_mfcc_outf, delta_mfccs, delimiter=",")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("sound_files", type=str, nargs="+")
    parser.add_argument(
        "--delta_order",
        type=int,
        default=2,
        help="The order of the MFCC delta must be 0, 1 or 2.",
    )

    args = parser.parse_args()

    if args.delta_order not in (0, 1, 2):
        raise ValueError("The order of the delta MFCCs must be 0, 1 or 2.")

    # Prepare statistics file.
    stats_path = "data/file_statistics.csv"
    with open(stats_path, "a") as stats_file:
        writer = csv.writer(stats_file, delimiter="\t")
        if os.path.getsize(stats_path) == 0:
            writer.writerow(["file_name", "duration", "n_samples", "sampling_rate"])

        for sound_path in args.sound_files:
            file_base, file_ext = os.path.splitext(os.path.basename(sound_path))

            # The parameter "sr" is set to None to obtain the original sampling rate.
            signal, sampling_rate = librosa.load(sound_path, sr=None)
            mfccs = librosa.feature.mfcc(
                signal, n_mfcc=13, sr=sampling_rate, n_fft=1012, hop_length=256
            )

            # Store audio file statistics.
            duration = librosa.get_duration(signal, sr=sampling_rate)
            n_samples = len(signal)
            writer.writerow([file_base + file_ext, duration, n_samples, sampling_rate])

            # Store MFCCS.
            store_mfccs(mfccs, file_base)

            # Store delta MFCCs by order.
            if args.delta_order > 0:
                store_delta_mfccs(mfccs, file_base, 1)
                if args.delta_order > 1:
                    store_delta_mfccs(mfccs, file_base, 2)
