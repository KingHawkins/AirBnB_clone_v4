#!/usr/bin/python3
import unittest
import io
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review

"""The console unittest"""


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()

    def test_do_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create BaseModel")
            base_id = f.getvalue().strip()
            self.assertEqual(len(base_id), 36)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertEqual(len(user_id), 36)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create Place")
            place_id = f.getvalue().strip()
            self.assertEqual(len(place_id), 36)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create City")
            city_id = f.getvalue().strip()
            self.assertEqual(len(city_id), 36)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create Amenity")
            amenity_id = f.getvalue().strip()
            self.assertEqual(len(amenity_id), 36)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create State")
            state_id = f.getvalue().strip()
            self.assertEqual(len(state_id), 36)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create Review")
            review_id = f.getvalue().strip()
            self.assertEqual(len(review_id), 36)

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("create NotAClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_do_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("show basemodel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("show BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_quit(self):
        """tests if quit works"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.assertTrue(self.hbnb.do_quit(''))
        self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.assertTrue(self.hbnb.do_EOF(''))
        self.assertEqual(fake_out.getvalue(), '')

    def test_emptyline(self):
        """tests if empty line works"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd('')
            self.assertEqual(f.getvalue(), '')

    def test_destroy(self):
        """checks for destroy"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd('destroy')
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd('destroy basemodel')
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy BaseModel 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy user")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy amenity")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy Amenity")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy Amenity 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy place")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy Place")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy Place 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy State")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy State 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy City")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy Review")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy City 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.hbnb.onecmd("destroy Review 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
