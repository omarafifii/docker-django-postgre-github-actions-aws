#!/usr/bin/env python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@admin.com', 'password')
