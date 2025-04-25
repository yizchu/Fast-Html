const { app, BrowserWindow, Menu } = require('electron');
const { createMenu, setMainWindow } = require('./menu');
const path = require('path');

const createMainWindow = () => {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        show: false,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            nodeIntegration: true,
        },
    });

    const menuTemplate = createMenu();
    const menu = Menu.buildFromTemplate(menuTemplate);
    Menu.setApplicationMenu(menu);
    setMainWindow(mainWindow);

    mainWindow.loadURL('http://localhost:3000');
    mainWindow.once('ready-to-show', () => {
        mainWindow.show();
        mainWindow.setTitle('Fast HTML');
    });

    mainWindow.on('closed', () => {
        if (!process.env.NEW_WINDOW) {
            app.quit();
        }
    });
};

app.whenReady().then(() => {
    createMainWindow();

    app.on('window-all-closed', () => {
        if (process.platform !== 'darwin') {
            app.quit();
        }
    });

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createMainWindow();
        }
    });
});