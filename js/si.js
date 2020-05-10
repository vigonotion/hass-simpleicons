const simpleIcons = require('simple-icons');

async function getIcon(name) {
    var si = simpleIcons.get(name);

    if (si === undefined) return {};

    return {
        path: si.path,
        viewBox: "-1 -1 26 26",
    };
}

window.customIconsets = window.customIconsets || {};
window.customIconsets["si"] = getIcon;
