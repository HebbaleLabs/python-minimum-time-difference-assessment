import unittest
from parameterized import parameterized
from minimum_time_difference import minimum_time_difference

class MinimumTimeDifferenceTest(unittest.TestCase):

  @parameterized.expand([
    ('instants with same hour', ['00:00', '00:01'], 1),
    ('instants with different hour', ['00:00', '12:00'], 720),
    ('instants in ascending order', ['00:00', '01:00'], 60),
    ('instants with different hour and time', ['11:15', '12:14'], 59)
  ])
  def test_simple_difference_time_instants(self, name, time_instants,
      expected_time_difference):
    actual_time_difference = minimum_time_difference(time_instants)
    message = 'For input values: {0}, expected value = {1}, and actual value = {2}'.format(
      time_instants, expected_time_difference, actual_time_difference)
    self.assertEqual(expected_time_difference, actual_time_difference, message)

  @parameterized.expand([
    ('instants with increasing difference', ['00:00', '00:01', '00:10', '01:00', '10:00'], 1),
    ('instants with increasing difference', ['00:00', '00:09', '00:59', '23:00', '23:59'], 9),
    ('instants with decreasing difference', ['22:33', '20:33', '00:33', '00:30'], 3),
    ('instants with decreasing difference', ['18:57', '10:43', '01:56', '00:24'], 92),
    ('instants with increasing and decreasing difference', ['01:00', '01:20', '01:15', '01:11', '01:05'], 4),
    ('instants with increasing and decreasing difference', ['03:00', '03:30', '03:45', '03:20', '04:30'], 10)
  ])
  def test_relative_difference_time_instants(self, name, time_instants,
      expected_time_difference):
    actual_time_difference = minimum_time_difference(time_instants)
    message = 'For input values: {0}, expected value = {1}, and actual value = {2}'.format(
        time_instants, expected_time_difference, actual_time_difference)
    self.assertEqual(expected_time_difference, actual_time_difference, message)

  @parameterized.expand([
    ('duplicate instants', ['00:00', '00:01', '00:00'], 0),
    ('lower anticlockwise difference', ['23:59', '00:00'], 1),
    ('lower anticlockwise difference', ['23:59', '01:00'], 61),
    ('lower anticlockwise difference', ['23:59', '02:00'], 121)
  ])
  def test_difference_timeinstants_edgecases(self, name, time_instants,
      expected_time_difference):
    actual_time_difference = minimum_time_difference(time_instants)
    message = 'For input values: {0}, expected value = {1}, and actual value = {2}'.format(
      time_instants, expected_time_difference, actual_time_difference)
    self.assertEqual(expected_time_difference, actual_time_difference, message)
