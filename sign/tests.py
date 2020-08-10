from django.test import TestCase
# from sign.models import Event, Guest


# Create your tests here.
# class ModelTest(TestCase):
#     def setUp(self):
#         Event.objects.create(id=6, name="gaogao", status=True, limit=2000, address='shenzhen',
#                              start_time="2020-8-1 00:00:00")
#         Guest.objects.create(id=6, event_id=6, realname='alen', phone='13711001101', email='alen@163.com', sign=False)
#
#     def test_event(self):
#         result = Event.objects.get(name='gaogao')
#         self.assertEqual(result.address, 'shenzhen')
#         self.assertTrue(result.status)
#
#     def test_guest(self):
#         result = Guest.objects.get(phone='13711001101')
#         self.assertEqual(result.realname, 'alen')
#         self.assertTrue(result.sign)

# class IndexPageTest(TestCase):
#     '''测试登录首页'''
#     def test_index_page_renders_index_template(self):
#         '''测试index视图'''
#         response=self.client.get('http://127.0.0.1:8000/')
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(response,'index.html')