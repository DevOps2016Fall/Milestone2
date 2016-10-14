from __future__ import print_function
from unittest import TestCase
from mock import patch
import project.authentication as auth

class StandAloneTests(TestCase):
  """Teset the stand-alone module functions."""

  @patch('__builtin__.open')
  def test_login(self, mock_open):
    """
    Pass the Test
    :param mock_open:
    :return:
    """
    mock_open.return_value.read.return_value = "ncsu|cs"
    self.assertTrue(auth.login('ncsu','cs'))

  @patch('__builtin__.open')
  def test_login_failed(self,mock_open):
    mock_open.return_value.read.return_value = "ncsu|cs"
    self.assertTrue(auth.login('ncsu','ece'))

  @patch('__builtin__.open')
  def test_login_error(self,mock_open):
    """
    I/O error
    :param mock_open:
    :return:
    """
    mock_open.side_effect = IOError()
    self.assertTrue(auth.login('ncsu','cs'))



