#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutTuples(Koan):
    # displays value in the index
    def test_creating_a_tuple(self):
        count_of_three =  (1, 2, 5)
        self.assertEqual(5, count_of_three[2])

    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):

        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # Note, assertRegex() uses regular expression pattern matching,
        # so you don't have to copy the whole message.

        # you cant assign this to a tuple so msg says "does not support"

        self.assertRegex(msg, 'does not support')

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three =  (1, 2, 5)
        with self.assertRaises(AttributeError): count_of_three.append("boom")

        # Tuples are less flexible than lists, but faster.

    def test_tuples_can_only_be_changed_through_replacement(self):
        # adds boom to the end of the tuple
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)
        list_count.append("boom")
        count_of_three = tuple(list_count)

        self.assertEqual((1, 2, 5, "boom"), count_of_three)

    def test_tuples_of_one_look_peculiar(self):
        # defining the classes of these inputs where adding a comma here makes them a tuple because there are multiple
        self.assertEqual(int, (1).__class__)
        self.assertEqual(tuple, (1,).__class__)
        self.assertEqual(tuple, ("I'm a tuple",).__class__)
        self.assertEqual(str, ("Not a tuple").__class__)

    def test_tuple_constructor_can_be_surprising(self):
        # tuple constructor this seperates all of the charcters from the string
        self.assertEqual(("S", "u", "r", "p", "r", "i", "s", "e", "!"), tuple("Surprise!"))

    def test_creating_empty_tuples(self):
        self.assertEqual(() , ())
        self.assertEqual(() , tuple()) #Sometimes less confusing

    def test_tuples_can_be_embedded(self):
        # is asking for value of place which is defined in 3rd variable
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(('Area 51', (37, 14, 6, 'N'), (115, 48, 40, 'W')), place)

    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        self.assertEqual('Cthulu', locations[2][0])
        self.assertEqual(15.56, locations[0][1][2])
