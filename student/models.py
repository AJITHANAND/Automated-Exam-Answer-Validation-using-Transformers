from django.db import models


class Student(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=100)
    std_class = models.CharField(max_length=100)
    register_num = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.register_num:
            last_student = Student.objects.order_by('id').last()
            if last_student:
                last_register_num = last_student.register_num
                prefix, seq = last_register_num.split('MCA')
                seq_num = int(seq) + 1
                new_register_num = f'{prefix}MCA{seq_num:04d}'
            else:
                new_register_num = 'MCA2023001'
            self.register_num = new_register_num
        super().save(*args, **kwargs)


class Login(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)
    password = models.CharField(max_length=512,
                                default="d80cf102414d7d87b3073ea9b1ec4ef60a5b59bd5f10a66839f0351d9af1b9ccab08b726817956c6eec1355f97438271e6b42f4e155b7d36fbef23eb6097fc6c")
    register_num = models.CharField(max_length=100, unique=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)


class Answers(models.Model):
    answer = models.JSONField(default=list)
    mark = models.JSONField(default=list)
    is_processing = models.BooleanField(default=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question_code = models.CharField(max_length=100)

    def set_answer(self, index, value):
        answers = self.answer or [''] * 10
        answers[index] = value
        self.answer = answers

    def get_answer(self, index):
        return (self.answer or [''] * 10)[index]

    def set_mark(self, index, value):
        mark = self.mark or [''] * 10
        mark[index] = value
        self.answer = mark

    def get_mark(self, index):
        return (self.mark or [''] * 10)[index]
