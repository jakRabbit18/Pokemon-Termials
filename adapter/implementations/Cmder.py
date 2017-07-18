import os
import xml.etree.ElementTree as et

from adapter import TerminalAdapterInterface

class Cmder(TerminalAdapterInterface):

    @staticmethod
    def is_available():
        print("Getting CMDER_ROOT")
        return os.environ.get("CMDER_ROOT") is not None

    def set_image_file_path(self, image_file_path):
        setBackground(image_file_path, True)

    def clear(self):
        setBackground("C:/back.bmp", False)

    def setBackground(self, iamge_file_path, show):
        config = input("Please input absolute path for user-ConEmu: ")

        tree = et.parse(config)
        for elem in tree.iterfind('key/key/value[@name="Background Image"]'):
            elem.data.set(image_file_path)
        for elem in tree.iterfind('key/key/value[@name="Background Image show"]'):
            elem.data.set(show)