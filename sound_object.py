import winsound
import threading


def play_sound(filename: str) -> None:
    winsound.PlaySound(filename, winsound.SND_FILENAME)


def play_sounds_parallel(file_list: list[str]) -> None:
    threads = []
    for file in file_list:
        sound_thread = threading.Thread(target=play_sound, args=(file,))
        threads.append(sound_thread)
        sound_thread.start()

    for thread in threads:
        thread.join()


