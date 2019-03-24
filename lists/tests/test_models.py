from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError

class ListAndItemModelsTest(TestCase):
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = "The first (ever) list item"
		first_item.list = list_
		first_item.save()


		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list, list_)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list, list_)

	def test_cannot_save_empty_list_items(self):
		list_ = List.objects.create()
		item = Item.objects.create(text="", list=list_)
		with self.assertRaises(ValidationError):
			item.save()
			item.full_clean()

	"""
	the context manager does the same as
	try:
		item.save()
		self.fail("the save should have raised an exception")
	except ValidationError:
		pass
	
	TextField left default, required is False, which means that
	the test should pass but it doesn't. Doesn't raise ValidationError
	because Django models don't run full validation on save. Any constrains
	made on the database will raise errors on save, but SQLite doesn't support
	enforcing emptiness constrains on text columns and so the save method is
	is letting this invalid value through silently.
	
	item.full_clean()
	A Method that manually runs validation
	"""


	def test_get_absolute_url(self):
		list_ = List.objects.create()
		self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')



		
