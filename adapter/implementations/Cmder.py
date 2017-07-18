import os
import xml.etree.ElementTree as et

from adapter import TerminalAdapterInterface

class Cmder(TerminalAdapterInterface):

    @staticmethod
    def is_available():
        return os.environ.get("CMDER_ROOT") == '1'

    def set_image_file_path(self, image_file_path):
        config = input("Please input abslute location of user-ConEmu: ")

        tree = et.parse(config)
        

        raise NotImplementedError()

    def clear(self):
        """
        Clear the terminal's background image.
        """
        raise NotImplementedError()