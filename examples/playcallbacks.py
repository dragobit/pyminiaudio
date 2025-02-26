"""
Shows a way to react on the end of a stream and device activities.
"""

import sys
import miniaudio


def stream_end_callback() -> None:
    print("\nSource stream ended!")


def stream_progress_callback(framecount: int) -> None:
    print(framecount, ",", end="", flush=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("use one argument: filename")
    filestream = miniaudio.stream_file(sys.argv[1])
    callbacks_stream = miniaudio.stream_with_callbacks(filestream, stream_progress_callback, stream_end_callback)
    next(callbacks_stream)  # start the generator
    with miniaudio.PlaybackDevice() as device:
        print("playback in background. press enter to exit:\n")
        device.start(callbacks_stream)
        input()
    print("Device playback stopped.")
