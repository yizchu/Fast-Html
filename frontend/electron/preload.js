const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    reload: () => {
        require('electron').ipcRenderer.send('reload-window');
    },
    openFile: () => ipcRenderer.invoke('dialog:openFile'),
    openDirectory: () => ipcRenderer.invoke('dialog:openDirectory'),
    sendDownload: (params) => ipcRenderer.send('download-page', params),
    onDownloadProgress: (callback) => {
        ipcRenderer.on('download-progress', callback);
    },
    onDownloadError: (callback) => {
        ipcRenderer.on('download-error', callback);
    }
});
