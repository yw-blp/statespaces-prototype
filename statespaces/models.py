from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # used for automatic password authentication only, customer_id copied to username
    customer_id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=1)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_initial}."

class Building(models.Model):
    building_id = models.BigAutoField(primary_key=True)
    building_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.building_name

class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    building_id = models.ForeignKey(
        Building,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employees'
    )
    manager_id = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Venue(models.Model):
    venue_id = models.BigAutoField(primary_key=True)
    venue_name = models.CharField(max_length=255)
    floor_area = models.IntegerField()
    venue_type = models.CharField(max_length=255)
    capacity = models.IntegerField()
    floor = models.IntegerField()
    in_use = models.BooleanField(default=False)
    fully_booked = models.BooleanField(default=False)
    building_id = models.ForeignKey(
        Building,
        on_delete=models.SET_NULL,
        null=False,
        related_name='venues'
    )

    def __str__(self):
        return self.venue_name

class Assignment(models.Model):
    assignment_id = models.BigAutoField(primary_key=True)
    date_of_assignment = models.DateField()
    venue_id = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        null=False,
        related_name='assignments'
    )
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=False,
        related_name='assignments'
    )

class Reservation(models.Model):
    reservation_id = models.BigAutoField(primary_key=True)
    participant_count = models.IntegerField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    venue_id = models.ForeignKey(
        Venue,
        on_delete=models.RESTRICT,
        null=False,
        related_name='reservations'
    )
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.RESTRICT,
        null=False,
        related_name='reservations'
    )

class Amenity(models.Model):
    amenity_id = models.BigAutoField(primary_key=True)
    amenity_type = models.CharField(max_length=255)
    amenity_description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    venue_id = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        null=False,
        related_name='amenities'
    )

class Renovation(models.Model):
    venue_id = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        null=False,
        related_name='renovations'
    )
    start_date = models.DateField()
    pk = models.CompositePrimaryKey('venue_id', 'start_date')
    status = models.CharField(max_length=255, default='Planned')
    renovation_description = models.CharField(max_length=255)
    end_date = models.DateField()