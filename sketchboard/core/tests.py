from django.test import TestCase
from .models import ConfigurationSet, Judgement, CustomUser

# Create your tests here.

class Test_Configuration_Set(TestCase):
    
    def setUp(self) -> None:
        
        user1 = CustomUser.objects.create(username="test_user_1", password="test1234")
        
        config_set1 = ConfigurationSet.objects.create(name="config1", config="{'color':'green'}")
        config_set2 = ConfigurationSet.objects.create(name="config2", config="{'color':'red'}")
        
        judgement1= Judgement.objects.create(user=user1, config_set=config_set1, rating=5)
        judgement2 = Judgement.objects.create(user=user1, config_set=config_set1, rating=5)
        judgement3 = Judgement.objects.create(user=user1, config_set=config_set1, rating=5)
        judgement4 = Judgement.objects.create(user=user1, config_set=config_set2, rating=2)
        judgement5 = Judgement.objects.create(user=user1, config_set=config_set2, rating=4)

    def test_create_judgement(self):
        user1 = CustomUser.objects.get(username="test_user_1")
        config_set1 = ConfigurationSet.objects.get(name="config1")
        judgement = config_set1.create_judgement(user1, 5)
        
        self.assertTrue(Judgement.objects.get(pk=judgement.pk) is not None)
        
    def test_get_average_rating(self):
        config_set1 = ConfigurationSet.objects.get(name="config1")
        config_set2 = ConfigurationSet.objects.get(name="config2")
        
        self.assertEqual(config_set1.get_average_rating(), 5)
        self.assertEqual(config_set2.get_average_rating(), 3)
        
    def test_get_all_attr(self):
        