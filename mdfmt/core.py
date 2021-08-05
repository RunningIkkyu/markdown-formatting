"""

s: space
ec: english charater
zc: zh charater
zp: zh punctuation
ep: en punctuation
       s
START --> START --> 


"""
STATUS_ERROR = -1
STATUS_START = 1

class Formatter():
    """Formatter """
    def __init__(self):
        self.current_status = STATUS_START
        pass

    def format(self, s: str) -> str:
        return s

    def _get_status(self) -> int:
        return self.current_status

    def _set_status(self, status: int):
        self.current_status = status

    def status_transfer(self, c: str):
        """Transfer status based on current charater. """
        s = self._get_status()
        n = STATUS_START
        if s == STATUS_START:
            n = self.nextof_start(c)
        elif s == 0:
            pass
        else:
            pass
        self._set_status(n)

    def nextof_start(self, c: str) -> int:
        """
        Get next status from STATUS_START.
        """
        #               space
        # STATUS_START -------> STATUS_START
        if c.isspace():
            return STATUS_START
        return STATUS_ERROR
