from django.db import models

class AccidentReport(models.Model):
  latitude = models.FloatField()
  longitude = models.FloatField()
  datetime = models.DateTimeField()

  police_force = models.CharField(max_length=100, blank=True, null=True)  # optional, auto-filled/admin
  weather_conditions = models.CharField(max_length=50)
  road_surface_conditions = models.CharField(max_length=50)
  light_conditions = models.CharField(max_length=50)

  number_of_vehicles = models.PositiveIntegerField()
  number_of_casualties = models.PositiveIntegerField()

  vehicle_types_involved = models.JSONField()  # store checkbox selection as JSON list

  severity_score = models.FloatField(blank=True, null=True)  # auto-calculated on save

  is_approved = models.BooleanField(default=False)  # optional, admin can approve

  def save(self, *args, **kwargs):
      self.severity_score = self.calculate_severity_score()
      super().save(*args, **kwargs)

  def calculate_severity_score(self):
      # Placeholder scoring logic (adjust as needed)
      return 2 * self.number_of_casualties + 0.5 * self.number_of_vehicles

  def __str__(self):
      return f"Report at ({self.latitude}, {self.longitude}) on {self.datetime}"
