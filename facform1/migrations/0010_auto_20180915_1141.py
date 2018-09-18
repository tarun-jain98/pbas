# Generated by Django 2.0.2 on 2018-09-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facform1', '0009_auto_20180915_0431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rd',
            old_name='c_index',
            new_name='book_m',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='c_date',
            new_name='c_c_date',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='c_name',
            new_name='c_c_index',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='c_place',
            new_name='c_c_name',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='c_title',
            new_name='c_c_place',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='j_index',
            new_name='c_c_title',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='j_date',
            new_name='c_j_date',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='j_issn',
            new_name='c_j_index',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='j_name',
            new_name='c_j_issn',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='j_title',
            new_name='c_j_name',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='j_page',
            new_name='c_j_page',
        ),
        migrations.RenameField(
            model_name='rd',
            old_name='j_volume',
            new_name='c_j_title',
        ),
        migrations.RenameField(
            model_name='remarks',
            old_name='tot_marks',
            new_name='total_marks',
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='e_l_f_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='e_l_r_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='e_o_f_r_final',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='e_t_f_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='e_t_r_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='o_l_f_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='o_l_r_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='o_t_f_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='o_t_r_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='feedbacktab',
            name='p_f_avg',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='c_j_volume',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='c_m',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_c_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_c_index',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_c_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_c_place',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_c_title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_j_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_j_index',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_j_issn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_j_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_j_page',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_j_title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='f_j_volume',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='j_m',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='onl_course_m',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='p_m',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='rd_tot_marks',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='rp_marks',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_c_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_c_index',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_c_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_c_place',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_c_title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_j_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_j_index',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_j_issn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_j_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_j_page',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_j_title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='s_j_volume',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='rd',
            name='w_m',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='hod_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='principal_status',
            field=models.BooleanField(default=False),
        ),
    ]