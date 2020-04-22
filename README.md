# hass-simpleicons

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

Use free icons from the [simpleicons](https://simpleicons.com) set in Home Assistant.

## Installation instructions

- Install using [HACS](https://hacs.xyz) (Or copy the contents of `custom_components/simpleicons/` to `<your config dir>/custom_components/simpleicons/`.)

- Restart Home Assistant

- Go to your integrations configuration and add simpleicons

## Usage

Find the icon you want in the [gallery](http://simpleicons.org/). Click on an icon. This will download the icon. You don't need that file, just it's filename.

The icon set is prefixed by: `si:`. Then comes the filename.

So,

- to get a facebook logo, use `si:facebook`
- to get a zigbee logo, use `si:zigbee`
- and so on

The icons are useable anywhere in Home Assistant - not only in lovelace.

## FAQ

### Can I set this up in configure.yaml instead?

Yes.

```yaml
simpleicons:
```

## Special thanks

This work is heavily based on [hass-fontawesome](https://github.com/thomasloven/hass-fontawesome) by Thomas Loven. Thank you!
