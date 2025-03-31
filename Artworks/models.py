from django.db import models
from django.conf import settings


class Artwork(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, 
                               on_delete=models.CASCADE, 
                               null=True, related_name='artworks')
    title = models.CharField(max_length=255)
    artwork_image = models.ImageField(upload_to='artworks/')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField(default=0000)
    media = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
    

# user's shopping cart


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart for {self.user.username}"


# artworks added to cart


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.artwork.title} (x{self.quantity})"
    
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    from_shop = models.CharField(max_length=20, default='Nairobi')
    to = models.CharField(max_length=20, default='Nairobi')
    phone_number = models.IntegerField(default=254)


class OrderItem(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    price = models.DecimalField(max_digits=10, decimal_places=2)