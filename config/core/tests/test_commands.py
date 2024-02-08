"""
Test custom Django management commands.
"""

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

from psycopg2 import OperationalError as psycopg2Error
from unittest.mock import patch

@patch('core.management.commands.wait_for_db.Command.check')  # Mocking the check method of the wait_for_db command
class CommandTests(SimpleTestCase):
    """ Test wait_for_db command. """

    def test_wait_for_db_ready(self, patched_check):
        """ Test waiting for database when the database is ready. """
        patched_check.return_value = True  # Mocking the return value of the check method to indicate database readiness

        call_command('wait_for_db')  # Calling the wait_for_db command

        patched_check.assert_called_once_with(databases=['default'])  # Asserting that the check method was called with the correct arguments

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError. """

        # Configure the side effect of the patched check method
        patched_check.side_effect = [psycopg2Error] * 3 + \
            [OperationalError] * 4 + [True]

        # Calling the wait_for_db command
        call_command('wait_for_db')

        # Assert the number of times the check method was called
        self.assertEqual(patched_check.call_count, 8)

        # Assert that the check method was called with the correct argument
        patched_check.assert_called_with(databases=['default'])
