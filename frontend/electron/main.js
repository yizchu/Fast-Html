const { app, BrowserWindow } = require('electron')
const path = require("path")

const createWindow = () => {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
    })

    mainWindow.loadURL("http://localhost:3000");
}

app.whenReady().then(() => {
    createWindow()
})
