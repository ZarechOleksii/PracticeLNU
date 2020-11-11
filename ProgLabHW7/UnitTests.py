import unittest
from Collection import Collection
from Event import Event


class TestHW7(unittest.TestCase):
    test_dict = {'id': '1',
                 'duration': '1.2',
                 'price': '2.54',
                 'rest_name': '2',
                 'title': 'TestName',
                 'date': ['2020', '2', '22'],
                 'time': ['14', '30']}

    def test_file_name(self):
        self.assertTrue(Collection('ToRead.txt'), 'Fail file name (cannot happen)')

    def test_validation_id(self):
        wrong_ids = ['abc', '-5']
        for x in wrong_ids:
            self.test_dict['id'] = x
            self.assertEqual(Event(self.test_dict).id, -1)

        self.test_dict['id'] = '1'
        self.assertEqual(Event(self.test_dict).id, 1, 'ID was not accepted')

    def test_validation_duration(self):
        self.test_dict['duration'] = 'abc'
        self.assertNotEqual(Event(self.test_dict).id, 1, 'Duration is not a number')
        self.test_dict['duration'] = '-3'
        self.assertNotEqual(Event(self.test_dict).id, 1, 'Duration is negative')

        self.test_dict['duration'] = '2'
        self.assertEqual(Event(self.test_dict).id, 1, 'Duration did not let initialization to happen')
        self.assertEqual(Event(self.test_dict).duration, 2, 'Duration is wrong')
        self.test_dict['duration'] = '2.421'
        self.assertEqual(Event(self.test_dict).id, 1, 'Duration did not let initialization to happen')
        self.assertNotEqual(Event(self.test_dict).duration, 2.421, 'Duration is wrong')
        self.assertEqual(Event(self.test_dict).duration, 2.4, 'Duration is wrong')

    def test_validation_price(self):
        self.test_dict['price'] = 'abc'
        self.assertNotEqual(Event(self.test_dict).id, 1, 'Price is not a number')
        self.test_dict['price'] = '-3'
        self.assertNotEqual(Event(self.test_dict).id, 1, 'Price is negative')

        self.test_dict['price'] = '2'
        self.assertEqual(Event(self.test_dict).id, 1, 'Price did not let initialization to happen')
        self.assertEqual(Event(self.test_dict).price, 2, 'Price is wrong')
        self.test_dict['price'] = '2.421'
        self.assertEqual(Event(self.test_dict).id, 1, 'Price did not let initialization to happen')
        self.assertNotEqual(Event(self.test_dict).price, 2.421, 'Price is wrong')
        self.assertEqual(Event(self.test_dict).price, 2.42, 'Price is wrong')

    def test_validation_restaurant(self):
        self.test_dict['rest_name'] = 'abc'
        self.assertNotEqual(Event(self.test_dict).id, 1, 'Restaurant name is not a number')
        self.test_dict['rest_name'] = '5'
        self.assertNotEqual(Event(self.test_dict).id, 1, 'Restaurant name is not in the list')

        self.test_dict['rest_name'] = '2'
        self.assertEqual(Event(self.test_dict).id, 1, 'Restaurant name was not accepted')

    def test_validation_title(self):
        wrong_titles = ['-abc', '|abc', ':abc']

        for x in wrong_titles:
            self.test_dict['title'] = x
            self.assertNotEqual(Event(self.test_dict).id, 1)

        self.test_dict['title'] = 'abc'
        self.assertEqual(Event(self.test_dict).id, 1, 'Title was not accepted')

    def test_validation_date(self):
        wrong_dates = [['20a0', '2', '22'], ['2020', 'a', '22'], ['2020', '2', 'a'], ['2020', '2', '30'],
                       ['2019', '2', '29'], ['2019', '15', '15']]
        for x in wrong_dates:
            self.test_dict['date'] = x
            self.assertNotEqual(Event(self.test_dict).id, 1)

        self.test_dict['date'] = ['2020', '2', '28']
        self.assertEqual(Event(self.test_dict).id, 1, 'Date was not accepted')

    def test_validation_time(self):
        wrong_time = [['1a', '59'], ['14', '5a'], ['14', '60'], ['24', '00']]
        for x in wrong_time:
            self.test_dict['time'] = x
            self.assertNotEqual(Event(self.test_dict).id, 1)

        self.test_dict['time'] = ['14', '30']
        self.assertEqual(Event(self.test_dict).id, 1, 'Time was not accepted')

    def test_collection_basic(self):
        test_dict = {'id': '1',
                     'duration': '1.2',
                     'price': '2.54',
                     'rest_name': '2',
                     'title': 'TestName',
                     'date': ['2020', '2', '22'],
                     'time': ['14', '30']}
        test_event1 = Event(test_dict)
        test_dict['id'] = '2'
        test_event2 = Event(test_dict)
        test_collection = Collection('Tests/EmptyFile.txt')
        #   append, len and getitem test
        self.assertEqual(len(test_collection), 0, 'Wrong length')
        test_collection.append(test_event1)
        self.assertEqual(len(test_collection), 1, 'Wrong length')
        test_collection.append(test_event2)
        self.assertEqual(len(test_collection), 2, 'Wrong length')
        self.assertIs(test_collection[0], test_event1, 'Wrong object')
        self.assertIs(test_collection[1], test_event2, 'Wrong object')
        #   deletion test
        self.assertFalse(test_collection.delete_id('Wrong input'), 'Has to be false')
        self.assertFalse(test_collection.delete_id(57), 'Has to be false')
        self.assertTrue(test_collection.delete_id(1), 'Has to be true')
        self.assertEqual(len(test_collection), 1, 'Wrong length')
        self.assertIs(test_collection[0], test_event2, 'Wrong object')
        #   editing element test
        self.assertFalse(test_collection.edit_one(test_collection.find_by_id(2), 'title', '-abc'), 'Should not edit')
        self.assertTrue(test_collection.edit_one(test_collection.find_by_id(2), 'title', 'good name'), 'Should edit')

    def test_collection_sort_write(self):
        test_collection = Collection('Tests/SortTest.txt')

        def get_file_content(way):
            content_f = open(way, 'r')
            content_text = content_f.read()
            content_f.close()
            return content_text

        def compare(way):
            test_collection.rewrite()
            manual_action = get_file_content(way)
            program_action = get_file_content('Tests/SortTest.txt')
            self.assertEqual(manual_action, program_action)

        arguments = ['T', 'I', 'R', 'Da', 'Ti', 'D', 'P', 'I']
        comparisons = ['ByTitle.txt', 'ByID.txt', 'ByRestaurantName.txt', 'ByDate.txt', 'ByTime.txt', 'ByDuration.txt',
                       'ByPrice.txt', 'ByID.txt']

        for x in range(0, len(arguments)):
            test_collection.sorting2(arguments[x])
            compare('Tests/' + comparisons[x])

    def test_collection_searching(self):
        test_collection = Collection('Tests/SearchTest.txt')
        search_args = ['NotExists', '', '10', 'Event', '20']
        to_find = ['', '',
                   'Event with ID 10 has ID 10\nEvent with ID 5 has price 10.5\n',

                   'Event with ID 5 has title FourthEvent\nEvent with ID 10 has title firstEvent\n',

                   'Event with ID 1 has starting date 2019-05-25\n'
                   'Event with ID 5 has starting date 2005-11-22\n'
                   'Event with ID 10 has starting date 2021-12-31\n']

        for x in range(0, len(search_args)):
            self.assertEqual(test_collection.search2(search_args[x]), to_find[x])

    def test_history(self):
        test_dict = {'id': '1',
                     'duration': '1.2',
                     'price': '2.54',
                     'rest_name': '2',
                     'title': 'TestName',
                     'date': ['2020', '2', '22'],
                     'time': ['14', '30']}
        test_collection = Collection('TestsHistory/ChangingFile.txt')

        def get_file_content(way):
            content_f = open(way, 'r')
            content_text = content_f.read()
            content_f.close()
            return content_text

        def compare(way):
            test_collection.rewrite()
            manual_action = get_file_content(way)
            program_action = get_file_content('TestsHistory/ChangingFile.txt')
            self.assertEqual(manual_action, program_action)

        testing_funcs = [test_collection.delete_id, test_collection.delete_id, test_collection.append,
                         test_collection.delete_id, test_collection.undo, test_collection.undo,
                         test_collection.undo, test_collection.redo, test_collection.redo,
                         test_collection.undo, test_collection.delete_id, test_collection.redo,
                         test_collection.undo, test_collection.undo, test_collection.undo, test_collection.undo]
        arguments = [4, 1, Event(test_dict), 14, None, None, None, None, None, None, 8, None, None, None, None, None]
        comparisons = ['Action1.txt', 'Action2.txt', 'Action3.txt', 'Action4.txt', 'Action3.txt', 'Action2.txt',
                       'Action1.txt', 'Action2.txt', 'Action3.txt', 'Action2.txt', 'Action3Alternative.txt',
                       'Action3Alternative.txt', 'Action2.txt', 'Action1.txt', 'Start.txt', 'Start.txt']

        for x in range(0, len(testing_funcs)):
            if arguments[x] is None:
                testing_funcs[x]()
            else:
                testing_funcs[x](arguments[x])
            compare('TestsHistory/' + comparisons[x])


if __name__ == '__main__':
    unittest.main()
