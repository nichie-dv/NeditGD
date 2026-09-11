import numpy as np
from NeditGD.Dictionaries.DataTypes import HSVString

def rgb_to_hsv(fR, fG, fB) -> tuple:
    """
    Converts an RGB color to HSV (given the base color is black).

    Args:
        fR: Red channel value.
        fG: Green channel value.
        fB: Blue channel value.

    Returns:
        A tuple containing hue (0-360), saturation (0-1),
        and value (0-1).
    """
    fCMax = max(fR, fG, fB)
    fCMin = min(fR, fG, fB)
    fDelta = fCMax - fCMin

    if fDelta > 0:
        if fCMax == fR:
            fH = 60 * (np.fmod(((fG - fB) / fDelta), 6))
        elif fCMax == fG:
            fH = 60 * (((fB - fR) / fDelta) + 2)
        elif fCMax == fB:
            fH = 60 * (((fR - fG) / fDelta) + 4)

        fS = fDelta / fCMax if fCMax > 0 else 0
        fV = fCMax
    else:
        fH = 0
        fS = 0
        fV = fCMax

    if fH < 0: fH += 360

    return fH, fS, fV

def rgb_to_hsvstring(fR, fG, fB) -> HSVString:
    """
    Converts an RGB color to HSV (given the base color is black).

    Args:
        fR: Red channel value.
        fG: Green channel value.
        fB: Blue channel value.

    Returns:
        A tuple containing hue (0-360), saturation (0-1),
        and value (0-1).
    """
    fCMax = max(fR, fG, fB)
    fCMin = min(fR, fG, fB)
    fDelta = fCMax - fCMin

    if fDelta > 0:
        if fCMax == fR:
            fH = 60 * (np.fmod(((fG - fB) / fDelta), 6))
        elif fCMax == fG:
            fH = 60 * (((fB - fR) / fDelta) + 2)
        elif fCMax == fB:
            fH = 60 * (((fR - fG) / fDelta) + 4)

        fS = fDelta / fCMax if fCMax > 0 else 0
        fV = fCMax
    else:
        fH = 0
        fS = 0
        fV = fCMax

    if fH < 0: fH += 360

    return HSVString(fH, fS, fV, True, True)