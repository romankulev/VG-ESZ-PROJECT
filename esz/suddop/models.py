from django.db import models


class Client(models.Model):
    name = models.CharField('Name',max_length=50)
    surname = models.CharField('Surname',max_length=50)
    patronymic = models.CharField('Patronymic',max_length=50)
    address = models.CharField('Address',max_length=100)


class Applicant(Client):
    phone = models.CharField('Phone',max_length=20)
    email = models.EmailField('Email')
    passportSeries = models.IntegerField('Passport series',max_length=4)
    passportNumber = models.IntegerField('Passport number',max_length=6)


class Student(Client):
    sex = models.CharField('Sex',max_length=15)
    dateOfBirth = models.DateField('Birth day')
    document = models.CharField('Document',max_length=25)
    snils = models.IntegerField('SNILS',max_length=15)


class Teacher(models.Model):
    name = models.CharField('Name',max_length=50)
    surname = models.CharField('Surname',max_length=50)
    patronymic = models.CharField('Patronymic',max_length=50)
    phone = models.CharField('Phone',max_length=20)


class Program(models.Model):
    name = models.CharField('Name',max_length=50)
    email = models.EmailField('Email')
    age = models.CharField('For age:',max_length=20)
    description = models.TextField('Program description', max_length=500)
    dateOfStart = models.DateField('Date of beginning')
    dateOfEnd = models.DateField('Date of ending')
    learningLevel = models.CharField('Learning level',max_length=25)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Contract(models.Model):
    dateOfConclusion = models.DateField('Date of conclusion')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)