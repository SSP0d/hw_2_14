import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

from src.database.models import User
from src.repository.users import create_user, get_user_by_email, confirmed_email
from src.schemas import UserModel


class TestUser(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.body = UserModel(
            username="Vitalii",
            email="vitalii@email.com",
            password="1234567890"
        )

    async def test_create_user(self):
        body = self.body
        result = await create_user(body=body, db=self.session)
        self.assertEqual(result.username, body.username)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.password, body.password)
        self.assertTrue(hasattr(result, "id"))

    async def test_get_user_by_email(self):
        body = self.body
        await create_user(body=body, db=self.session)
        user = self.session.query(User).filter(User.email == body.email).first().email
        result = await get_user_by_email(email=body.email, db=self.session)
        self.assertEqual(result.email, user)


    async def test_confirmed_email(self):
        body = self.body
        await create_user(body=body, db=self.session)
        await confirmed_email(email=body.email, db=self.session)
        result = await get_user_by_email(email=body.email, db=self.session)
        self.assertEqual(result.confirmed, True)


if __name__ == '__main__':
    unittest.main()
