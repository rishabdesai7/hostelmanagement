from django.db import models

'''
This file is used to generate models
'''


class hostel(models.Model):
    '''
    creates hostel db
    '''
    hostel_id = models.SmallIntegerField(primary_key=True)
    hostel_name = models.CharField(max_length=30)
    totalrooms = models.PositiveIntegerField()
    availablerooms = models.PositiveIntegerField()

    def __str__(self):
        '''
        :return: str
        '''
        return 'Name: {0}, Hostel Number : {1} , ' \
               'Total Rooms : {2} , Available Rooms : {3} '.format(self.hostel_name, self.hostel_id,
                                                                   self.totalrooms, self.availablerooms)

    class Meta:
        '''GENERATES META DATA'''
        db_table = 'hostel'


class users(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    user_type = models.CharField(max_length=10)
    hostel_no = models.IntegerField(null=True)
    room_no = models.IntegerField(null=True)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'id : {self.id} user_type : {self.user_type}'

    class Meta:
        db_table = "users"


class complaint(models.Model):
    s_id = models.PositiveIntegerField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'sender : {self.s_id}  complaint : {self.text}'

    class Meta:
        db_table = "complaint"

class applications(models.Model):
    app_id = models.AutoField(primary_key=True)
    student_id = models.SmallIntegerField()
    hostel_id = models.SmallIntegerField()
    room_id = models.SmallIntegerField()
    status = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f'id: {self.app_id} student_id:{self.student_id} \
                    hostel_id:{self.hostel_id} room_id:{self.room_id} status : {self.status}'

    class Meta:
        db_table = "applications"


class rooms(models.Model):
    room_id = models.SmallIntegerField(primary_key=True)
    hostel_no = models.SmallIntegerField()
    status = models.CharField(max_length=10, default="free")
    student_id = models.SmallIntegerField(default=-1)

    def __str__(self):
        return f'id: {self.room_id} hostel:{self.hostel_no} status:{self.status} student_id:{self.student_id}'

    class Meta:
        db_table = "rooms"


