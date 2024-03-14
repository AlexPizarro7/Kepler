import numpy as np
from astropy.time import Time
from astropy.coordinates import get_sun, get_body
from astropy import units as u


def moon_phase(year, month, day):
    """Returns the phase of the moon for a given date."""
    date = Time(f"{year}-{month}-{day}")
    moon = get_body("moon", date)
    sun = get_sun(date)
    elongation = sun.separation(moon)
    phase_angle = np.arccos(np.clip(np.cos(elongation), -1, 1)) * u.deg
    
    return phase_angle