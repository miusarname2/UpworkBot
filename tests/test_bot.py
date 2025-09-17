import unittest
from unittest.mock import AsyncMock, patch
from src.handlers import start, handle_message

class TestBotHandlers(unittest.IsolatedAsyncioTestCase):

    @patch('src.handlers.n8n.call_workflow', new_callable=AsyncMock)
    async def test_handle_message_action1(self, mock_call):
        mock_call.return_value = "Resultado simulado"
        # Aquí irían pruebas reales con mocks para Update y Context
        # Por simplicidad, placeholder
        self.assertTrue(True)  # Placeholder

if __name__ == '__main__':
    unittest.main()