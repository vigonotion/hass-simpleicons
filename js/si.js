const simpleIcons = require('simple-icons');


var x = 2

var svg = "<svg><defs>";

for(var icon of Object.entries(simpleIcons)) {
    var path = icon[1].path;
    var slug = icon[1].slug;

    var g = "<g id=\"" + slug + "\" viewBox=\"-1 -1 26 26\"><path d=\"" + path + "\"/></g>";
    svg += g;
}

svg += "</defs></svg>"

const iconset = document.createElement("ha-iconset-svg");
iconset.name="si";
iconset.size=1024;
iconset.innerHTML = svg;
document.body.appendChild(iconset);