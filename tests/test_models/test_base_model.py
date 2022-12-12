from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def test_save(self):
        basemodel = BaseModel()

    def test_to_dict(self):
        basemodel = BaseModel()
        kind = type(basemodel.to_dict())
        self.assertEqual(kind, dict)
        base_dict = basemodel.to_dict()
        created_at = type(base_dict['created_at'])
        self.assertTrue( created_at == str)

    def test_id(self):
        basemodel = BaseModel()

    def test_created_at(self):
        basemodel = BaseModel()

    def test_str(self):
        basemodel = BaseModel()


if __name__ == "__main__":
    unittest.main()
