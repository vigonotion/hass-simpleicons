import homeassistant.components.frontend
from homeassistant.components.frontend import _frontend_root
from homeassistant.config_entries import SOURCE_IMPORT

DOMAIN = "simpleicons"

DATA_EXTRA_MODULE_URL = 'frontend_extra_module_url'
ICONS_URL = '/'+DOMAIN+'/'
ICON_FILES = {
    'simpleicons': 'si.js'
}

async def async_setup(hass, config):
    hass.http.register_static_path(
        f"/{DOMAIN}/si.js",
        hass.config.path(f"custom_components/{DOMAIN}/data/si.js"),
        True
    )
    
    if DOMAIN not in config:
        return True
    
    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN, context={"source": SOURCE_IMPORT}
        )
    )

    register_modules(hass)
    return True

async def async_setup_entry(hass, config_entry):
    config_entry.add_update_listener(_update_listener)
    register_modules(hass)
    return True

async def async_remove_entry(hass, config_entry):
    register_modules(hass)
    return True

async def _update_listener(hass, config_entry):
    register_modules(hass)
    return True


def register_modules(hass):
    if DATA_EXTRA_MODULE_URL not in hass.data:
        hass.data[DATA_EXTRA_MODULE_URL] = set()
    url_set = hass.data[DATA_EXTRA_MODULE_URL]

    for k,v in ICON_FILES.items():
        url_set.remove(ICONS_URL+v)
        #if k in modules and modules[k] != False:
        url_set.add(ICONS_URL+v)
