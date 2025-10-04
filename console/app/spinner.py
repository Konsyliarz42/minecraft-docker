# https://www.compart.com/en/unicode/block/U+2800

from threading import Thread
from time import sleep
from types import TracebackType
from typing import Final

from .styled_string import Color, styled_string

__all__ = ["Spinner"]


class Spinner:
    DOTS: Final[tuple[str, ...]] = ("⣸", "⣴", "⣦", "⣇", "⡏", "⠟", "⠻", "⢹")

    def __init__(self, message: str = "", color: Color = Color.BLUE) -> None:
        self.message = message
        self.color = color

        self._start = False
        self.thread: Thread | None = None

    def __enter__(self) -> None:
        self.start()

    def __exit__(
        self,
        _type: type[BaseException] | None,
        _value: BaseException | None,
        _traceback: TracebackType | None,
    ) -> None:
        self.stop()

    def _spin(self) -> None:
        dots = styled_string(Spinner.DOTS[0], self.color)
        print(f"{dots} {self.message}", end="", flush=True)

        while self._start:
            for dot in Spinner.DOTS:
                dots = styled_string(dot, self.color)
                print(f"\r{dots} {self.message}", end="", flush=True)
                sleep(0.1)

        print("\r", " " * (len(self.message) + 2), end="\r", flush=True)

    def start(self, message: str | None = None) -> None:
        if self.thread and self.thread.is_alive():
            raise Exception("The spinner has already started")

        self.message = message if message is not None else self.message
        self._start = True
        self.thread = Thread(target=self._spin)
        self.thread.start()

    def stop(self) -> None:
        self._start = False

        if self.thread and self.thread.is_alive():
            self.thread.join()
