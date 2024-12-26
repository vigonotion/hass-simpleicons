import logging

from homeassistant import config_entries

_LOGGER = logging.getLogger(__name__)


@config_entries.HANDLERS.register("simpleicons")
class simpleiconsConfigFlow(config_entries.ConfigFlow):
    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(title="", data={})

    async_step_import = async_step_user
