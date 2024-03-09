from django.db import models


class Template(models.Model):
    """Модель шаблона."""
    tag = models.SlugField('Тэг', max_length=16, unique=True)
    title = models.CharField('Название', max_length=50)

    def fields(self):
        return TemplateField.objects.filter(template=self).order_by('tab')

    def __unicode__(self):
        return self.title

    def __str__(self) -> str:
        return self.title[:21]

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


class TemplateField(models.Model):
    """"""
    FieldTypes = (
        ('I', 'Integer'),
        ('T', 'Text'),
        ('B', 'Bool'),
        ('E', 'E-mail'),
        ('U', 'URL'),
        ('C', 'Choices'),
    )
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    tag = models.SlugField('Тэг', max_length=32)
    title = models.CharField('Название', max_length=50)
    type = models.CharField('Тип поля', max_length=1, choices=FieldTypes)
    tab = models.IntegerField('Очередность', default=0)
    required = models.BooleanField('Обязательно для заполнения', default=True)

    def __unicode__(self):
        return u'%s: %s' % (self.template, self.tag)

    def parameters(self):
        return FieldParameter.objects.filter(field=self).order_by('tab')

    def __str__(self) -> str:
        return self.tag[:21]

    class Meta:
        unique_together = ("template", "tag")
        verbose_name = 'Поле в шаблоне'
        verbose_name_plural = 'Поле в шаблоне'


class FieldParameter(models.Model):
    """"""
    field = models.ForeignKey(TemplateField, on_delete=models.CASCADE)
    tag = models.SlugField('Тэг', max_length=32)
    value = models.CharField('Значение', max_length=255)
    tab = models.IntegerField('Очередность', default=0)

    def __unicode__(self):
        return u'%s: %s = %s' % (self.field, self.tag, self.value)

    def __str__(self) -> str:
        return self.tag[:21]

    class Meta:
        unique_together = ("field", "tag", "value")
        verbose_name = 'Поле формы'
        verbose_name_plural = 'Поля формы'


class Record(models.Model):
    """"""
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    dt = models.DateTimeField('Дата и время')

    def __unicode__(self):
        return u'%s @ %s' % (self.template, self.dt)

    def __str__(self) -> str:
        return f'Запись от {self.dt}'[:21]

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class RecordData(models.Model):
    """"""
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    field = models.ForeignKey(TemplateField, on_delete=models.DO_NOTHING)
    value = models.CharField('Занчение', max_length=255)

    def __unicode__(self):
        return u'%s %s' % (self.record, self.field)

    class Meta:
        unique_together = ("record", "field")
        verbose_name = 'Заполненная форма'
        verbose_name_plural = 'Заполненные формы'
