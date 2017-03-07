import unittest
import xipppy
import xippmex
import mock

class TestBasicCont(unittest.TestCase):
    """
    Test calls to LFP
    """
    def test_cont_lfp(self):
        xipppy.cont_lfp = mock.MagicMock()
        xippmex.xippmex('cont', 1, 1, 'lfp')
        xipppy.cont_lfp.assert_called_with(1, 1, 0)

    def tests_cont_raw(self):
        xipppy.cont_raw = mock.MagicMock()
        xippmex.xippmex('cont', 1, 1, 'raw')
        xipppy.cont_raw.assert_called_with(30, 1, 0)

    def tests_cont_hires(self):
        xipppy.cont_hires = mock.MagicMock()
        xippmex.xippmex('cont', 1, 1, 'hires')
        xipppy.cont_hires.assert_called_with(2, 1, 0)

    def tests_cont_hifreq(self):
        xipppy.cont_hifreq = mock.MagicMock()
        xippmex.xippmex('cont', 1, 1, 'hifreq')
        xipppy.cont_hifreq.assert_called_with(7, 1, 0)
