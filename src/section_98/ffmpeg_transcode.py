import argparse
import logging
import os
import pathlib
import subprocess
import time

# Examples:
# Linux:
# $ python3 ffmpeg_transcode.py /media/usb/ffmpeg/in --crf 20 --preset slow
# Windows:
# $ python3 ffmpeg_transcode.py D:/ffmpeg/in --crf 20 --preset slow

# This is a great project to test overclocking - see here for more details:
# https://magpi.raspberrypi.org/articles/how-to-overclock-raspberry-pi-4

def _get_next_file(path):
    """Helper function to get next file in path."""
    p = sorted(pathlib.Path(path).glob("*"))
    files = [x for x in p if x.is_file() and not x.name.startswith(".")]
    return files[0] if files else None


def main(args):
    print("Start of main.")
    logging.info("Start of main.")
    while True:
        file = _get_next_file(args.inputpath)
        if not file:
            break
        print(f"Video file: {file.name}")
        logging.info(f"Video file: {file.name}")
        process_parameters = []
        process_parameters.append("ffmpeg")
        #process_parameters.append("-y")  # overwrite
        process_parameters.append("-n")  # do not overwrite, safer default
        process_parameters.append("-i")
        process_parameters.append(f"{str(file.resolve())}")
        process_parameters.append("-c:v")
        process_parameters.append("libx264")
        process_parameters.append("-preset")
        process_parameters.append(f"{args.preset}")
        process_parameters.append("-crf")
        process_parameters.append(f"{args.crf}")
        process_parameters.append("-c:a")
        process_parameters.append("copy")

        """
        process_parameters.append("-ss")
        process_parameters.append("1200") # Start location: 1200=20 minutes, 1800 =30 minutes
        process_parameters.append("-t")
        process_parameters.append("600") # Duration: 60=1 minute
        """

        process_parameters.append(
            f"{file.parent.parent / 'out' / file.stem}_CRF{args.crf}_{args.preset.upper()}.{args.outputformat.lower()}"
        )
        print(" ".join(process_parameters))
        logging.info(f'process_parameters: {" ".join(process_parameters)}')

        subprocess_output = subprocess.run(
            process_parameters, capture_output=True, text=True
        ).stderr
        print(subprocess_output)

        # move file to Archive directory so we don't try to process it again
        print("Transcode complete, moving video file to Archive directory.")
        logging.info("Transcode complete, moving video file to Archive directory.")
        archive_file_name = f"{file.parent / 'archive' / file.name}"
        pathlib.Path(f"{str(file.resolve())}").rename(archive_file_name)

    print("The End.")
    logging.info("The End.")


if __name__ == "__main__":
    if os.name == 'nt':
        default_input_path = "D:/ffmpeg/in" # Windows
    else:
        default_input_path ="/home/pi/Projects/ffmpeg/in"

    logging.basicConfig(
        level=logging.DEBUG,
        filename=f"{__file__.split('.')[0]}.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    parser = argparse.ArgumentParser(
        description="ffmpeg - convert all movies found in directory to output format, typically mp4 (default) or mkv."
    )
    parser.add_argument(
        "--inputpath",
        type=str,
        help="Input directory path.",
        #nargs='?', # '?' = a single value, which can be optional
        required=False,
        default=default_input_path,
    )
    parser.add_argument(
        "--crf",
        type=str,
        help="Constant Rate Factor (default=20).",
        required=False,
        default="20",
    )
    parser.add_argument(
        "--preset",
        type=str,
        help="Preset is a collection of options that will provide a certain encoding speed to compression ratio..",
        choices=[
            "ultrafast",
            "superfast",
            "veryfast",
            "faster",
            "fast",
            "medium",
            "slow", # 2 hours to transcode each 1 hour using crf 20 on Raspberry Pi 4
            "slower", # 3 hours to transcode each 1 hour using crf 20 on Raspberry Pi 4
            "veryslow", # 6 hours to transcode each 1 hour using crf 20 on Raspberry Pi 4
            "placebo",
        ],
        required=False,
        default="slow",
    )
    parser.add_argument(
        "--outputformat",
        type=str,
        help="Output format, typically mp4 (default) or mkv.",
        required=False,
        default="mp4",
    )
    arguments = parser.parse_args()
    print(arguments)
    main(arguments)
