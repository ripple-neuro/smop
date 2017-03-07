import unittest
import xipppy
import xippmex
import mock

class TestTime(unittest.TestCase):
    """
    First test in this.  Still not sure how this is going to work out.

    Make sure that time calls call the right place.
    """
    def test_time(self):
        """
        Basic test and get a feel for the mocks.
        """
        xipppy.time = mock.MagicMock()
        xippmex.xippmex('time')
        xipppy.time.assert_called_with()
