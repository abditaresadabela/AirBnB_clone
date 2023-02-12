import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from console import HBNBCommand


class TestHBNBCommand(TestCase):
    def setUp(self):
        self.hbnb = HBNBCommand()
        self.input_string = "create BaseModel"

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd(self.input_string)
            output = f.getvalue()
            self.assertIn("BaseModel", output)
            self.assertIn("created", output)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("show BaseModel")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd(self.input_string)
            self.hbnb.onecmd("show BaseModel")
            output = f.getvalue()
            self.assertIn("BaseModel", output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("destroy BaseModel")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd(self.input_string)
            self.hbnb.onecmd("destroy BaseModel")
            output = f.getvalue()
            self.assertIn("BaseModel", output)
            self.assertIn("destroyed", output)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd("all")
            output = f.getvalue()
            self.assertIn("** class doesn't exist **", output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb.onecmd(self.input_string)
            self.hbnb.onecmd("all")
            output = f.getvalue()
            self.assertIn("BaseModel", output)

    def test_update(self):
        with patch('sys.std
