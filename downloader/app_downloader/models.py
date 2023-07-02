from django.db import models


class DbDownload(models.Model):
    object_name = models.CharField(max_length=255, verbose_name = "Наименование объекта")
    equipment_name = models.CharField(max_length=255, verbose_name = "Наименование оборудования")
    file_name = models.CharField(max_length=255, null=True, blank=True )
    version = models.IntegerField( null=True, blank=True)
    file = models.FileField(upload_to='documents', max_length=100, blank=True, verbose_name = "Файл")
    ip = models.CharField(max_length=255, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.object_name

class AchrAlarms(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACHR_Alarms'


class AchrInf(models.Model):
    object_name = models.TextField(db_column='Object_Name', blank=True, null=True)  # Field name made lowercase.
    create_day = models.IntegerField(db_column='Create_Day', blank=True, null=True)  # Field name made lowercase.
    create_month = models.IntegerField(db_column='Create_Month', blank=True, null=True)  # Field name made lowercase.
    create_year = models.IntegerField(db_column='Create_Year', blank=True, null=True)  # Field name made lowercase.
    start_day = models.IntegerField(db_column='Start_Day', blank=True, null=True)  # Field name made lowercase.
    start_month = models.IntegerField(db_column='Start_Month', blank=True, null=True)  # Field name made lowercase.
    start_year = models.IntegerField(db_column='Start_Year', blank=True, null=True)  # Field name made lowercase.
    comp_name = models.TextField(db_column='Comp_Name', blank=True, null=True)  # Field name made lowercase.
    tel_number = models.TextField(db_column='Tel_Number', blank=True, null=True)  # Field name made lowercase.
    delaym = models.IntegerField(db_column='delayM', blank=True, null=True)  # Field name made lowercase.
    delaynw = models.IntegerField(db_column='delayNw', blank=True, null=True)  # Field name made lowercase.
    delayna = models.IntegerField(db_column='delayNa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACHR_Inf'


class AlarmsRele(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alarms_Rele'


class Confighydra(models.Model):
    create_day = models.IntegerField(db_column='Create_Day', blank=True, null=True)  # Field name made lowercase.
    create_month = models.IntegerField(db_column='Create_Month', blank=True, null=True)  # Field name made lowercase.
    create_year = models.IntegerField(db_column='Create_Year', blank=True, null=True)  # Field name made lowercase.
    start_day = models.IntegerField(db_column='Start_Day', blank=True, null=True)  # Field name made lowercase.
    start_month = models.IntegerField(db_column='Start_Month', blank=True, null=True)  # Field name made lowercase.
    start_year = models.IntegerField(db_column='Start_Year', blank=True, null=True)  # Field name made lowercase.
    comp_name = models.TextField(db_column='Comp_Name', blank=True, null=True)  # Field name made lowercase.
    tel_number = models.TextField(db_column='Tel_Number', blank=True, null=True)  # Field name made lowercase.
    h2_conc_w = models.FloatField(db_column='H2_Conc_W', blank=True, null=True)  # Field name made lowercase.
    relh2o_conc_w = models.FloatField(db_column='RelH2O_Conc_W', blank=True, null=True)  # Field name made lowercase.
    h2_conc_a = models.FloatField(db_column='H2_Conc_A', blank=True, null=True)  # Field name made lowercase.
    relh2o_conc_a = models.FloatField(db_column='RelH2O_Conc_A', blank=True, null=True)  # Field name made lowercase.
    h2o_conc_w = models.FloatField(db_column='H2O_Conc_W', blank=True, null=True)  # Field name made lowercase.
    h2o_conc_a = models.FloatField(db_column='H2O_Conc_A', blank=True, null=True)  # Field name made lowercase.
    h2_grd_w = models.FloatField(db_column='H2_GrD_W', blank=True, null=True)  # Field name made lowercase.
    h2_grw_w = models.FloatField(db_column='H2_GrW_W', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfigHydra'


class Configpvt(models.Model):
    object_name = models.TextField(db_column='Object_Name', blank=True, null=True)  # Field name made lowercase.
    ser_number = models.TextField(db_column='Ser_Number', blank=True, null=True)  # Field name made lowercase.
    create_day = models.IntegerField(db_column='Create_Day', blank=True, null=True)  # Field name made lowercase.
    create_month = models.IntegerField(db_column='Create_Month', blank=True, null=True)  # Field name made lowercase.
    create_year = models.IntegerField(db_column='Create_Year', blank=True, null=True)  # Field name made lowercase.
    start_day = models.IntegerField(db_column='Start_Day', blank=True, null=True)  # Field name made lowercase.
    start_month = models.IntegerField(db_column='Start_Month', blank=True, null=True)  # Field name made lowercase.
    start_year = models.IntegerField(db_column='Start_Year', blank=True, null=True)  # Field name made lowercase.
    comp_name = models.TextField(db_column='Comp_Name', blank=True, null=True)  # Field name made lowercase.
    tel_number = models.TextField(db_column='Tel_Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfigPVT'


class Configrpn(models.Model):
    object_name = models.TextField(db_column='Object_Name', blank=True, null=True)  # Field name made lowercase.
    ser_number = models.TextField(db_column='Ser_Number', blank=True, null=True)  # Field name made lowercase.
    create_day = models.IntegerField(db_column='Create_Day', blank=True, null=True)  # Field name made lowercase.
    create_month = models.IntegerField(db_column='Create_Month', blank=True, null=True)  # Field name made lowercase.
    create_year = models.IntegerField(db_column='Create_Year', blank=True, null=True)  # Field name made lowercase.
    start_day = models.IntegerField(db_column='Start_Day', blank=True, null=True)  # Field name made lowercase.
    start_month = models.IntegerField(db_column='Start_Month', blank=True, null=True)  # Field name made lowercase.
    start_year = models.IntegerField(db_column='Start_Year', blank=True, null=True)  # Field name made lowercase.
    comp_name = models.TextField(db_column='Comp_Name', blank=True, null=True)  # Field name made lowercase.
    tel_number = models.TextField(db_column='Tel_Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfigRPN'


class Corestart(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(blank=True, null=True)
    quality_message = models.IntegerField(db_column='Quality_message', blank=True, null=True)  # Field name made lowercase.
    core_start_time = models.TextField(blank=True, null=True)
    quality_core_start_time = models.IntegerField(db_column='Quality_core_start_time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CoreStart'


class Dopbushmlong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    phi_next1 = models.FloatField(db_column='Phi_next1', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next1 = models.IntegerField(db_column='Quality_Phi_next1', blank=True, null=True)  # Field name made lowercase.
    phi_next2 = models.FloatField(db_column='Phi_next2', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next2 = models.IntegerField(db_column='Quality_Phi_next2', blank=True, null=True)  # Field name made lowercase.
    phi_next3 = models.FloatField(db_column='Phi_next3', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next3 = models.IntegerField(db_column='Quality_Phi_next3', blank=True, null=True)  # Field name made lowercase.
    phi_next4 = models.FloatField(db_column='Phi_next4', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next4 = models.IntegerField(db_column='Quality_Phi_next4', blank=True, null=True)  # Field name made lowercase.
    phi_next5 = models.FloatField(db_column='Phi_next5', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next5 = models.IntegerField(db_column='Quality_Phi_next5', blank=True, null=True)  # Field name made lowercase.
    u0 = models.FloatField(db_column='U0', blank=True, null=True)  # Field name made lowercase.
    quality_u0 = models.IntegerField(db_column='Quality_U0', blank=True, null=True)  # Field name made lowercase.
    u1 = models.FloatField(db_column='U1', blank=True, null=True)  # Field name made lowercase.
    quality_u1 = models.IntegerField(db_column='Quality_U1', blank=True, null=True)  # Field name made lowercase.
    u2 = models.FloatField(db_column='U2', blank=True, null=True)  # Field name made lowercase.
    quality_u2 = models.IntegerField(db_column='Quality_U2', blank=True, null=True)  # Field name made lowercase.
    kuu0 = models.FloatField(db_column='KuU0', blank=True, null=True)  # Field name made lowercase.
    quality_kuu0 = models.IntegerField(db_column='Quality_KuU0', blank=True, null=True)  # Field name made lowercase.
    kuu2 = models.FloatField(db_column='KuU2', blank=True, null=True)  # Field name made lowercase.
    quality_kuu2 = models.IntegerField(db_column='Quality_KuU2', blank=True, null=True)  # Field name made lowercase.
    i0 = models.FloatField(db_column='I0', blank=True, null=True)  # Field name made lowercase.
    quality_i0 = models.IntegerField(db_column='Quality_I0', blank=True, null=True)  # Field name made lowercase.
    i1 = models.FloatField(db_column='I1', blank=True, null=True)  # Field name made lowercase.
    quality_i1 = models.IntegerField(db_column='Quality_I1', blank=True, null=True)  # Field name made lowercase.
    i2 = models.FloatField(db_column='I2', blank=True, null=True)  # Field name made lowercase.
    quality_i2 = models.IntegerField(db_column='Quality_I2', blank=True, null=True)  # Field name made lowercase.
    kui0 = models.FloatField(db_column='KuI0', blank=True, null=True)  # Field name made lowercase.
    quality_kui0 = models.IntegerField(db_column='Quality_KuI0', blank=True, null=True)  # Field name made lowercase.
    kui2 = models.FloatField(db_column='KuI2', blank=True, null=True)  # Field name made lowercase.
    quality_kui2 = models.IntegerField(db_column='Quality_KuI2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DopBushMLong'


class Dopbushmshort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    phi_next1 = models.FloatField(db_column='Phi_next1', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next1 = models.IntegerField(db_column='Quality_Phi_next1', blank=True, null=True)  # Field name made lowercase.
    phi_next2 = models.FloatField(db_column='Phi_next2', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next2 = models.IntegerField(db_column='Quality_Phi_next2', blank=True, null=True)  # Field name made lowercase.
    phi_next3 = models.FloatField(db_column='Phi_next3', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next3 = models.IntegerField(db_column='Quality_Phi_next3', blank=True, null=True)  # Field name made lowercase.
    phi_next4 = models.FloatField(db_column='Phi_next4', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next4 = models.IntegerField(db_column='Quality_Phi_next4', blank=True, null=True)  # Field name made lowercase.
    phi_next5 = models.FloatField(db_column='Phi_next5', blank=True, null=True)  # Field name made lowercase.
    quality_phi_next5 = models.IntegerField(db_column='Quality_Phi_next5', blank=True, null=True)  # Field name made lowercase.
    u0 = models.FloatField(db_column='U0', blank=True, null=True)  # Field name made lowercase.
    quality_u0 = models.IntegerField(db_column='Quality_U0', blank=True, null=True)  # Field name made lowercase.
    u1 = models.FloatField(db_column='U1', blank=True, null=True)  # Field name made lowercase.
    quality_u1 = models.IntegerField(db_column='Quality_U1', blank=True, null=True)  # Field name made lowercase.
    u2 = models.FloatField(db_column='U2', blank=True, null=True)  # Field name made lowercase.
    quality_u2 = models.IntegerField(db_column='Quality_U2', blank=True, null=True)  # Field name made lowercase.
    kuu0 = models.FloatField(db_column='KuU0', blank=True, null=True)  # Field name made lowercase.
    quality_kuu0 = models.IntegerField(db_column='Quality_KuU0', blank=True, null=True)  # Field name made lowercase.
    kuu2 = models.FloatField(db_column='KuU2', blank=True, null=True)  # Field name made lowercase.
    quality_kuu2 = models.IntegerField(db_column='Quality_KuU2', blank=True, null=True)  # Field name made lowercase.
    i0 = models.FloatField(db_column='I0', blank=True, null=True)  # Field name made lowercase.
    quality_i0 = models.IntegerField(db_column='Quality_I0', blank=True, null=True)  # Field name made lowercase.
    i1 = models.FloatField(db_column='I1', blank=True, null=True)  # Field name made lowercase.
    quality_i1 = models.IntegerField(db_column='Quality_I1', blank=True, null=True)  # Field name made lowercase.
    i2 = models.FloatField(db_column='I2', blank=True, null=True)  # Field name made lowercase.
    quality_i2 = models.IntegerField(db_column='Quality_I2', blank=True, null=True)  # Field name made lowercase.
    kui0 = models.FloatField(db_column='KuI0', blank=True, null=True)  # Field name made lowercase.
    quality_kui0 = models.IntegerField(db_column='Quality_KuI0', blank=True, null=True)  # Field name made lowercase.
    kui2 = models.FloatField(db_column='KuI2', blank=True, null=True)  # Field name made lowercase.
    quality_kui2 = models.IntegerField(db_column='Quality_KuI2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DopBushMShort'


class EnergParamLong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    a_u_vn = models.FloatField(db_column='A_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_a_u_vn = models.IntegerField(db_column='Quality_A_U_VN', blank=True, null=True)  # Field name made lowercase.
    b_u_vn = models.FloatField(db_column='B_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_b_u_vn = models.IntegerField(db_column='Quality_B_U_VN', blank=True, null=True)  # Field name made lowercase.
    c_u_vn = models.FloatField(db_column='C_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_c_u_vn = models.IntegerField(db_column='Quality_C_U_VN', blank=True, null=True)  # Field name made lowercase.
    ab_u_vn = models.FloatField(db_column='AB_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_ab_u_vn = models.IntegerField(db_column='Quality_AB_U_VN', blank=True, null=True)  # Field name made lowercase.
    bc_u_vn = models.FloatField(db_column='BC_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_bc_u_vn = models.IntegerField(db_column='Quality_BC_U_VN', blank=True, null=True)  # Field name made lowercase.
    ca_u_vn = models.FloatField(db_column='CA_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_ca_u_vn = models.IntegerField(db_column='Quality_CA_U_VN', blank=True, null=True)  # Field name made lowercase.
    a_i_vn = models.FloatField(db_column='A_I_VN', blank=True, null=True)  # Field name made lowercase.
    quality_a_i_vn = models.IntegerField(db_column='Quality_A_I_VN', blank=True, null=True)  # Field name made lowercase.
    b_i_vn = models.FloatField(db_column='B_I_VN', blank=True, null=True)  # Field name made lowercase.
    quality_b_i_vn = models.IntegerField(db_column='Quality_B_I_VN', blank=True, null=True)  # Field name made lowercase.
    c_i_vn = models.FloatField(db_column='C_I_VN', blank=True, null=True)  # Field name made lowercase.
    quality_c_i_vn = models.IntegerField(db_column='Quality_C_I_VN', blank=True, null=True)  # Field name made lowercase.
    a_u_nn1 = models.FloatField(db_column='A_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_a_u_nn1 = models.IntegerField(db_column='Quality_A_U_NN1', blank=True, null=True)  # Field name made lowercase.
    b_u_nn1 = models.FloatField(db_column='B_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_b_u_nn1 = models.IntegerField(db_column='Quality_B_U_NN1', blank=True, null=True)  # Field name made lowercase.
    c_u_nn1 = models.FloatField(db_column='C_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_c_u_nn1 = models.IntegerField(db_column='Quality_C_U_NN1', blank=True, null=True)  # Field name made lowercase.
    ab_u_nn1 = models.FloatField(db_column='AB_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_ab_u_nn1 = models.IntegerField(db_column='Quality_AB_U_NN1', blank=True, null=True)  # Field name made lowercase.
    bc_u_nn1 = models.FloatField(db_column='BC_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_bc_u_nn1 = models.IntegerField(db_column='Quality_BC_U_NN1', blank=True, null=True)  # Field name made lowercase.
    ca_u_nn1 = models.FloatField(db_column='CA_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_ca_u_nn1 = models.IntegerField(db_column='Quality_CA_U_NN1', blank=True, null=True)  # Field name made lowercase.
    a_i_nn1 = models.FloatField(db_column='A_I_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_a_i_nn1 = models.IntegerField(db_column='Quality_A_I_NN1', blank=True, null=True)  # Field name made lowercase.
    b_i_nn1 = models.FloatField(db_column='B_I_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_b_i_nn1 = models.IntegerField(db_column='Quality_B_I_NN1', blank=True, null=True)  # Field name made lowercase.
    c_i_nn1 = models.FloatField(db_column='C_I_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_c_i_nn1 = models.IntegerField(db_column='Quality_C_I_NN1', blank=True, null=True)  # Field name made lowercase.
    a_u_nn2 = models.FloatField(db_column='A_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_a_u_nn2 = models.IntegerField(db_column='Quality_A_U_NN2', blank=True, null=True)  # Field name made lowercase.
    b_u_nn2 = models.FloatField(db_column='B_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_b_u_nn2 = models.IntegerField(db_column='Quality_B_U_NN2', blank=True, null=True)  # Field name made lowercase.
    c_u_nn2 = models.FloatField(db_column='C_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_c_u_nn2 = models.IntegerField(db_column='Quality_C_U_NN2', blank=True, null=True)  # Field name made lowercase.
    ab_u_nn2 = models.FloatField(db_column='AB_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_ab_u_nn2 = models.IntegerField(db_column='Quality_AB_U_NN2', blank=True, null=True)  # Field name made lowercase.
    bc_u_nn2 = models.FloatField(db_column='BC_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_bc_u_nn2 = models.IntegerField(db_column='Quality_BC_U_NN2', blank=True, null=True)  # Field name made lowercase.
    ca_u_nn2 = models.FloatField(db_column='CA_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_ca_u_nn2 = models.IntegerField(db_column='Quality_CA_U_NN2', blank=True, null=True)  # Field name made lowercase.
    a_i_nn2 = models.FloatField(db_column='A_I_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_a_i_nn2 = models.IntegerField(db_column='Quality_A_I_NN2', blank=True, null=True)  # Field name made lowercase.
    b_i_nn2 = models.FloatField(db_column='B_I_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_b_i_nn2 = models.IntegerField(db_column='Quality_B_I_NN2', blank=True, null=True)  # Field name made lowercase.
    c_i_nn2 = models.FloatField(db_column='C_I_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_c_i_nn2 = models.IntegerField(db_column='Quality_C_I_NN2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Energ_param_long'


class EnergParamShort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    a_u_vn = models.FloatField(db_column='A_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_a_u_vn = models.IntegerField(db_column='Quality_A_U_VN', blank=True, null=True)  # Field name made lowercase.
    b_u_vn = models.FloatField(db_column='B_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_b_u_vn = models.IntegerField(db_column='Quality_B_U_VN', blank=True, null=True)  # Field name made lowercase.
    c_u_vn = models.FloatField(db_column='C_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_c_u_vn = models.IntegerField(db_column='Quality_C_U_VN', blank=True, null=True)  # Field name made lowercase.
    ab_u_vn = models.FloatField(db_column='AB_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_ab_u_vn = models.IntegerField(db_column='Quality_AB_U_VN', blank=True, null=True)  # Field name made lowercase.
    bc_u_vn = models.FloatField(db_column='BC_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_bc_u_vn = models.IntegerField(db_column='Quality_BC_U_VN', blank=True, null=True)  # Field name made lowercase.
    ca_u_vn = models.FloatField(db_column='CA_U_VN', blank=True, null=True)  # Field name made lowercase.
    quality_ca_u_vn = models.IntegerField(db_column='Quality_CA_U_VN', blank=True, null=True)  # Field name made lowercase.
    a_i_vn = models.FloatField(db_column='A_I_VN', blank=True, null=True)  # Field name made lowercase.
    quality_a_i_vn = models.IntegerField(db_column='Quality_A_I_VN', blank=True, null=True)  # Field name made lowercase.
    b_i_vn = models.FloatField(db_column='B_I_VN', blank=True, null=True)  # Field name made lowercase.
    quality_b_i_vn = models.IntegerField(db_column='Quality_B_I_VN', blank=True, null=True)  # Field name made lowercase.
    c_i_vn = models.FloatField(db_column='C_I_VN', blank=True, null=True)  # Field name made lowercase.
    quality_c_i_vn = models.IntegerField(db_column='Quality_C_I_VN', blank=True, null=True)  # Field name made lowercase.
    a_u_nn1 = models.FloatField(db_column='A_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_a_u_nn1 = models.IntegerField(db_column='Quality_A_U_NN1', blank=True, null=True)  # Field name made lowercase.
    b_u_nn1 = models.FloatField(db_column='B_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_b_u_nn1 = models.IntegerField(db_column='Quality_B_U_NN1', blank=True, null=True)  # Field name made lowercase.
    c_u_nn1 = models.FloatField(db_column='C_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_c_u_nn1 = models.IntegerField(db_column='Quality_C_U_NN1', blank=True, null=True)  # Field name made lowercase.
    ab_u_nn1 = models.FloatField(db_column='AB_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_ab_u_nn1 = models.IntegerField(db_column='Quality_AB_U_NN1', blank=True, null=True)  # Field name made lowercase.
    bc_u_nn1 = models.FloatField(db_column='BC_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_bc_u_nn1 = models.IntegerField(db_column='Quality_BC_U_NN1', blank=True, null=True)  # Field name made lowercase.
    ca_u_nn1 = models.FloatField(db_column='CA_U_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_ca_u_nn1 = models.IntegerField(db_column='Quality_CA_U_NN1', blank=True, null=True)  # Field name made lowercase.
    a_i_nn1 = models.FloatField(db_column='A_I_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_a_i_nn1 = models.IntegerField(db_column='Quality_A_I_NN1', blank=True, null=True)  # Field name made lowercase.
    b_i_nn1 = models.FloatField(db_column='B_I_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_b_i_nn1 = models.IntegerField(db_column='Quality_B_I_NN1', blank=True, null=True)  # Field name made lowercase.
    c_i_nn1 = models.FloatField(db_column='C_I_NN1', blank=True, null=True)  # Field name made lowercase.
    quality_c_i_nn1 = models.IntegerField(db_column='Quality_C_I_NN1', blank=True, null=True)  # Field name made lowercase.
    a_u_nn2 = models.FloatField(db_column='A_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_a_u_nn2 = models.IntegerField(db_column='Quality_A_U_NN2', blank=True, null=True)  # Field name made lowercase.
    b_u_nn2 = models.FloatField(db_column='B_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_b_u_nn2 = models.IntegerField(db_column='Quality_B_U_NN2', blank=True, null=True)  # Field name made lowercase.
    c_u_nn2 = models.FloatField(db_column='C_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_c_u_nn2 = models.IntegerField(db_column='Quality_C_U_NN2', blank=True, null=True)  # Field name made lowercase.
    ab_u_nn2 = models.FloatField(db_column='AB_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_ab_u_nn2 = models.IntegerField(db_column='Quality_AB_U_NN2', blank=True, null=True)  # Field name made lowercase.
    bc_u_nn2 = models.FloatField(db_column='BC_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_bc_u_nn2 = models.IntegerField(db_column='Quality_BC_U_NN2', blank=True, null=True)  # Field name made lowercase.
    ca_u_nn2 = models.FloatField(db_column='CA_U_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_ca_u_nn2 = models.IntegerField(db_column='Quality_CA_U_NN2', blank=True, null=True)  # Field name made lowercase.
    a_i_nn2 = models.FloatField(db_column='A_I_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_a_i_nn2 = models.IntegerField(db_column='Quality_A_I_NN2', blank=True, null=True)  # Field name made lowercase.
    b_i_nn2 = models.FloatField(db_column='B_I_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_b_i_nn2 = models.IntegerField(db_column='Quality_B_I_NN2', blank=True, null=True)  # Field name made lowercase.
    c_i_nn2 = models.FloatField(db_column='C_I_NN2', blank=True, null=True)  # Field name made lowercase.
    quality_c_i_nn2 = models.IntegerField(db_column='Quality_C_I_NN2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Energ_param_short'


class Eventsavtuk(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsAVTUK'


class Eventsbushm(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsBushM'


class Eventshydra(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsHydra'


class Eventsmodel(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsModel'


class EventsovervoltVn(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsOverVolt_VN'


class Eventspvt(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsPVT'


class Eventsrpn(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsRPN'


class Eventsrejim(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsRejim'


class Eventsvibr(models.Model):
    identifier = models.IntegerField(db_column='Identifier', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventsVibr'


class Hydralong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    h2 = models.FloatField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    quality_h2 = models.IntegerField(db_column='Quality_H2', blank=True, null=True)  # Field name made lowercase.
    relh2o = models.FloatField(db_column='RelH2O', blank=True, null=True)  # Field name made lowercase.
    quality_relh2o = models.IntegerField(db_column='Quality_RelH2O', blank=True, null=True)  # Field name made lowercase.
    h2o = models.FloatField(db_column='H2O', blank=True, null=True)  # Field name made lowercase.
    quality_h2o = models.IntegerField(db_column='Quality_H2O', blank=True, null=True)  # Field name made lowercase.
    h2_grd = models.FloatField(db_column='H2_GrD', blank=True, null=True)  # Field name made lowercase.
    quality_h2_grd = models.IntegerField(db_column='Quality_H2_GrD', blank=True, null=True)  # Field name made lowercase.
    h2_grw = models.FloatField(db_column='H2_GrW', blank=True, null=True)  # Field name made lowercase.
    quality_h2_grw = models.IntegerField(db_column='Quality_H2_GrW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HydraLong'


class Hydrashort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    h2 = models.FloatField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    quality_h2 = models.IntegerField(db_column='Quality_H2', blank=True, null=True)  # Field name made lowercase.
    relh2o = models.FloatField(db_column='RelH2O', blank=True, null=True)  # Field name made lowercase.
    quality_relh2o = models.IntegerField(db_column='Quality_RelH2O', blank=True, null=True)  # Field name made lowercase.
    h2o = models.FloatField(db_column='H2O', blank=True, null=True)  # Field name made lowercase.
    quality_h2o = models.IntegerField(db_column='Quality_H2O', blank=True, null=True)  # Field name made lowercase.
    h2_grd = models.FloatField(db_column='H2_GrD', blank=True, null=True)  # Field name made lowercase.
    quality_h2_grd = models.IntegerField(db_column='Quality_H2_GrD', blank=True, null=True)  # Field name made lowercase.
    h2_grw = models.FloatField(db_column='H2_GrW', blank=True, null=True)  # Field name made lowercase.
    quality_h2_grw = models.IntegerField(db_column='Quality_H2_GrW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HydraShort'


class Hydravibrlong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    level = models.FloatField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    quality_level = models.IntegerField(db_column='Quality_Level', blank=True, null=True)  # Field name made lowercase.
    vibra = models.FloatField(db_column='VibrA', blank=True, null=True)  # Field name made lowercase.
    quality_vibra = models.IntegerField(db_column='Quality_VibrA', blank=True, null=True)  # Field name made lowercase.
    vibrv = models.FloatField(db_column='VibrV', blank=True, null=True)  # Field name made lowercase.
    quality_vibrv = models.IntegerField(db_column='Quality_VibrV', blank=True, null=True)  # Field name made lowercase.
    vibrs = models.FloatField(db_column='VibrS', blank=True, null=True)  # Field name made lowercase.
    quality_vibrs = models.IntegerField(db_column='Quality_VibrS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HydraVibrLong'


class Hydravibrshort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    level = models.FloatField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    quality_level = models.IntegerField(db_column='Quality_Level', blank=True, null=True)  # Field name made lowercase.
    vibra = models.FloatField(db_column='VibrA', blank=True, null=True)  # Field name made lowercase.
    quality_vibra = models.IntegerField(db_column='Quality_VibrA', blank=True, null=True)  # Field name made lowercase.
    vibrv = models.FloatField(db_column='VibrV', blank=True, null=True)  # Field name made lowercase.
    quality_vibrv = models.IntegerField(db_column='Quality_VibrV', blank=True, null=True)  # Field name made lowercase.
    vibrs = models.FloatField(db_column='VibrS', blank=True, null=True)  # Field name made lowercase.
    quality_vibrs = models.IntegerField(db_column='Quality_VibrS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HydraVibrShort'


class Mainbushmlong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    ua = models.FloatField(db_column='UA', blank=True, null=True)  # Field name made lowercase.
    quality_ua = models.IntegerField(db_column='Quality_UA', blank=True, null=True)  # Field name made lowercase.
    ub = models.FloatField(db_column='UB', blank=True, null=True)  # Field name made lowercase.
    quality_ub = models.IntegerField(db_column='Quality_UB', blank=True, null=True)  # Field name made lowercase.
    uc = models.FloatField(db_column='UC', blank=True, null=True)  # Field name made lowercase.
    quality_uc = models.IntegerField(db_column='Quality_UC', blank=True, null=True)  # Field name made lowercase.
    ia = models.FloatField(db_column='IA', blank=True, null=True)  # Field name made lowercase.
    quality_ia = models.IntegerField(db_column='Quality_IA', blank=True, null=True)  # Field name made lowercase.
    ib = models.FloatField(db_column='IB', blank=True, null=True)  # Field name made lowercase.
    quality_ib = models.IntegerField(db_column='Quality_IB', blank=True, null=True)  # Field name made lowercase.
    ic = models.FloatField(db_column='IC', blank=True, null=True)  # Field name made lowercase.
    quality_ic = models.IntegerField(db_column='Quality_IC', blank=True, null=True)  # Field name made lowercase.
    tga = models.FloatField(db_column='TgA', blank=True, null=True)  # Field name made lowercase.
    quality_tga = models.IntegerField(db_column='Quality_TgA', blank=True, null=True)  # Field name made lowercase.
    tgb = models.FloatField(db_column='TgB', blank=True, null=True)  # Field name made lowercase.
    quality_tgb = models.IntegerField(db_column='Quality_TgB', blank=True, null=True)  # Field name made lowercase.
    tgc = models.FloatField(db_column='TgC', blank=True, null=True)  # Field name made lowercase.
    quality_tgc = models.IntegerField(db_column='Quality_TgC', blank=True, null=True)  # Field name made lowercase.
    ca = models.FloatField(db_column='CA', blank=True, null=True)  # Field name made lowercase.
    quality_ca = models.IntegerField(db_column='Quality_CA', blank=True, null=True)  # Field name made lowercase.
    cb = models.FloatField(db_column='CB', blank=True, null=True)  # Field name made lowercase.
    quality_cb = models.IntegerField(db_column='Quality_CB', blank=True, null=True)  # Field name made lowercase.
    cc = models.FloatField(db_column='CC', blank=True, null=True)  # Field name made lowercase.
    quality_cc = models.IntegerField(db_column='Quality_CC', blank=True, null=True)  # Field name made lowercase.
    dta = models.FloatField(db_column='dTA', blank=True, null=True)  # Field name made lowercase.
    quality_dta = models.IntegerField(db_column='Quality_dTA', blank=True, null=True)  # Field name made lowercase.
    dtb = models.FloatField(db_column='dTB', blank=True, null=True)  # Field name made lowercase.
    quality_dtb = models.IntegerField(db_column='Quality_dTB', blank=True, null=True)  # Field name made lowercase.
    dtc = models.FloatField(db_column='dTC', blank=True, null=True)  # Field name made lowercase.
    quality_dtc = models.IntegerField(db_column='Quality_dTC', blank=True, null=True)  # Field name made lowercase.
    dca = models.FloatField(db_column='dCA', blank=True, null=True)  # Field name made lowercase.
    quality_dca = models.IntegerField(db_column='Quality_dCA', blank=True, null=True)  # Field name made lowercase.
    dcb = models.FloatField(db_column='dCB', blank=True, null=True)  # Field name made lowercase.
    quality_dcb = models.IntegerField(db_column='Quality_dCB', blank=True, null=True)  # Field name made lowercase.
    dcc = models.FloatField(db_column='dCC', blank=True, null=True)  # Field name made lowercase.
    quality_dcc = models.IntegerField(db_column='Quality_dCC', blank=True, null=True)  # Field name made lowercase.
    inb = models.FloatField(db_column='Inb', blank=True, null=True)  # Field name made lowercase.
    quality_inb = models.IntegerField(db_column='Quality_Inb', blank=True, null=True)  # Field name made lowercase.
    phnb = models.FloatField(db_column='Phnb', blank=True, null=True)  # Field name made lowercase.
    quality_phnb = models.IntegerField(db_column='Quality_Phnb', blank=True, null=True)  # Field name made lowercase.
    f = models.FloatField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    quality_f = models.IntegerField(db_column='Quality_F', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MainBushMLong'


class Mainbushmshort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    ua = models.FloatField(db_column='UA', blank=True, null=True)  # Field name made lowercase.
    quality_ua = models.IntegerField(db_column='Quality_UA', blank=True, null=True)  # Field name made lowercase.
    ub = models.FloatField(db_column='UB', blank=True, null=True)  # Field name made lowercase.
    quality_ub = models.IntegerField(db_column='Quality_UB', blank=True, null=True)  # Field name made lowercase.
    uc = models.FloatField(db_column='UC', blank=True, null=True)  # Field name made lowercase.
    quality_uc = models.IntegerField(db_column='Quality_UC', blank=True, null=True)  # Field name made lowercase.
    ia = models.FloatField(db_column='IA', blank=True, null=True)  # Field name made lowercase.
    quality_ia = models.IntegerField(db_column='Quality_IA', blank=True, null=True)  # Field name made lowercase.
    ib = models.FloatField(db_column='IB', blank=True, null=True)  # Field name made lowercase.
    quality_ib = models.IntegerField(db_column='Quality_IB', blank=True, null=True)  # Field name made lowercase.
    ic = models.FloatField(db_column='IC', blank=True, null=True)  # Field name made lowercase.
    quality_ic = models.IntegerField(db_column='Quality_IC', blank=True, null=True)  # Field name made lowercase.
    tga = models.FloatField(db_column='TgA', blank=True, null=True)  # Field name made lowercase.
    quality_tga = models.IntegerField(db_column='Quality_TgA', blank=True, null=True)  # Field name made lowercase.
    tgb = models.FloatField(db_column='TgB', blank=True, null=True)  # Field name made lowercase.
    quality_tgb = models.IntegerField(db_column='Quality_TgB', blank=True, null=True)  # Field name made lowercase.
    tgc = models.FloatField(db_column='TgC', blank=True, null=True)  # Field name made lowercase.
    quality_tgc = models.IntegerField(db_column='Quality_TgC', blank=True, null=True)  # Field name made lowercase.
    ca = models.FloatField(db_column='CA', blank=True, null=True)  # Field name made lowercase.
    quality_ca = models.IntegerField(db_column='Quality_CA', blank=True, null=True)  # Field name made lowercase.
    cb = models.FloatField(db_column='CB', blank=True, null=True)  # Field name made lowercase.
    quality_cb = models.IntegerField(db_column='Quality_CB', blank=True, null=True)  # Field name made lowercase.
    cc = models.FloatField(db_column='CC', blank=True, null=True)  # Field name made lowercase.
    quality_cc = models.IntegerField(db_column='Quality_CC', blank=True, null=True)  # Field name made lowercase.
    dta = models.FloatField(db_column='dTA', blank=True, null=True)  # Field name made lowercase.
    quality_dta = models.IntegerField(db_column='Quality_dTA', blank=True, null=True)  # Field name made lowercase.
    dtb = models.FloatField(db_column='dTB', blank=True, null=True)  # Field name made lowercase.
    quality_dtb = models.IntegerField(db_column='Quality_dTB', blank=True, null=True)  # Field name made lowercase.
    dtc = models.FloatField(db_column='dTC', blank=True, null=True)  # Field name made lowercase.
    quality_dtc = models.IntegerField(db_column='Quality_dTC', blank=True, null=True)  # Field name made lowercase.
    dca = models.FloatField(db_column='dCA', blank=True, null=True)  # Field name made lowercase.
    quality_dca = models.IntegerField(db_column='Quality_dCA', blank=True, null=True)  # Field name made lowercase.
    dcb = models.FloatField(db_column='dCB', blank=True, null=True)  # Field name made lowercase.
    quality_dcb = models.IntegerField(db_column='Quality_dCB', blank=True, null=True)  # Field name made lowercase.
    dcc = models.FloatField(db_column='dCC', blank=True, null=True)  # Field name made lowercase.
    quality_dcc = models.IntegerField(db_column='Quality_dCC', blank=True, null=True)  # Field name made lowercase.
    inb = models.FloatField(db_column='Inb', blank=True, null=True)  # Field name made lowercase.
    quality_inb = models.IntegerField(db_column='Quality_Inb', blank=True, null=True)  # Field name made lowercase.
    phnb = models.FloatField(db_column='Phnb', blank=True, null=True)  # Field name made lowercase.
    quality_phnb = models.IntegerField(db_column='Quality_Phnb', blank=True, null=True)  # Field name made lowercase.
    f = models.FloatField(db_column='F', blank=True, null=True)  # Field name made lowercase.
    quality_f = models.IntegerField(db_column='Quality_F', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MainBushMShort'


class Modellong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    tnnt = models.FloatField(db_column='TNNT', blank=True, null=True)  # Field name made lowercase.
    quality_tnnt = models.IntegerField(db_column='Quality_TNNT', blank=True, null=True)  # Field name made lowercase.
    wabs = models.FloatField(db_column='WABS', blank=True, null=True)  # Field name made lowercase.
    quality_wabs = models.IntegerField(db_column='Quality_WABS', blank=True, null=True)  # Field name made lowercase.
    wbum = models.FloatField(db_column='WBUM', blank=True, null=True)  # Field name made lowercase.
    quality_wbum = models.IntegerField(db_column='Quality_WBUM', blank=True, null=True)  # Field name made lowercase.
    tkond = models.FloatField(db_column='TKOND', blank=True, null=True)  # Field name made lowercase.
    quality_tkond = models.IntegerField(db_column='Quality_TKOND', blank=True, null=True)  # Field name made lowercase.
    tpuz = models.FloatField(db_column='TPUZ', blank=True, null=True)  # Field name made lowercase.
    quality_tpuz = models.IntegerField(db_column='Quality_TPUZ', blank=True, null=True)  # Field name made lowercase.
    tpuzz = models.FloatField(db_column='TPUZZ', blank=True, null=True)  # Field name made lowercase.
    quality_tpuzz = models.IntegerField(db_column='Quality_TPUZZ', blank=True, null=True)  # Field name made lowercase.
    kstar = models.FloatField(db_column='KSTAR', blank=True, null=True)  # Field name made lowercase.
    quality_kstar = models.IntegerField(db_column='Quality_KSTAR', blank=True, null=True)  # Field name made lowercase.
    age = models.FloatField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    quality_age = models.IntegerField(db_column='Quality_AGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModelLong'


class Pvtlong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    tokr = models.FloatField(db_column='Tokr', blank=True, null=True)  # Field name made lowercase.
    quality_tokr = models.IntegerField(db_column='Quality_Tokr', blank=True, null=True)  # Field name made lowercase.
    mokr = models.FloatField(db_column='Mokr', blank=True, null=True)  # Field name made lowercase.
    quality_mokr = models.IntegerField(db_column='Quality_Mokr', blank=True, null=True)  # Field name made lowercase.
    dewpoint = models.FloatField(db_column='DewPoint', blank=True, null=True)  # Field name made lowercase.
    quality_dewpoint = models.IntegerField(db_column='Quality_DewPoint', blank=True, null=True)  # Field name made lowercase.
    errcode = models.IntegerField(db_column='ErrCode', blank=True, null=True)  # Field name made lowercase.
    quality_errcode = models.IntegerField(db_column='Quality_ErrCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVTLong'


class Pvtshort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    tokr = models.FloatField(db_column='Tokr', blank=True, null=True)  # Field name made lowercase.
    quality_tokr = models.IntegerField(db_column='Quality_Tokr', blank=True, null=True)  # Field name made lowercase.
    mokr = models.FloatField(db_column='Mokr', blank=True, null=True)  # Field name made lowercase.
    quality_mokr = models.IntegerField(db_column='Quality_Mokr', blank=True, null=True)  # Field name made lowercase.
    dewpoint = models.FloatField(db_column='DewPoint', blank=True, null=True)  # Field name made lowercase.
    quality_dewpoint = models.IntegerField(db_column='Quality_DewPoint', blank=True, null=True)  # Field name made lowercase.
    errcode = models.IntegerField(db_column='ErrCode', blank=True, null=True)  # Field name made lowercase.
    quality_errcode = models.IntegerField(db_column='Quality_ErrCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PVTShort'


class RejimLong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    il_vn = models.FloatField(db_column='IL_VN', blank=True, null=True)  # Field name made lowercase.
    quality_il_vn = models.IntegerField(db_column='Quality_IL_VN', blank=True, null=True)  # Field name made lowercase.
    tvsm = models.FloatField(db_column='TVSM', blank=True, null=True)  # Field name made lowercase.
    quality_tvsm = models.IntegerField(db_column='Quality_TVSM', blank=True, null=True)  # Field name made lowercase.
    tnsm = models.FloatField(db_column='TNSM', blank=True, null=True)  # Field name made lowercase.
    quality_tnsm = models.IntegerField(db_column='Quality_TNSM', blank=True, null=True)  # Field name made lowercase.
    tokr = models.FloatField(db_column='TOKR', blank=True, null=True)  # Field name made lowercase.
    quality_tokr = models.IntegerField(db_column='Quality_TOKR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REJIM_long'


class RejimShort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    il_vn = models.FloatField(db_column='IL_VN', blank=True, null=True)  # Field name made lowercase.
    quality_il_vn = models.IntegerField(db_column='Quality_IL_VN', blank=True, null=True)  # Field name made lowercase.
    tvsm = models.FloatField(db_column='TVSM', blank=True, null=True)  # Field name made lowercase.
    quality_tvsm = models.IntegerField(db_column='Quality_TVSM', blank=True, null=True)  # Field name made lowercase.
    tnsm = models.FloatField(db_column='TNSM', blank=True, null=True)  # Field name made lowercase.
    quality_tnsm = models.IntegerField(db_column='Quality_TNSM', blank=True, null=True)  # Field name made lowercase.
    tokr = models.FloatField(db_column='TOKR', blank=True, null=True)  # Field name made lowercase.
    quality_tokr = models.IntegerField(db_column='Quality_TOKR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REJIM_short'


class RpnModel(models.Model):
    kolvo_perekluch = models.IntegerField(blank=True, null=True)
    iznos_mex = models.FloatField(blank=True, null=True)
    iznos_comm = models.FloatField(blank=True, null=True)
    last_switch = models.TextField(blank=True, null=True)
    curr_otp = models.IntegerField(blank=True, null=True)
    otp_numb = models.FloatField(blank=True, null=True)
    n0atom = models.FloatField(db_column='N0atom', blank=True, null=True)  # Field name made lowercase.
    inomatom = models.FloatField(db_column='Inomatom', blank=True, null=True)  # Field name made lowercase.
    nmaxatom = models.FloatField(db_column='Nmaxatom', blank=True, null=True)  # Field name made lowercase.
    katom = models.FloatField(db_column='Katom', blank=True, null=True)  # Field name made lowercase.
    warnmex = models.FloatField(blank=True, null=True)
    warnoverall = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RPN_model'


class SmtoConf(models.Model):
    lastserv_day = models.FloatField(db_column='LastServ_day', blank=True, null=True)  # Field name made lowercase.
    lastserv_month = models.FloatField(db_column='LastServ_month', blank=True, null=True)  # Field name made lowercase.
    lastserv_year = models.FloatField(db_column='LastServ_year', blank=True, null=True)  # Field name made lowercase.
    serv_period = models.FloatField(db_column='Serv_Period', blank=True, null=True)  # Field name made lowercase.
    warn_serv = models.FloatField(db_column='Warn_Serv', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMTO_Conf'


class TobjectConf(models.Model):
    trans_mode = models.TextField(db_column='Trans_Mode', blank=True, null=True)  # Field name made lowercase.
    prod_fact = models.TextField(db_column='Prod_Fact', blank=True, null=True)  # Field name made lowercase.
    ser_number = models.TextField(db_column='Ser_Number', blank=True, null=True)  # Field name made lowercase.
    stat_name = models.TextField(db_column='Stat_Name', blank=True, null=True)  # Field name made lowercase.
    create_day = models.IntegerField(db_column='Create_Day', blank=True, null=True)  # Field name made lowercase.
    create_month = models.IntegerField(db_column='Create_Month', blank=True, null=True)  # Field name made lowercase.
    create_year = models.IntegerField(db_column='Create_Year', blank=True, null=True)  # Field name made lowercase.
    start_day = models.IntegerField(db_column='Start_Day', blank=True, null=True)  # Field name made lowercase.
    start_month = models.IntegerField(db_column='Start_Month', blank=True, null=True)  # Field name made lowercase.
    start_year = models.IntegerField(db_column='Start_Year', blank=True, null=True)  # Field name made lowercase.
    lres = models.FloatField(db_column='Lres', blank=True, null=True)  # Field name made lowercase.
    lo = models.FloatField(db_column='Lo', blank=True, null=True)  # Field name made lowercase.
    lastserv_day = models.FloatField(db_column='LastServ_day', blank=True, null=True)  # Field name made lowercase.
    lastserv_month = models.FloatField(db_column='LastServ_month', blank=True, null=True)  # Field name made lowercase.
    lastserv_year = models.IntegerField(db_column='LastServ_year', blank=True, null=True)  # Field name made lowercase.
    serv_period = models.FloatField(db_column='Serv_Period', blank=True, null=True)  # Field name made lowercase.
    warn_serv = models.FloatField(db_column='Warn_Serv', blank=True, null=True)  # Field name made lowercase.
    tar = models.FloatField(db_column='TAR', blank=True, null=True)  # Field name made lowercase.
    obm3 = models.IntegerField(db_column='Obm3', blank=True, null=True)  # Field name made lowercase.
    phase = models.IntegerField(db_column='Phase', blank=True, null=True)  # Field name made lowercase.
    pnom = models.FloatField(db_column='Pnom', blank=True, null=True)  # Field name made lowercase.
    zas = models.IntegerField(db_column='Zas', blank=True, null=True)  # Field name made lowercase.
    vlag = models.IntegerField(db_column='Vlag', blank=True, null=True)  # Field name made lowercase.
    oilt1 = models.IntegerField(db_column='OilT1', blank=True, null=True)  # Field name made lowercase.
    m1 = models.FloatField(blank=True, null=True)
    cat1 = models.FloatField(db_column='CaT1', blank=True, null=True)  # Field name made lowercase.
    c25t1 = models.FloatField(db_column='C25T1', blank=True, null=True)  # Field name made lowercase.
    oilt2 = models.IntegerField(db_column='OilT2', blank=True, null=True)  # Field name made lowercase.
    cat2 = models.FloatField(db_column='CaT2', blank=True, null=True)  # Field name made lowercase.
    c25t2 = models.FloatField(db_column='C25T2', blank=True, null=True)  # Field name made lowercase.
    oild = models.IntegerField(db_column='OilD', blank=True, null=True)  # Field name made lowercase.
    cad = models.FloatField(db_column='CaD', blank=True, null=True)  # Field name made lowercase.
    c25d = models.FloatField(db_column='C25D', blank=True, null=True)  # Field name made lowercase.
    mdc = models.IntegerField(db_column='MDC', blank=True, null=True)  # Field name made lowercase.
    woil = models.IntegerField(db_column='WOil', blank=True, null=True)  # Field name made lowercase.
    aoil = models.IntegerField(db_column='AOil', blank=True, null=True)  # Field name made lowercase.
    wnnt = models.IntegerField(db_column='WNNT', blank=True, null=True)  # Field name made lowercase.
    annt = models.IntegerField(db_column='ANNT', blank=True, null=True)  # Field name made lowercase.
    unom0 = models.FloatField(db_column='Unom0', blank=True, null=True)  # Field name made lowercase.
    unom1 = models.FloatField(db_column='Unom1', blank=True, null=True)  # Field name made lowercase.
    unom2 = models.FloatField(db_column='Unom2', blank=True, null=True)  # Field name made lowercase.
    inom0 = models.FloatField(db_column='Inom0', blank=True, null=True)  # Field name made lowercase.
    inom1 = models.FloatField(db_column='Inom1', blank=True, null=True)  # Field name made lowercase.
    inom2 = models.FloatField(db_column='Inom2', blank=True, null=True)  # Field name made lowercase.
    inom3 = models.FloatField(db_column='Inom3', blank=True, null=True)  # Field name made lowercase.
    pxx = models.FloatField(db_column='Pxx', blank=True, null=True)  # Field name made lowercase.
    pkz0 = models.FloatField(db_column='Pkz0', blank=True, null=True)  # Field name made lowercase.
    pkz1 = models.FloatField(db_column='Pkz1', blank=True, null=True)  # Field name made lowercase.
    pkz2 = models.FloatField(db_column='Pkz2', blank=True, null=True)  # Field name made lowercase.
    dtvsm = models.FloatField(db_column='dTvsm', blank=True, null=True)  # Field name made lowercase.
    tauvsm = models.FloatField(db_column='Tauvsm', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    k11 = models.FloatField(blank=True, null=True)
    k21 = models.FloatField(blank=True, null=True)
    k22 = models.FloatField(blank=True, null=True)
    nob = models.IntegerField(db_column='Nob', blank=True, null=True)  # Field name made lowercase.
    nnt0_iob = models.IntegerField(db_column='NNT0_iob', blank=True, null=True)  # Field name made lowercase.
    nnt0_dtnnt = models.FloatField(db_column='NNT0_dTnnt', blank=True, null=True)  # Field name made lowercase.
    nnt0_taunnt = models.FloatField(db_column='NNT0_Taunnt', blank=True, null=True)  # Field name made lowercase.
    nnt0_y = models.FloatField(db_column='NNT0_y', blank=True, null=True)  # Field name made lowercase.
    nnt1_iob = models.IntegerField(db_column='NNT1_iob', blank=True, null=True)  # Field name made lowercase.
    nnt1_dtnnt = models.FloatField(db_column='NNT1_dTnnt', blank=True, null=True)  # Field name made lowercase.
    nnt1_taunnt = models.FloatField(db_column='NNT1_Taunnt', blank=True, null=True)  # Field name made lowercase.
    nnt1_y = models.FloatField(db_column='NNT1_y', blank=True, null=True)  # Field name made lowercase.
    nnt2_iob = models.IntegerField(db_column='NNT2_iob', blank=True, null=True)  # Field name made lowercase.
    nnt2_dtnnt = models.FloatField(db_column='NNT2_dTnnt', blank=True, null=True)  # Field name made lowercase.
    nnt2_taunnt = models.FloatField(db_column='NNT2_Taunnt', blank=True, null=True)  # Field name made lowercase.
    nnt2_y = models.FloatField(db_column='NNT2_y', blank=True, null=True)  # Field name made lowercase.
    nnt3_iob = models.IntegerField(db_column='NNT3_iob', blank=True, null=True)  # Field name made lowercase.
    nnt3_dtnnt = models.FloatField(db_column='NNT3_dTnnt', blank=True, null=True)  # Field name made lowercase.
    nnt3_taunnt = models.FloatField(db_column='NNT3_Taunnt', blank=True, null=True)  # Field name made lowercase.
    nnt3_y = models.FloatField(db_column='NNT3_y', blank=True, null=True)  # Field name made lowercase.
    puvn = models.IntegerField(db_column='PUvn', blank=True, null=True)  # Field name made lowercase.
    pusn = models.IntegerField(db_column='PUsn', blank=True, null=True)  # Field name made lowercase.
    punn = models.IntegerField(db_column='PUnn', blank=True, null=True)  # Field name made lowercase.
    npu = models.IntegerField(db_column='Npu', blank=True, null=True)  # Field name made lowercase.
    nreg = models.IntegerField(db_column='Nreg', blank=True, null=True)  # Field name made lowercase.
    du = models.FloatField(db_column='DU', blank=True, null=True)  # Field name made lowercase.
    wabs_warn = models.FloatField(db_column='WABS_Warn', blank=True, null=True)  # Field name made lowercase.
    wabs_alarm = models.FloatField(db_column='WABS_Alarm', blank=True, null=True)  # Field name made lowercase.
    age_starting = models.FloatField(db_column='Age_starting', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TObject_Conf'


class Toillong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    toil = models.FloatField(db_column='TOil', blank=True, null=True)  # Field name made lowercase.
    quality_toil = models.IntegerField(db_column='Quality_TOil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOilLong'


class Toilshort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    toil = models.FloatField(db_column='TOil', blank=True, null=True)  # Field name made lowercase.
    quality_toil = models.IntegerField(db_column='Quality_TOil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOilShort'


class Vvibrlong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    vviba1 = models.FloatField(db_column='VVibA1', blank=True, null=True)  # Field name made lowercase.
    quality_vviba1 = models.IntegerField(db_column='Quality_VVibA1', blank=True, null=True)  # Field name made lowercase.
    vviba2 = models.FloatField(db_column='VVibA2', blank=True, null=True)  # Field name made lowercase.
    quality_vviba2 = models.IntegerField(db_column='Quality_VVibA2', blank=True, null=True)  # Field name made lowercase.
    vviba3 = models.FloatField(db_column='VVibA3', blank=True, null=True)  # Field name made lowercase.
    quality_vviba3 = models.IntegerField(db_column='Quality_VVibA3', blank=True, null=True)  # Field name made lowercase.
    vvibs1 = models.FloatField(db_column='VVibS1', blank=True, null=True)  # Field name made lowercase.
    quality_vvibs1 = models.IntegerField(db_column='Quality_VVibS1', blank=True, null=True)  # Field name made lowercase.
    vvibs2 = models.FloatField(db_column='VVibS2', blank=True, null=True)  # Field name made lowercase.
    quality_vvibs2 = models.IntegerField(db_column='Quality_VVibS2', blank=True, null=True)  # Field name made lowercase.
    vvibs3 = models.FloatField(db_column='VVibS3', blank=True, null=True)  # Field name made lowercase.
    quality_vvibs3 = models.IntegerField(db_column='Quality_VVibS3', blank=True, null=True)  # Field name made lowercase.
    vvibv1 = models.FloatField(db_column='VVibV1', blank=True, null=True)  # Field name made lowercase.
    quality_vvibv1 = models.IntegerField(db_column='Quality_VVibV1', blank=True, null=True)  # Field name made lowercase.
    vvibv2 = models.FloatField(db_column='VVibV2', blank=True, null=True)  # Field name made lowercase.
    quality_vvibv2 = models.IntegerField(db_column='Quality_VVibV2', blank=True, null=True)  # Field name made lowercase.
    vvibv3 = models.FloatField(db_column='VVibV3', blank=True, null=True)  # Field name made lowercase.
    quality_vvibv3 = models.IntegerField(db_column='Quality_VVibV3', blank=True, null=True)  # Field name made lowercase.
    setvviba_w = models.FloatField(db_column='SetVVibA_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvviba_w = models.IntegerField(db_column='Quality_SetVVibA_W', blank=True, null=True)  # Field name made lowercase.
    setvviba_a = models.FloatField(db_column='SetVVibA_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvviba_a = models.IntegerField(db_column='Quality_SetVVibA_A', blank=True, null=True)  # Field name made lowercase.
    setvvibs_w = models.FloatField(db_column='SetVVibS_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibs_w = models.IntegerField(db_column='Quality_SetVVibS_W', blank=True, null=True)  # Field name made lowercase.
    setvvibs_a = models.FloatField(db_column='SetVVibS_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibs_a = models.IntegerField(db_column='Quality_SetVVibS_A', blank=True, null=True)  # Field name made lowercase.
    setvvibv_w = models.FloatField(db_column='SetVVibV_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibv_w = models.IntegerField(db_column='Quality_SetVVibV_W', blank=True, null=True)  # Field name made lowercase.
    setvvibv_a = models.FloatField(db_column='SetVVibV_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibv_a = models.IntegerField(db_column='Quality_SetVVibV_A', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VVibrLong'


class Vvibrshort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    vviba1 = models.FloatField(db_column='VVibA1', blank=True, null=True)  # Field name made lowercase.
    quality_vviba1 = models.IntegerField(db_column='Quality_VVibA1', blank=True, null=True)  # Field name made lowercase.
    vviba2 = models.FloatField(db_column='VVibA2', blank=True, null=True)  # Field name made lowercase.
    quality_vviba2 = models.IntegerField(db_column='Quality_VVibA2', blank=True, null=True)  # Field name made lowercase.
    vviba3 = models.FloatField(db_column='VVibA3', blank=True, null=True)  # Field name made lowercase.
    quality_vviba3 = models.IntegerField(db_column='Quality_VVibA3', blank=True, null=True)  # Field name made lowercase.
    vvibs1 = models.FloatField(db_column='VVibS1', blank=True, null=True)  # Field name made lowercase.
    quality_vvibs1 = models.IntegerField(db_column='Quality_VVibS1', blank=True, null=True)  # Field name made lowercase.
    vvibs2 = models.FloatField(db_column='VVibS2', blank=True, null=True)  # Field name made lowercase.
    quality_vvibs2 = models.IntegerField(db_column='Quality_VVibS2', blank=True, null=True)  # Field name made lowercase.
    vvibs3 = models.FloatField(db_column='VVibS3', blank=True, null=True)  # Field name made lowercase.
    quality_vvibs3 = models.IntegerField(db_column='Quality_VVibS3', blank=True, null=True)  # Field name made lowercase.
    vvibv1 = models.FloatField(db_column='VVibV1', blank=True, null=True)  # Field name made lowercase.
    quality_vvibv1 = models.IntegerField(db_column='Quality_VVibV1', blank=True, null=True)  # Field name made lowercase.
    vvibv2 = models.FloatField(db_column='VVibV2', blank=True, null=True)  # Field name made lowercase.
    quality_vvibv2 = models.IntegerField(db_column='Quality_VVibV2', blank=True, null=True)  # Field name made lowercase.
    vvibv3 = models.FloatField(db_column='VVibV3', blank=True, null=True)  # Field name made lowercase.
    quality_vvibv3 = models.IntegerField(db_column='Quality_VVibV3', blank=True, null=True)  # Field name made lowercase.
    setvviba_w = models.FloatField(db_column='SetVVibA_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvviba_w = models.IntegerField(db_column='Quality_SetVVibA_W', blank=True, null=True)  # Field name made lowercase.
    setvviba_a = models.FloatField(db_column='SetVVibA_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvviba_a = models.IntegerField(db_column='Quality_SetVVibA_A', blank=True, null=True)  # Field name made lowercase.
    setvvibs_w = models.FloatField(db_column='SetVVibS_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibs_w = models.IntegerField(db_column='Quality_SetVVibS_W', blank=True, null=True)  # Field name made lowercase.
    setvvibs_a = models.FloatField(db_column='SetVVibS_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibs_a = models.IntegerField(db_column='Quality_SetVVibS_A', blank=True, null=True)  # Field name made lowercase.
    setvvibv_w = models.FloatField(db_column='SetVVibV_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibv_w = models.IntegerField(db_column='Quality_SetVVibV_W', blank=True, null=True)  # Field name made lowercase.
    setvvibv_a = models.FloatField(db_column='SetVVibV_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvvibv_a = models.IntegerField(db_column='Quality_SetVVibV_A', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VVibrShort'


class Vibrlong(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    viba1 = models.FloatField(db_column='VibA1', blank=True, null=True)  # Field name made lowercase.
    quality_viba1 = models.IntegerField(db_column='Quality_VibA1', blank=True, null=True)  # Field name made lowercase.
    viba2 = models.FloatField(db_column='VibA2', blank=True, null=True)  # Field name made lowercase.
    quality_viba2 = models.IntegerField(db_column='Quality_VibA2', blank=True, null=True)  # Field name made lowercase.
    viba3 = models.FloatField(db_column='VibA3', blank=True, null=True)  # Field name made lowercase.
    quality_viba3 = models.IntegerField(db_column='Quality_VibA3', blank=True, null=True)  # Field name made lowercase.
    vibs1 = models.FloatField(db_column='VibS1', blank=True, null=True)  # Field name made lowercase.
    quality_vibs1 = models.IntegerField(db_column='Quality_VibS1', blank=True, null=True)  # Field name made lowercase.
    vibs2 = models.FloatField(db_column='VibS2', blank=True, null=True)  # Field name made lowercase.
    quality_vibs2 = models.IntegerField(db_column='Quality_VibS2', blank=True, null=True)  # Field name made lowercase.
    vibs3 = models.FloatField(db_column='VibS3', blank=True, null=True)  # Field name made lowercase.
    quality_vibs3 = models.IntegerField(db_column='Quality_VibS3', blank=True, null=True)  # Field name made lowercase.
    vibv1 = models.FloatField(db_column='VibV1', blank=True, null=True)  # Field name made lowercase.
    quality_vibv1 = models.IntegerField(db_column='Quality_VibV1', blank=True, null=True)  # Field name made lowercase.
    vibv2 = models.FloatField(db_column='VibV2', blank=True, null=True)  # Field name made lowercase.
    quality_vibv2 = models.IntegerField(db_column='Quality_VibV2', blank=True, null=True)  # Field name made lowercase.
    vibv3 = models.FloatField(db_column='VibV3', blank=True, null=True)  # Field name made lowercase.
    quality_vibv3 = models.IntegerField(db_column='Quality_VibV3', blank=True, null=True)  # Field name made lowercase.
    setviba_w = models.FloatField(db_column='SetVibA_W', blank=True, null=True)  # Field name made lowercase.
    quality_setviba_w = models.IntegerField(db_column='Quality_SetVibA_W', blank=True, null=True)  # Field name made lowercase.
    setviba_a = models.FloatField(db_column='SetVibA_A', blank=True, null=True)  # Field name made lowercase.
    quality_setviba_a = models.IntegerField(db_column='Quality_SetVibA_A', blank=True, null=True)  # Field name made lowercase.
    setvibs_w = models.FloatField(db_column='SetVibS_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvibs_w = models.IntegerField(db_column='Quality_SetVibS_W', blank=True, null=True)  # Field name made lowercase.
    setvibs_a = models.FloatField(db_column='SetVibS_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvibs_a = models.IntegerField(db_column='Quality_SetVibS_A', blank=True, null=True)  # Field name made lowercase.
    setvibv_w = models.FloatField(db_column='SetVibV_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvibv_w = models.IntegerField(db_column='Quality_SetVibV_W', blank=True, null=True)  # Field name made lowercase.
    setvibv_a = models.FloatField(db_column='SetVibV_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvibv_a = models.IntegerField(db_column='Quality_SetVibV_A', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VibrLong'


class Vibrshort(models.Model):
    time = models.TextField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    viba1 = models.FloatField(db_column='VibA1', blank=True, null=True)  # Field name made lowercase.
    quality_viba1 = models.IntegerField(db_column='Quality_VibA1', blank=True, null=True)  # Field name made lowercase.
    viba2 = models.FloatField(db_column='VibA2', blank=True, null=True)  # Field name made lowercase.
    quality_viba2 = models.IntegerField(db_column='Quality_VibA2', blank=True, null=True)  # Field name made lowercase.
    viba3 = models.FloatField(db_column='VibA3', blank=True, null=True)  # Field name made lowercase.
    quality_viba3 = models.IntegerField(db_column='Quality_VibA3', blank=True, null=True)  # Field name made lowercase.
    vibs1 = models.FloatField(db_column='VibS1', blank=True, null=True)  # Field name made lowercase.
    quality_vibs1 = models.IntegerField(db_column='Quality_VibS1', blank=True, null=True)  # Field name made lowercase.
    vibs2 = models.FloatField(db_column='VibS2', blank=True, null=True)  # Field name made lowercase.
    quality_vibs2 = models.IntegerField(db_column='Quality_VibS2', blank=True, null=True)  # Field name made lowercase.
    vibs3 = models.FloatField(db_column='VibS3', blank=True, null=True)  # Field name made lowercase.
    quality_vibs3 = models.IntegerField(db_column='Quality_VibS3', blank=True, null=True)  # Field name made lowercase.
    vibv1 = models.FloatField(db_column='VibV1', blank=True, null=True)  # Field name made lowercase.
    quality_vibv1 = models.IntegerField(db_column='Quality_VibV1', blank=True, null=True)  # Field name made lowercase.
    vibv2 = models.FloatField(db_column='VibV2', blank=True, null=True)  # Field name made lowercase.
    quality_vibv2 = models.IntegerField(db_column='Quality_VibV2', blank=True, null=True)  # Field name made lowercase.
    vibv3 = models.FloatField(db_column='VibV3', blank=True, null=True)  # Field name made lowercase.
    quality_vibv3 = models.IntegerField(db_column='Quality_VibV3', blank=True, null=True)  # Field name made lowercase.
    setviba_w = models.FloatField(db_column='SetVibA_W', blank=True, null=True)  # Field name made lowercase.
    quality_setviba_w = models.IntegerField(db_column='Quality_SetVibA_W', blank=True, null=True)  # Field name made lowercase.
    setviba_a = models.FloatField(db_column='SetVibA_A', blank=True, null=True)  # Field name made lowercase.
    quality_setviba_a = models.IntegerField(db_column='Quality_SetVibA_A', blank=True, null=True)  # Field name made lowercase.
    setvibs_w = models.FloatField(db_column='SetVibS_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvibs_w = models.IntegerField(db_column='Quality_SetVibS_W', blank=True, null=True)  # Field name made lowercase.
    setvibs_a = models.FloatField(db_column='SetVibS_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvibs_a = models.IntegerField(db_column='Quality_SetVibS_A', blank=True, null=True)  # Field name made lowercase.
    setvibv_w = models.FloatField(db_column='SetVibV_W', blank=True, null=True)  # Field name made lowercase.
    quality_setvibv_w = models.IntegerField(db_column='Quality_SetVibV_W', blank=True, null=True)  # Field name made lowercase.
    setvibv_a = models.FloatField(db_column='SetVibV_A', blank=True, null=True)  # Field name made lowercase.
    quality_setvibv_a = models.IntegerField(db_column='Quality_SetVibV_A', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VibrShort'


class MemoryTableHystogram(models.Model):
    a1 = models.FloatField(blank=True, null=True)
    a2 = models.FloatField(blank=True, null=True)
    a3 = models.FloatField(blank=True, null=True)
    a4 = models.FloatField(blank=True, null=True)
    a5 = models.FloatField(blank=True, null=True)
    a6 = models.FloatField(blank=True, null=True)
    a7 = models.FloatField(blank=True, null=True)
    a8 = models.FloatField(blank=True, null=True)
    a9 = models.FloatField(blank=True, null=True)
    a10 = models.FloatField(blank=True, null=True)
    a12 = models.FloatField(blank=True, null=True)
    a22 = models.FloatField(blank=True, null=True)
    a32 = models.FloatField(blank=True, null=True)
    a42 = models.FloatField(blank=True, null=True)
    a52 = models.FloatField(blank=True, null=True)
    a62 = models.FloatField(blank=True, null=True)
    a72 = models.FloatField(blank=True, null=True)
    a82 = models.FloatField(blank=True, null=True)
    a92 = models.FloatField(blank=True, null=True)
    a102 = models.FloatField(blank=True, null=True)
    a13 = models.FloatField(blank=True, null=True)
    a23 = models.FloatField(blank=True, null=True)
    a33 = models.FloatField(blank=True, null=True)
    a43 = models.FloatField(blank=True, null=True)
    a53 = models.FloatField(blank=True, null=True)
    a63 = models.FloatField(blank=True, null=True)
    a73 = models.FloatField(blank=True, null=True)
    a83 = models.FloatField(blank=True, null=True)
    a93 = models.FloatField(blank=True, null=True)
    a103 = models.FloatField(blank=True, null=True)
    a14 = models.FloatField(blank=True, null=True)
    a24 = models.FloatField(blank=True, null=True)
    a34 = models.FloatField(blank=True, null=True)
    a44 = models.FloatField(blank=True, null=True)
    a54 = models.FloatField(blank=True, null=True)
    a64 = models.FloatField(blank=True, null=True)
    a74 = models.FloatField(blank=True, null=True)
    a84 = models.FloatField(blank=True, null=True)
    a94 = models.FloatField(blank=True, null=True)
    a104 = models.FloatField(blank=True, null=True)
    a15 = models.FloatField(blank=True, null=True)
    a25 = models.FloatField(blank=True, null=True)
    a35 = models.FloatField(blank=True, null=True)
    a45 = models.FloatField(blank=True, null=True)
    a55 = models.FloatField(blank=True, null=True)
    a65 = models.FloatField(blank=True, null=True)
    a75 = models.FloatField(blank=True, null=True)
    a85 = models.FloatField(blank=True, null=True)
    a95 = models.FloatField(blank=True, null=True)
    a105 = models.FloatField(blank=True, null=True)
    a16 = models.FloatField(blank=True, null=True)
    a26 = models.FloatField(blank=True, null=True)
    a36 = models.FloatField(blank=True, null=True)
    a46 = models.FloatField(blank=True, null=True)
    a56 = models.FloatField(blank=True, null=True)
    a66 = models.FloatField(blank=True, null=True)
    a76 = models.FloatField(blank=True, null=True)
    a86 = models.FloatField(blank=True, null=True)
    a96 = models.FloatField(blank=True, null=True)
    a106 = models.FloatField(blank=True, null=True)
    a17 = models.FloatField(blank=True, null=True)
    a27 = models.FloatField(blank=True, null=True)
    a37 = models.FloatField(blank=True, null=True)
    a47 = models.FloatField(blank=True, null=True)
    a57 = models.FloatField(blank=True, null=True)
    a67 = models.FloatField(blank=True, null=True)
    a77 = models.FloatField(blank=True, null=True)
    a87 = models.FloatField(blank=True, null=True)
    a97 = models.FloatField(blank=True, null=True)
    a107 = models.FloatField(blank=True, null=True)
    a18 = models.FloatField(blank=True, null=True)
    a28 = models.FloatField(blank=True, null=True)
    a38 = models.FloatField(blank=True, null=True)
    a48 = models.FloatField(blank=True, null=True)
    a58 = models.FloatField(blank=True, null=True)
    a68 = models.FloatField(blank=True, null=True)
    a78 = models.FloatField(blank=True, null=True)
    a88 = models.FloatField(blank=True, null=True)
    a98 = models.FloatField(blank=True, null=True)
    a108 = models.FloatField(blank=True, null=True)
    a19 = models.FloatField(blank=True, null=True)
    a29 = models.FloatField(blank=True, null=True)
    a39 = models.FloatField(blank=True, null=True)
    a49 = models.FloatField(blank=True, null=True)
    a59 = models.FloatField(blank=True, null=True)
    a69 = models.FloatField(blank=True, null=True)
    a79 = models.FloatField(blank=True, null=True)
    a89 = models.FloatField(blank=True, null=True)
    a99 = models.FloatField(blank=True, null=True)
    a109 = models.FloatField(blank=True, null=True)
    a110 = models.FloatField(blank=True, null=True)
    a210 = models.FloatField(blank=True, null=True)
    a310 = models.FloatField(blank=True, null=True)
    a410 = models.FloatField(blank=True, null=True)
    a510 = models.FloatField(blank=True, null=True)
    a610 = models.FloatField(blank=True, null=True)
    a710 = models.FloatField(blank=True, null=True)
    a810 = models.FloatField(blank=True, null=True)
    a910 = models.FloatField(blank=True, null=True)
    a1010 = models.FloatField(blank=True, null=True)
    a111 = models.FloatField(blank=True, null=True)
    a211 = models.FloatField(blank=True, null=True)
    a311 = models.FloatField(blank=True, null=True)
    a411 = models.FloatField(blank=True, null=True)
    a511 = models.FloatField(blank=True, null=True)
    a611 = models.FloatField(blank=True, null=True)
    a711 = models.FloatField(blank=True, null=True)
    a811 = models.FloatField(blank=True, null=True)
    a911 = models.FloatField(blank=True, null=True)
    a1011 = models.FloatField(blank=True, null=True)
    a112 = models.FloatField(blank=True, null=True)
    a212 = models.FloatField(blank=True, null=True)
    a312 = models.FloatField(blank=True, null=True)
    a412 = models.FloatField(blank=True, null=True)
    a512 = models.FloatField(blank=True, null=True)
    a612 = models.FloatField(blank=True, null=True)
    a712 = models.FloatField(blank=True, null=True)
    a812 = models.FloatField(blank=True, null=True)
    a912 = models.FloatField(blank=True, null=True)
    a1012 = models.FloatField(blank=True, null=True)
    a113 = models.FloatField(blank=True, null=True)
    a213 = models.FloatField(blank=True, null=True)
    a313 = models.FloatField(blank=True, null=True)
    a413 = models.FloatField(blank=True, null=True)
    a513 = models.FloatField(blank=True, null=True)
    a613 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memory_table_hystogram'


class Password(models.Model):
    psw = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password'

