const fs = require('fs');
const { readPsd, initializeCanvas } = require('ag-psd');
const { createCanvas } = require('canvas');
initializeCanvas(createCanvas);

function extractLayerStructure(psd) {
    const structure = {
        children: []
    };

    function processLayer(layer) {
        const layerInfo = {
            name: layer.name || '',
            top: layer.top,
            left: layer.left,
            right: layer.right,
            bottom: layer.bottom,
            width: layer.right - layer.left,
            height: layer.bottom - layer.top,
            blendMode: layer.blendMode,
            opacity: layer.opacity,
            hidden: layer.hidden,
            layerId: layer.layerId,
            type: layer.type,
            layerClass: layer.layerClass,
            text: layer.text ? {
                value: layer.text.value,
                font: layer.text.font,
                size: layer.text.size,
                color: layer.text.color,
            } : null,
            children: []
        };

        if (layer.children) {
            layer.children.forEach(child => {
                layerInfo.children.push(processLayer(child));
            });
        }

        return layerInfo;
    }

    psd.children.forEach(child => {
        structure.children.push(processLayer(child));
    });

    return structure;
}

async function readPsdFile(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, (err, data) => {
            if (err) {
                reject(err);
                return;
            }
            resolve(data);
        });
    });
}

async function handlePsdFile(filePath) {
    try {
        const psdData = await readPsdFile(filePath);
        const psd = await readPsd(psdData);
        const layerStructure = extractLayerStructure(psd);
        fs.writeFile("page.json", JSON.stringify(layerStructure, null, 2), (err) => {
            if (err) {
                console.error('Error writing file:', err);
            } else {
                console.log('Layer structure saved to page.json');
            }
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

module.exports = {
    handlePsdFile
};
