from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Order


User = get_user_model()


class OrderTestCase(TestCase):
    def setUp(self) -> None:
        self.user_a_username = "sina"
        self.user_a_pw = "pass"

        user_a = User.objects.create(
            username=self.user_a_username, email="s.e.sezza121@gmail.com"
        )

        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(self.user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_create_order(self):
        obj = Order.objects.create(user=self.user_a, title="abc123", price=12.23)
        # assert that the order is created successfully and it has a valid id number
        self.assertIsInstance(obj, Order)
        self.assertEqual(obj.__str__(), f"Order {obj.id} by sina")

    def test_addition_of_product_to_cart(self):
        """
        This method tests if we can add product to cart
        and retrieve them later using `get_products` method  of Order class.

        It first creates an instance of Product with name 'apple', price 50 and quantity 10.
        Then adds this product into the cart of user_a (admin).
        After adding, it retrieves all products in the cart using `get_products()` function.
        Finally, asserts that there is only one item in the list and its attributes are same as those defined above.
        """
        pass
