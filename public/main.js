const { app, BrowserWindow } = require('electron')

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    })

    // win.loadFile('./index.html')
    win.loadURL('http://localhost:3000')

    // Open devtools
    win.webContents.openDevTools()
}

app.whenReady().then(createWindow)

// Quit when all windows are closed, except on macOS. Application and menu bar
// should remain active until user explicitly quits
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    // macOS re-creates a window in the app when the dock icon is clicked and
    // there are no other windows open
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
    }
})
