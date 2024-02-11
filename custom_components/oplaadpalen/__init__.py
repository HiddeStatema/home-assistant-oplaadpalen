"""
The "oplaadpalen" custom component.

oplaadpalen:
"""
from __future__ import annotations

import logging

from homeassistant.const import (
    CONF_ID,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "oplaadpalen"
_LOGGER = logging.getLogger(__name__)

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.states.set('oplaadpalen.favorite_id', config[CONF_ID])
    _LOGGER.info('setup', config)
    return True
