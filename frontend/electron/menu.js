const { dialog, app, BrowserWindow } = require('electron');
const { handlePsdFile } = require('./psd/psdHandler');
const { setStyleWindow } = require('./dialog/style');
const path = require('path');
const { spawn } = require('child_process'); // 引入 spawn 方法
let mainWindow = null;

module.exports = {
    createMenu: () => {
        const menuTemplate = [
            {
                label: '文件',
                submenu: [
                    {
                        label: '新建窗口',
                        click: async () => {
                            const electronPath = process.execPath;
                            const appPath = app.getAppPath();
                            spawn(electronPath, [appPath], {
                                detached: true,
                                stdio: 'ignore',
                            }).unref();
                        },
                    },
                    {
                        label: '新建项目',
                        click: async () => {
                            mainWindow.setEnabled(false);
                            const { filePaths } = await dialog.showOpenDialog({
                                properties: ['openFile'],
                                filters: [{ name: 'PSD Files', extensions: ['psd'] }],
                            });
                            if (filePaths && filePaths.length > 0) {

                                await handlePsdFile(filePaths[0]);
                            }
                            mainWindow.focus();
                            mainWindow.setEnabled(true);

                        },
                    },
                    {
                        label: '打开项目',
                        click: async () => {
                            mainWindow.setEnabled(false);
                            const { canceled, filePaths } = await dialog.showOpenDialog({
                                properties: ['openDirectory'],
                            });
                            if (canceled || !filePaths.length) {
                                mainWindow.focus();
                                mainWindow.setEnabled(true);
                                return null;
                            }

                            const getAllFiles = (dirPath, arrayOfFiles = []) => {
                                const files = fs.readdirSync(dirPath);
                                for (const file of files) {
                                    const fullPath = path.join(dirPath, file);
                                    if (fs.statSync(fullPath).isDirectory()) {
                                        getAllFiles(fullPath, arrayOfFiles);
                                    } else {
                                        arrayOfFiles.push(fullPath.replace(/\\/g, '/'));
                                    }
                                }
                                return arrayOfFiles;
                            };
                            mainWindow.focus();
                            mainWindow.setEnabled(true);
                            return {
                                dirPath: filePaths[0].replace(/\\/g, '/'),
                                files: getAllFiles(filePaths[0]),
                            };
                        },
                    },
                    {
                        label: '退出',
                        click: () => {
                            app.quit();
                        },
                    },
                ],
            },
            {
                label: '窗口',
                submenu: [
                    {
                        label: '样式',
                        type: 'checkbox',
                        checked: false,
                        click: (menuItem) => {
                            const styleWindow = setStyleWindow(mainWindow);
                            if (styleWindow) {
                                styleWindow.on('closed', () => {
                                    menuItem.checked = false;
                                });
                            } else {
                                menuItem.checked = false;
                            }
                        },
                    },
                ],
            },
            {
                label: '用户',
                submenu: [],
            },
            {
                label: '帮助',
                submenu: [],
            },
        ];

        return menuTemplate;
    },
    setMainWindow: (window) => {
        mainWindow = window;
    },
};