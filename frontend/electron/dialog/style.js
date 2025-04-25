import { BrowserWindow } from 'electron';
import { fileURLToPath } from 'url';

import path from "path";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
let styleWindow = null;

function setStyleWindow(mainWindow) {
    if (styleWindow) {
        styleWindow.close();
        styleWindow = null;
        return null;
    }

    styleWindow = new BrowserWindow({
        width: 400,
        height: 600,
        show: false,
        parent: mainWindow,
        modal: false,
        frame: true,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            nodeIntegration: true,
        },
    });
    styleWindow.loadURL('http://localhost:3000/style');
    styleWindow.webContents.once('did-finish-load', () => {
        styleWindow.show();
        styleWindow.setTitle("样式");
    })
    styleWindow.on('closed', () => {
        styleWindow = null;
    });
    return styleWindow;
}
export { setStyleWindow };