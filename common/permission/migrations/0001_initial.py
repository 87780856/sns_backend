# Generated by Django 2.2.1 on 2019-05-28 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlObject',
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
                ('control_object_type', models.IntegerField(blank=True, null=True, verbose_name='控制对象类型')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_set', to='permission.ControlObject')),
            ],
            options={
                'verbose_name': '控制对象',
            },
        ),
        migrations.CreateModel(
            name='Role',
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
                ('role_type', models.IntegerField(blank=True, null=True, verbose_name='角色类型')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name': '角色',
            },
        ),
        migrations.CreateModel(
            name='ControlPolicy',
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
                ('control_policy_type', models.IntegerField(blank=True, null=True, verbose_name='控制策略类型')),
                ('control_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='permission.ControlObject', verbose_name='控制对象')),
                ('permission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Permission')),
            ],
            options={
                'verbose_name': '控制策略',
            },
        ),
        migrations.CreateModel(
            name='Account',
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
                ('account_type', models.IntegerField(blank=True, null=True, verbose_name='账号类型')),
                ('member', models.IntegerField(blank=True, null=True, verbose_name='会员')),
                ('head_img', models.CharField(blank=True, max_length=4096, null=True, verbose_name='头像')),
                ('email_binding_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='邮箱绑定标志')),
                ('phone_number', models.CharField(blank=True, max_length=256, null=True, verbose_name='手机号')),
                ('phone_binding_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='手机号绑定标志')),
                ('qq_openid', models.CharField(blank=True, max_length=4096, null=True, verbose_name='QQopenid')),
                ('qq_binding_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='QQ绑定标志')),
                ('wechat_openid', models.CharField(blank=True, max_length=4096, null=True, verbose_name='微信openid')),
                ('wechat_binding_flag', models.CharField(blank=True, choices=[('Y', '是'), ('N', '否')], max_length=256, null=True, verbose_name='微信绑定标志')),
                ('current_login_ip', models.CharField(blank=True, max_length=256, null=True, verbose_name='当前登录IP')),
                ('current_login_type', models.CharField(blank=True, max_length=256, null=True, verbose_name='当前登录类型')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '账号',
            },
        ),
    ]
