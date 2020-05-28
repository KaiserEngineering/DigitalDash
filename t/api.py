"""Testing basics of DigitalDash."""
import unittest
from test import Test
from main import GUI
from digitaldash.needle.needle import Needle
from digitaldash.needle.radial import NeedleRadial
from digitaldash.needle.linear import NeedleLinear
from digitaldash.needle.ellipse import NeedleEllipse
from digitaldash.ke_lable import KELabel
from digitaldash.alert import Alert
from digitaldash.massager import smooth
from static.constants import KE_PID

class BasicNeedle_TestCase(unittest.TestCase):

    def test_needle_simple(self):
        needles = (
            NeedleRadial(
                themeConfig=120, degrees=120, path='static/imgs/Stock/',
                pids=["0x0C"], pid="0x0C"
            ),
            NeedleEllipse(
                themeConfig=120, degrees=120, path='static/imgs/Dirt/',
                pids=["0x0C"], pid="0x0C"
            ),
            NeedleLinear(
                themeConfig=120, degrees=120, path='static/imgs/Linear/',
                pids=["0x0C"], pid="0x0C"
            ),
        )

        for needle in needles:
            offset = float(0) if needle.Type == 'Linear' else float(60)
            value  = float(0) if needle.Type == 'Linear' else float(-60.0)

            self.assertEqual(needle.degrees, float(120), needle.Type+" component sets degrees property correctly")
            self.assertEqual(needle.min, float(0), needle.Type+" component sets min property correctly")
            self.assertEqual(needle.max, float(8000), needle.Type+" component sets max property correctly")
            self.assertEqual(needle.true_value, needle.min, needle.Type+" component defaults to minimum value")
            self.assertEqual(needle.offset, offset, needle.Type+" component sets correct offset with negative min")
            self.assertEqual(needle.update, value, needle.Type+" component sets the correct rotational degrees (not true vlaue)")

            old_value = needle.update

            needle.setData(4000)
            value = float(50) if needle.Type == 'Linear' else float(0)

            self.assertEqual(needle.true_value, float(4000), needle.Type+" component defaults to minimum value")
            self.assertEqual(needle.update, smooth(New=value, Old=old_value), needle.Type+" component sets the correct rotational value with smoothing (not true value)")

class BasicLabels_TestCase(unittest.TestCase):

    def test_label_simple(self):
        label = KELabel(
            default        = 'hello, world',
            ConfigColor    = (1, 1, 1 ,1),
            ConfigFontSize = 25,
            data           = 0,
            pid            = "0x0C",
            **KE_PID["0x0C"]
        )
        self.assertEqual(label.text, "hello, world", "Default text value is set correctly")
        self.assertEqual(label.decimals, str(KE_PID["0x0C"]['decimals']), "Decimal place set correctly for label")

        label.setData(100)
        self.assertEqual(label.text, "hello, world100", "Default text value is set correctly form setData method")

        label = KELabel(
            default        = 'Min: ',
            data           = 1,
            pid            = "0x0B"
        )
        label.setData(0)
        self.assertEqual(label.text, "0", "Default text value is set correctly")
        label.setData(-100)
        self.assertEqual(label.text, "-100", "Min value sets correctly")

        label.setData(100)
        self.assertEqual(label.text, "-100", "Min value stays minimum seen")

        label = KELabel(
            default        = 'Max: ',
            data           = 1,
            pid            = "0x0B"
        )
        label.setData(0)
        self.assertEqual(label.text, "0", "Default text value is set correctly")
        label.setData(100)
        self.assertEqual(label.text, "100", "Max value sets correctly")

        label.setData(10)
        self.assertEqual(label.text, "100", "Max value stays max seen")

        # Test PID labels
        label = KELabel(
            default        = '__PID__',
            pid            = "0x0C"
        )
        self.assertEqual(label.text, "RPM", "Sets PID label correctly")

class BasicAlerts_TestCase(unittest.TestCase):
    def test_alert_simple(self):
        alert = Alert(
            value     = 100,
            op        = '>',
            index     = 0,
            priority  = 0,
            message   = 'Hello, from tests',
            pid       = "0x0B"
        )
        self.assertFalse(alert.check(99), "Check fails when it should")
        self.assertNotEqual(alert.text, 'Hello, from tests', "Do not set alert value")

        self.assertTrue(alert.check(101), "Check passes when it should")
        alert.change('', '')
        self.assertEqual(alert.text, 'Hello, from tests', "Do not set alert value")

if __name__ == '__main__':
    unittest.main()
