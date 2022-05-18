import numpy as np
from pathlib import Path
from dataclasses import dataclass
from matplotlib.pyplot import Axes


@dataclass
class Measurement:
    time: np.ndarray
    Vr: np.ndarray  # x
    Vc: np.ndarray  # y


Mat = str  # Material name alias
Res = int  # Resistance alias (kilo-ohm)
