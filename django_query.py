#we want to retrieve a single object for a Django model called Attendee with primary key = 7.

value = Attendee.objects.get(pk=7)
print(value)
