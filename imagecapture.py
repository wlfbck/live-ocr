import win32gui
import win32ui
import win32con
from pynput.mouse import Listener


# https://stackoverflow.com/questions/57761132/area-selection-and-capture-of-the-screen-with-python-on-windows
def getImage(x, y, width, height, path):
    # grab a handle to the main desktop window
    hdesktop = win32gui.GetDesktopWindow()

    # create a device context
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()

    # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (x, y), win32con.SRCCOPY)

    # save the bitmap to a file
    screenshot.SaveBitmapFile(mem_dc, path)
    # free our objects
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())


# https://stackoverflow.com/questions/63126967/how-to-detect-mouse-click-and-keypress
# if this gets executed we want to get the points. needs to be force killed afterwards
if __name__ == '__main__':
    def on_click(x, y, button, pressed):
        if pressed:
            print("Mouse clicked: " + str(x) + ", " + str(y))


    with Listener(on_click=on_click) as listener:
        listener.join()
