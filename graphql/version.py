from typing import NamedTuple

__all__ = ["version", "version_info", "version_js", "version_info_js"]


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

    def __str__(self):
        v = f"{self.major}.{self.minor}.{self.micro}"
        level = self.releaselevel
        if level and level != "final":
            v = f"{v}{level[:1]}{self.serial}"
        return v


version = "1.1.0b0"

version_info = VersionInfo(1, 1, 0, "beta", 0)

version_js = "14.4.0"

version_info_js = VersionInfo(14, 4, 0, "final", 0)
