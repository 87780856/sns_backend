# Generated by Django 2.2.1 on 2019-05-28 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=4096, null=True, verbose_name='描述')),
                ('remark', models.CharField(blank=True, max_length=4096, null=True, verbose_name='备注')),
                ('sn', models.CharField(blank=True, max_length=256, null=True, verbose_name='排序号')),
                ('valid_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='有效标志')),
                ('created_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='创建人')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='修改人')),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('code', models.CharField(max_length=256, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='名称')),
                ('app_module', models.IntegerField(blank=True, null=True, verbose_name='应用模块')),
            ],
            options={
                'verbose_name': '应用实例',
            },
        ),
        migrations.CreateModel(
            name='BizParamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=4096, null=True, verbose_name='描述')),
                ('remark', models.CharField(blank=True, max_length=4096, null=True, verbose_name='备注')),
                ('sn', models.CharField(blank=True, max_length=256, null=True, verbose_name='排序号')),
                ('valid_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='有效标志')),
                ('created_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='创建人')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='修改人')),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('code', models.CharField(max_length=256, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '业务参数类型',
            },
        ),
        migrations.CreateModel(
            name='SysParamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=4096, null=True, verbose_name='描述')),
                ('remark', models.CharField(blank=True, max_length=4096, null=True, verbose_name='备注')),
                ('sn', models.CharField(blank=True, max_length=256, null=True, verbose_name='排序号')),
                ('valid_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='有效标志')),
                ('created_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='创建人')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='修改人')),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('code', models.CharField(max_length=256, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='名称')),
            ],
            options={
                'verbose_name': '系统参数类型',
            },
        ),
        migrations.CreateModel(
            name='SysParamValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=4096, null=True, verbose_name='描述')),
                ('remark', models.CharField(blank=True, max_length=4096, null=True, verbose_name='备注')),
                ('sn', models.CharField(blank=True, max_length=256, null=True, verbose_name='排序号')),
                ('valid_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='有效标志')),
                ('created_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='创建人')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='修改人')),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('code', models.CharField(max_length=256, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='名称')),
                ('param_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.SysParamType', verbose_name='系统参数值')),
            ],
            options={
                'verbose_name': '系统参数值',
            },
        ),
        migrations.CreateModel(
            name='BizParamValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=4096, null=True, verbose_name='描述')),
                ('remark', models.CharField(blank=True, max_length=4096, null=True, verbose_name='备注')),
                ('sn', models.CharField(blank=True, max_length=256, null=True, verbose_name='排序号')),
                ('valid_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='有效标志')),
                ('created_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='创建人')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified_man', models.CharField(blank=True, max_length=256, null=True, verbose_name='修改人')),
                ('modified_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('code', models.CharField(max_length=256, unique=True, verbose_name='编号')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='名称')),
                ('biz_module', models.IntegerField(blank=True, null=True, verbose_name='业务模块')),
                ('app_instance', models.IntegerField(blank=True, null=True, verbose_name='所属应用')),
                ('param_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='system.BizParamType', verbose_name='业务参数类型')),
            ],
            options={
                'verbose_name': '业务参数值',
            },
        ),
    ]