let icons = {};

async function getIcon(name) {
    let si = undefined;

    if (icons[name] !== undefined) {
        si = icons[name];
    } else {
        const response = await fetch(`/simpleicons/icons/${name}`);

        if (!response.ok) return {};
        si = await response.json();
        icons[name] = si;
    }

    return {
        path: si.path,
        viewBox: "-1 -1 26 26",
    };
}

async function getIconList() {
    const response = await fetch(`/simpleicons/icons`);

    if (!response.ok) return [];

    const icons = await response.json();

    return icons;
}

window.customIcons = window.customIcons || {};
window.customIcons["si"] = { getIcon, getIconList };