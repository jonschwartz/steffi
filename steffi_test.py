from contextlib import redirect_stdout
import io
import steffi
import unittest


class MainTest(unittest.TestCase):
    def test_info(self) -> None:
        steffi.log_level = 4
        with redirect_stdout(io.StringIO()) as result:
            steffi.info('this')
        self.assertEqual(result.getvalue(), 'this\n')

        steffi.log_level = 3
        with redirect_stdout(io.StringIO()) as result:
            steffi.info('this')
        self.assertEqual(result.getvalue(), '')

        steffi.log_level = 2
        with redirect_stdout(io.StringIO()) as result:
            steffi.info('this')
        self.assertEqual(result.getvalue(), '')

        steffi.log_level = 1
        with redirect_stdout(io.StringIO()) as result:
            steffi.info('this')
        self.assertEqual(result.getvalue(), '')

    def test_warn(self) -> None:
        steffi.log_level = 4
        with redirect_stdout(io.StringIO()) as result:
            steffi.warn('this')
        self.assertEqual(result.getvalue(), 'this\n')

        steffi.log_level = 3
        with redirect_stdout(io.StringIO()) as result:
            steffi.warn('this')
        self.assertEqual(result.getvalue(), 'this\n')

        steffi.log_level = 2
        with redirect_stdout(io.StringIO()) as result:
            steffi.warn('this')
        self.assertEqual(result.getvalue(), '')

        steffi.log_level = 1
        with redirect_stdout(io.StringIO()) as result:
            steffi.warn('this')
        self.assertEqual(result.getvalue(), '')

    def test_error(self) -> None:
        steffi.log_level = 4
        with redirect_stdout(io.StringIO()) as result:
            steffi.error('this')
        self.assertEqual(result.getvalue(), 'this\n')

        steffi.log_level = 3
        with redirect_stdout(io.StringIO()) as result:
            steffi.error('this')
        self.assertEqual(result.getvalue(), 'this\n')

        steffi.log_level = 2
        with redirect_stdout(io.StringIO()) as result:
            steffi.error('this')
        self.assertEqual(result.getvalue(), 'this\n')

        steffi.log_level = 1
        with redirect_stdout(io.StringIO()) as result:
            steffi.error('this')
        self.assertEqual(result.getvalue(), '')


if __name__ == '__main__':
    unittest.main()
