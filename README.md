### hass-simpleicons

```
$$$$$$$\                                                              $$\                     $$\ 
$$  __$$\                                                             $$ |                    $$ |
$$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$ |
$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|\____$$\\_$$  _|  $$  __$$\ $$  __$$ |
$$ |  $$ |$$$$$$$$ |$$ /  $$ |$$ |  \__|$$$$$$$$ |$$ /      $$$$$$$ | $$ |    $$$$$$$$ |$$ /  $$ |
$$ |  $$ |$$   ____|$$ |  $$ |$$ |      $$   ____|$$ |     $$  __$$ | $$ |$$\ $$   ____|$$ |  $$ |
$$$$$$$  |\$$$$$$$\ $$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$\\$$$$$$$ | \$$$$  |\$$$$$$$\ \$$$$$$$ |
\_______/  \_______|$$  ____/ \__|       \_______| \_______|\_______|  \____/  \_______| \_______|
                    $$ |                                                                          
                    $$ |                                                                          
                    \__|                                                                          
```

This integration is deprecated.

The integration has been unstable for some users, and keeping it up to date was quite a chore.

But there is a good alternative! Thomas Loven wrote an integration for a bunch of icons, including simple-icons:


## Migrate to hass-custom_icons

Check out the repository: https://github.com/thomasloven/hass-custom_icons

- Remove my simple-icons integration
- Add the hass-custom_icons integration (see https://github.com/thomasloven/hass-custom_icons)
- Restart home assistant
- Add integration
- Change settings: Download Iconify icons and reload local icons, refresh page, enable simple-icons
- Change your icons from `si:ICONNAME` to `simple-icons:ICONNAME`
