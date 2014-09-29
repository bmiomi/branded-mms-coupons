import unittest

from coupons import app
from coupons.utils import create_background_image, generate_barcode_image, \
                          open_image_file_from_url, send_coupon_via_mms

class TestCoupons(unittest.TestCase):
    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        pass

    def test_create_background_image_size(self):
        try:
            width, height = 640, 480
            img = create_background_image(width, height)
            self.assertEqual(img.size[0], width)
            self.assertEqual(img.size[1], height)
        except Exception as e:
            self.fail(e)

    def test_generate_barcode_image(self):
        try:
            barcode = generate_barcode_image('567890')
            self.assertEqual(barcode.size[0], 360)
            self.assertEqual(barcode.size[1], 280)
        except Exception as e:
            self.fail(e)

    def test_open_image_file_from_url(self):
        image = open_image_file_from_url( \
            'http://www.fullstackpython.com/theme/img/fsp-logo.png')
        self.assertIsNot(image, False)

    def test_open_image_file_from_url_incorrect_url(self):
        image = open_image_file_from_url( \
            'http://www.fullstackpython.com/theme/img/fsp-logo.ng')
        self.assertFalse(image)

    def test_get_upload_image(self):
        response = self.test_app.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCoupons)
    unittest.TextTestRunner().run(suite)
