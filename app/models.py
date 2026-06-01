from django.db import models


# =========================
# PERSON MODEL
# =========================
class Person(models.Model):

    # Basic Information
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)

    # Personal Details
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)

    # Contact Information
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    # Address Information
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # Extra Information
    occupation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    # Profile Image
    image = models.ImageField(upload_to='person_images/', null=True, blank=True)

    # Status
    is_active = models.BooleanField(default=True)

    # Date and Time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



# =========================
# AADHAR CARD MODEL
# =========================
class Adharcard(models.Model):

    # One To One Relation
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE
    )

    # Aadhaar Details
    adharno = models.CharField(
        max_length=12,
        unique=True
    )

    # Card Details
    card_color = models.CharField(max_length=50)
    issue_place = models.CharField(max_length=100)

    # Address
    address = models.TextField()

    # Verification
    is_verified = models.BooleanField(default=False)

    # Upload Documents
    document = models.FileField(
        upload_to='documents/',
        null=True,
        blank=True
    )

    # QR Code Image
    qr_image = models.ImageField(
        upload_to='qr_images/',
        null=True,
        blank=True
    )

    # Timestamps
    issue_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.adharno