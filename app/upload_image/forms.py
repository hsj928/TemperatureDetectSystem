from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, DateField, FloatField
from wtforms.validators import DataRequired
from wtforms_components import TimeField

from .. import no_co_images, co_images, original_images, clean_images, ccd_images, matrix_temp


class UploadNoCoImageForm(FlaskForm):
    """
    上传未诊断图片的表单
    """
    no_co_image = FileField('未诊断图片', validators=[FileAllowed(no_co_images, '只能上传图片！'), FileRequired('尚未选取图片！')])
    image_num = StringField('图像编号', validators=[DataRequired()])
    power_company_province = StringField('省级供电公司')
    power_company_cityorcountry = StringField('市县级供电公司')
    suborlineorzone_name = StringField('变电站（线路、台区）名')
    location_detail = TextAreaField('详细位置')
    location_nature = TextAreaField('地点性质')
    production_date = DateField('出厂日期')
    run_date = DateField('投运日期')
    detection_date = DateField('检测日期')
    detection_time = TimeField('详细时间')
    report_date = DateField('报告日期')
    instrument_model = StringField('仪器型号')
    instrument_num = StringField('仪器编号')
    reporter = StringField('报告人')
    steward = StringField('负责人')
    inspector = StringField('检测人')
    reviewer = StringField('校阅人')
    auditor = StringField('审核人')
    rated_current = FloatField('额定电流')
    load_current = FloatField('负荷电流')
    voltage_level = FloatField('电压等级')
    weather = StringField('天气')
    emissivity = FloatField('辐射系数')
    wind_speed = FloatField('风速')
    test_distance = FloatField('测试距离')
    max_temp = FloatField('最高温度')
    min_temp = FloatField('最低温度')
    env_temp = FloatField('环境温度')
    env_humi = FloatField('环境湿度')
    device_name = StringField('设备名称')
    device_type = StringField('设备类型')
    interval_name = StringField('间隔名称')
    test_unit = StringField('实验单位')
    test_nature = StringField('检测性质')


class UploadCoImageForm(FlaskForm):
    """
    上传诊断后图片的表单
    """

    original_image = FileField('原图', validators=[FileAllowed(original_images, '只能上传图片！'), FileRequired('尚未选取图片！')])
    clean_image = FileField('净图', validators=[FileAllowed(clean_images, '只能上传图片！'), FileRequired('尚未选取图片！')])
    co_image = FileField('诊断后图', validators=[FileAllowed(co_images, '只能上传图片！'), FileRequired('尚未选取图片！')])
    ccd_image = FileField('可见光图', validators=[FileAllowed(ccd_images, '只能上传图片！')])
    matrix_file = FileField('温度矩阵', validators=[FileAllowed(matrix_temp, '只能上传 txt 文件！'), FileRequired('尚未选取文件！')])
    image_num = StringField('图像编号', validators=[DataRequired()])
    power_company_province = StringField('省级供电公司')
    power_company_cityorcountry = StringField('市县级供电公司')
    suborlineorzone_name = StringField('变电站（线路、台区）名')
    location_detail = TextAreaField('详细位置')
    location_nature = TextAreaField('地点性质')
    production_date = DateField('出厂日期')
    run_date = DateField('投运日期')
    detection_date = DateField('检测日期')
    detection_time = TimeField('详细时间')
    report_date = DateField('报告日期')
    instrument_model = StringField('仪器型号')
    instrument_num = StringField('仪器编号')
    reporter = StringField('报告人')
    principal = StringField('负责人')
    inspector = StringField('检测人')
    reviewer = StringField('校阅人')
    auditor = StringField('审核人')
    rated_current = FloatField('额定电流')
    load_current = FloatField('负荷电流')
    voltage_level = FloatField('电压等级')
    weather = StringField('天气')
    E = FloatField('辐射系数')
    wind_speed = FloatField('风速')
    DST = FloatField('测试距离')
    im_h_tm = FloatField('最高温度')
    im_l_tm = FloatField('最低温度')
    TATM = FloatField('环境温度')
    RH = FloatField('环境湿度')
    device_name = StringField('设备名称')
    device_type = StringField('设备类型')
    interval_name = StringField('间隔名称')
    test_unit = StringField('实验单位')
    test_nature = StringField('检测性质')
    defect_part = TextAreaField('缺陷部位')
    defect_type = TextAreaField('缺陷类型')
    trouble_rank = TextAreaField('缺陷等级')
    diagnose_analyse = TextAreaField('诊断分析')
    processing_way = TextAreaField('处理建议')
    rrg_tem = FloatField('参照体温度')
    hot_mode = TextAreaField('致热类型')
    r1_name = TextAreaField('兴趣区域1名称')
    r2_name = TextAreaField('兴趣区域2名称')
    r3_name = TextAreaField('兴趣区域3名称')
    r4_name = TextAreaField('兴趣区域4名称')
    r5_name = TextAreaField('兴趣区域5名称')
    phase1_name = TextAreaField('兴趣区域1相位')
    phase2_name = TextAreaField('兴趣区域2相位')
    phase3_name = TextAreaField('兴趣区域3相位')
    phase4_name = TextAreaField('兴趣区域4相位')
    phase5_name = TextAreaField('兴趣区域5相位')
    high_tm1 = FloatField('兴趣区域1最高温度')
    high_tm2 = FloatField('兴趣区域2最高温度')
    high_tm3 = FloatField('兴趣区域3最高温度')
    high_tm4 = FloatField('兴趣区域4最高温度')
    high_tm5 = FloatField('兴趣区域5最高温度')
    low_tm1 = FloatField('兴趣区域1最低温度')
    low_tm2 = FloatField('兴趣区域2最低温度')
    low_tm3 = FloatField('兴趣区域3最低温度')
    low_tm4 = FloatField('兴趣区域4最低温度')
    low_tm5 = FloatField('兴趣区域5最低温度')
    re_tm1 = FloatField('兴趣区域1平均温度')
    re_tm2 = FloatField('兴趣区域2平均温度')
    re_tm3 = FloatField('兴趣区域3平均温度')
    re_tm4 = FloatField('兴趣区域4平均温度')
    re_tm5 = FloatField('兴趣区域5平均温度')
    rtd = FloatField('相对温差')
    td = FloatField('温差')
