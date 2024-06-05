import unittest
import datetime
import time
import HtmlTestRunner

from NoteManager import NoteManager
from Note import Note
from TextNote import TextNote
from ListNote import ListNote
from MediaNote import MediaNote
from ImageNote import ImageNote
from AudioNote import AudioNote


class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.manager = NoteManager()

        self.note1 = Note("Note 1", ["tag1", "tag2"], 2)
        time.sleep(0.0001)
        self.note2 = Note("Note 2", ["tag1"], 3)
        time.sleep(0.0001)

        self.note3 = TextNote("Text Note 1", ["tag1", "tag2"], 12, "sfsfsdfdgfgf")
        time.sleep(0.0001)
        self.note4 = TextNote("Text Note 2", ["tag2", "tag3"], 4, "slkdfjsldfhs")
        time.sleep(0.0001)

        self.note5 = ListNote("List Note 1", ["tag3", "tag4"], 3, ["a", "b"])
        time.sleep(0.0001)
        self.note6 = ListNote("List Note 2", ["tag3", "tag5"], 5, ["c", "d"])
        time.sleep(0.0001)

        self.note7 = MediaNote("Media Note 1", ["tag4", "tag6", "tag7"], 6, "/sdsdsd/sdsds.ewe")
        time.sleep(0.0001)
        self.note8 = MediaNote("Media Note 2", ["tag4"], 7, "/werwer/werwer.qwe")
        time.sleep(0.0001)

        self.note9 = ImageNote("Image Note 1", ["tag5", "tag7"], 9, "/fsdfsf.ewe", 600)
        time.sleep(0.0001)
        self.note10 = ImageNote("Image Note 2", ["tag5", "tag6"], 8, "/sfssd/fghs.ewe", 800)
        time.sleep(0.0001)

        self.note11 = AudioNote("Audio Note 1", ["tag6", "tag8"], 10, "/ptsfsf/s.fdf", 3.5)
        time.sleep(0.0001)
        self.note12 = AudioNote("Audio Note 2", ["tag6", "tag7", "tag8", "tag9"], 11, "/psfsd.sf", 2.97)
        time.sleep(0.0001)

        # Now we artificially set updated_at to note5 and note9, so that we can test our method search_by_data_range
        # UPD: we set delay 0.0001 sec after every operation,
        self.note5.updated_at = datetime.datetime(2024, 6, 7, 12, 0, 0)
        self.note9.updated_at = datetime.datetime(2024, 6, 8, 12, 0, 0)

        self.manager.create(self.note1)
        self.manager.create(self.note2)
        self.manager.create(self.note3)
        self.manager.create(self.note4)
        self.manager.create(self.note5)
        self.manager.create(self.note6)
        self.manager.create(self.note7)
        self.manager.create(self.note8)
        self.manager.create(self.note9)
        self.manager.create(self.note10)
        self.manager.create(self.note11)
        self.manager.create(self.note12)

    def test_create_note_and_read_note_by_title(self):
        self.assertEqual(self.manager.read("Note 1"), self.note1)
        self.assertIsNone(self.manager.read("Note 3"))

    def test_update_note(self):
        self.manager.update("Note 2", importance=1)
        self.assertEqual(self.manager.read("Note 2").importance, 1)

    def test_delete_note_by_title(self):
        self.manager.delete("Text Note 1")
        self.assertIsNone(self.manager.read("Test Note 1"))

    def test_search_by_class(self):
        result = self.manager.search_by_class(ListNote)
        self.assertIn(self.note5, result)
        self.assertNotIn(self.note4, result)

    def test_search_by_date_range(self):
        start_date = datetime.datetime(2024, 6, 7, 0, 0, 0)
        end_date = datetime.datetime(2024, 6, 9, 0, 0, 0)
        result = self.manager.search_by_date_range(start_date, end_date)
        self.assertEqual(len(result), 2)

    def test_search_by_tags(self):
        result = self.manager.search_by_tags(["tag4", "tag6"])
        self.assertIn(self.note5, result)
        self.assertIn(self.note7, result)
        self.assertIn(self.note8, result)
        self.assertIn(self.note10, result)
        self.assertIn(self.note11, result)
        self.assertIn(self.note12, result)
        self.assertNotIn(self.note1, result)

    def test_sort_notes_by_title(self):
        result = self.manager.sort_notes(by="title")
        self.assertEqual(result, [self.note11, self.note12, self.note9,
                                  self.note10, self.note5, self.note6, self.note7,
                                  self.note8, self.note1, self.note2, self.note3, self.note4])

    def test_sort_notes_by_importance(self):
        result = self.manager.sort_notes(by="importance")
        self.assertEqual(result, [self.note3, self.note12, self.note11, self.note9,
                                  self.note10, self.note8, self.note7, self.note6,
                                  self.note4, self.note2, self.note5, self.note1])

    def test_sort_notes_by_updated_at(self):
        result = self.manager.sort_notes(by="updated_at")
        self.assertEqual(result, [self.note9, self.note5, self.note12,
                                  self.note11, self.note10, self.note8, self.note7,
                                  self.note6, self.note4, self.note3, self.note2, self.note1])

# To get report use python -m unittest -v > report.txt
if __name__ == '__main__':
    unittest.main()
