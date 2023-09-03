import unittest
from unittest.mock import Mock
from src.common_utils import persistent_execution


class TestPersistentExecution(unittest.IsolatedAsyncioTestCase):
    async def test_function(self):
        async def test_function():
            return 5

        result = await persistent_execution(test_function, logger_=Mock())
        self.assertEqual(result, 5)
