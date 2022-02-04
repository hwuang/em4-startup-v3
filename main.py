# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request, redirect, url_for, session, abort
import os
import google
import mock
import logging
from google.auth import app_engine
from google.cloud import ndb, datastore
import datetime
from datetime import datetime
from datetime import date
from datetime import time
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import random
import calendar


# app = Flask(__name__)


def get_db():
    if os.getenv('TESTING', '').startswith('yes'):
        # localhost
        os.environ["DATASTORE_DATASET"] = "test"
        os.environ["DATASTORE_PROJECT_ID"] = "test"
        os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8001"
        os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "localhost:8001/datastore"
        os.environ["DATASTORE_HOST"] = "http://localhost:8001"

        credentials = mock.Mock(spec=google.auth.credentials.Credentials)
        # db = ndb.Client(project="test", credentials=credentials)
        db = datastore.Client()
    else:
        # production
        # credentials = app_engine.Credentials()
        # db = ndb.Client(credentials=credentials, project="kp-4-0-prodv3")
        # db = ndb.Client()
        db = datastore.Client()

    return db


client = get_db()

# def ndb_wsgi_middleware(wsgi_app):
#     def middleware(environ, start_response):
#         with client.context():
#             return wsgi_app(environ, start_response)
#
#     return middleware


app = Flask(__name__)


# app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)  # Wrap the app in middleware.


# <editor-fold desc="Description">
# def ndb_wsgi_middleware(wsgi_app):
#     def middleware(environ, start_response):
#         # client = get_db()
#         with client.context():
#             return wsgi_app(environ, start_response)
#
#     return middleware
#
#
# app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)  # Wrap the app in middleware.
# </editor-fold>
# app.secret_key = '\xbb\x91Y\x08\x93R\xff\xf4\xbf%\xa8#\xa4F\xf6\n\xd9\xf4\xb0\xd2\xf75b\xa1'


# def get_db():
#     if os.getenv('GAE_ENV', '').startswith('standard'):
#         # production
#         db = ndb.Client()
#     else:
#         # localhost
#         os.environ["DATASTORE_DATASET"] = "test"
#         os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8001"
#         os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "localhost:8001/datastore"
#         os.environ["DATASTORE_HOST"] = "http://localhost:8001"
#         os.environ["DATASTORE_PROJECT_ID"] = "test"
#
#         credentials = mock.Mock(spec=google.auth.credentials.Credentials)
#         db = ndb.Client(project="test", credentials=credentials)
#
#     return db


# def ndb_wsgi_middleware(wsgi_app):
#     def middleware(environ, start_response):
#         with client.context():
#             return wsgi_app(environ, start_response)
#
#     return middleware
#
#
# app.wsgi_app = ndb_wsgi_middleware(app.wsgi_app)  # Wrap the app in middleware.


# client = get_db()


class ClientInformation(ndb.Model):
    name = ndb.StringProperty(required=True)
    lastname = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
    address1 = ndb.StringProperty()
    address2 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zipcode = ndb.StringProperty()


class ClientInformation(ndb.Model):
    name = ndb.StringProperty(required=True)
    lastname = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()
    address1 = ndb.StringProperty()
    address2 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = ndb.StringProperty()
    zipcode = ndb.StringProperty()


class UserAuthInformation(ndb.Model):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty()
    password_reset = ndb.BooleanProperty()
    client_id = ndb.IntegerProperty(required=True)
    created_on = ndb.DateTimeProperty(auto_now_add=True)
    admin = ndb.BooleanProperty(default=False)


class InsuranceInformation(ndb.Model):
    client_id = ndb.IntegerProperty(required=True)
    insurance_company = ndb.StringProperty()
    naic = ndb.StringProperty()
    policy = ndb.StringProperty()
    expiry = ndb.DateTimeProperty()


class StickerInformation(ndb.Model):
    ftp_id = ndb.IntegerProperty(required=True)
    client_id = ndb.IntegerProperty()
    sticker = ndb.StringProperty()
    expiry = ndb.DateTimeProperty()


class VehicleInformation(ndb.Model):
    user_id = ndb.IntegerProperty(required=True)
    client_id = ndb.IntegerProperty(required=True)
    ftp_id = ndb.IntegerProperty(required=True)
    tenant_id = ndb.IntegerProperty(required=True)
    imei = ndb.IntegerProperty(required=True)
    department = ndb.StringProperty()
    vin = ndb.StringProperty(required=True)
    license_plate = ndb.StringProperty(required=True)
    start_date = ndb.DateProperty()
    make = ndb.StringProperty()
    model = ndb.StringProperty()
    year = ndb.IntegerProperty()  # year is required
    vehicle_id = ndb.StringProperty()
    odometer = ndb.IntegerProperty()
    activity_date = ndb.DateProperty()
    software = ndb.JsonProperty()
    date_added = ndb.DateTimeProperty(auto_now_add=True)
    ecm_expiry_date = ndb.DateProperty()
    latest_activity_date = ndb.DateTimeProperty()
    tested = ndb.BooleanProperty()
    comments = ndb.TextProperty()


class EmCarsDailyRpt(ndb.Model):
    res_sys_no_obd = ndb.StringProperty(required=True)
    lic_st_id = ndb.StringProperty()
    ets_id = ndb.StringProperty()
    etnj2_sw_ver = ndb.StringProperty()
    vin = ndb.StringProperty()
    vin_src = ndb.StringProperty()
    vehicle_vin = ndb.StringProperty()
    vehicle_vin_src = ndb.StringProperty()
    obd2_vin_obd = ndb.StringProperty(required=True)
    vin_mask = ndb.StringProperty()
    lic_no_obd = ndb.StringProperty(required=True)
    lic_jur_obd = ndb.StringProperty(required=True)
    lic_src = ndb.StringProperty()
    model_yr_obd = ndb.IntegerProperty(required=True)
    make_obd = ndb.StringProperty(required=True)
    model_obd = ndb.StringProperty(required=True)
    gvwr = ndb.StringProperty()
    no_of_cyl = ndb.IntegerProperty()
    eng_size = ndb.IntegerProperty()
    trans_type = ndb.StringProperty()
    fuel_cd = ndb.StringProperty()
    vid_sys_no = ndb.IntegerProperty()
    curr_odo_rdng_obd = ndb.IntegerProperty(required=True)
    prev_odo_rdng_obd = ndb.IntegerProperty(required=True)
    mvc_reg_code = ndb.StringProperty()
    mvc_vehicle_type_code = ndb.StringProperty()
    test_type = ndb.StringProperty()
    start_time_obd = ndb.DateTimeProperty()
    end_time_obd = ndb.DateTimeProperty()
    create_date_obd = ndb.DateTimeProperty()
    prev_test_date = ndb.DateTimeProperty()
    emiss_test_type = ndb.StringProperty()
    primary_emiss_test_code = ndb.StringProperty()
    bulb_check_res = ndb.StringProperty()
    chk_eng_light_on_obd = ndb.StringProperty(required=True)
    indicator_light_result = ndb.StringProperty()
    exempt_from_obd = ndb.StringProperty()
    obd_bypassed = ndb.StringProperty()
    bypass_obd_allowed = ndb.StringProperty()
    obd2_connect_res = ndb.StringProperty()
    communic_res = ndb.StringProperty()
    obd = ndb.StringProperty()
    obd2_test_fl = ndb.StringProperty()
    pcm_mudule_id = ndb.StringProperty()
    obd_module_id_2 = ndb.StringProperty()
    obd_module_id_3 = ndb.StringProperty()
    obd_type = ndb.StringProperty()
    obd_calid = ndb.StringProperty()
    obd_cvn = ndb.IntegerProperty()
    cvn_exclusion = ndb.StringProperty()
    pid_count_obd = ndb.IntegerProperty(required=True)
    obd_pid00_obd = ndb.StringProperty(required=True)
    obd_pid20_obd = ndb.StringProperty(required=True)
    obd_pid40_obd = ndb.StringProperty(required=True)
    obd_rpm_obd = ndb.IntegerProperty(required=True)
    rpm_exclusion = ndb.IntegerProperty()
    misfire_mon_res_obd = ndb.StringProperty(required=True)
    fuel_sys_mon_res_obd = ndb.StringProperty(required=True)
    comp_cmpnt_res_obd = ndb.StringProperty(required=True)
    catalyst_mon_res_obd = ndb.StringProperty(required=True)
    heat_cat_mon_res_obd = ndb.StringProperty(required=True)
    evap_sys_mon_res_obd = ndb.StringProperty(required=True)
    sec_air_sys_mon_res_obd = ndb.StringProperty(required=True)
    air_cond_mon_res_obd = ndb.StringProperty(required=True)
    oxy_sens_mon_res_obd = ndb.StringProperty(required=True)
    htd_oxy_sns_mon_res_obd = ndb.StringProperty(required=True)
    egr_sys_mon_res_obd = ndb.StringProperty(required=True)
    rdy_mon_obd = ndb.IntegerProperty(required=True)
    tot_unset_rdy_mon = ndb.IntegerProperty()
    readiness_status = ndb.StringProperty()
    continuous_monit_xclusion = ndb.StringProperty()
    exempt_from_readiness = ndb.StringProperty()
    mil_command_stat = ndb.StringProperty()
    dtc1_obd = ndb.StringProperty(required=True)
    dtc2_obd = ndb.StringProperty(required=True)
    dtc3_obd = ndb.StringProperty(required=True)
    dtc4_obd = ndb.StringProperty(required=True)
    dtc5_obd = ndb.StringProperty(required=True)
    dtc6_obd = ndb.StringProperty(required=True)
    dtc7_obd = ndb.StringProperty(required=True)
    dtc8_obd = ndb.StringProperty(required=True)
    dtc9_obd = ndb.StringProperty(required=True)
    dtc10_obd = ndb.StringProperty(required=True)
    tot_stored_dtcs_obd = ndb.IntegerProperty(required=True)
    catalyst_dtc_pres_obd = ndb.StringProperty(required=True)
    pend_dtc1_obd = ndb.StringProperty(required=True)
    pend_dtc2_obd = ndb.StringProperty(required=True)
    pend_dtc3_obd = ndb.StringProperty(required=True)
    pend_dtc4_obd = ndb.StringProperty(required=True)
    pend_dtc5_obd = ndb.StringProperty(required=True)
    pend_dtc6_obd = ndb.StringProperty(required=True)
    pend_dtc7_obd = ndb.StringProperty(required=True)
    pend_dtc8_obd = ndb.StringProperty(required=True)
    pend_dtc9_obd = ndb.StringProperty(required=True)
    pend_dtc10_obd = ndb.StringProperty(required=True)
    cat_retest_exclusion = ndb.StringProperty()
    obd_warmups_obd = ndb.StringProperty(required=True)
    obd_code_cleared_distance_obd = ndb.StringProperty(required=True)
    obd_mil_on_distance_obd = ndb.StringProperty(required=True)
    obd_code_cleared_time_obd = ndb.DateTimeProperty()
    obd_mil_on_time_obd = ndb.DateTimeProperty()
    emiss_clarification = ndb.StringProperty()
    misc_comnt = ndb.StringProperty()
    misc_comnt_res = ndb.StringProperty()
    misc_emiss_reject_comment = ndb.StringProperty()
    misc_emiss_reject_result = ndb.StringProperty()
    overall_tamper_result = ndb.StringProperty()
    ex_sys_res = ndb.StringProperty()
    overall_obd2_res = ndb.StringProperty()
    exh_emiss_test_res = ndb.StringProperty()
    overall_gas_cap_res = ndb.StringProperty()
    ovr_exh_obd2_em_res = ndb.StringProperty()
    overall_emiss_res = ndb.StringProperty()
    overall_saf_res = ndb.StringProperty()
    overall_test_res = ndb.StringProperty()
    created_date_sys = ndb.DateTimeProperty()
    created_user_sys = ndb.StringProperty()
    update_date_sys = ndb.DateTimeProperty()
    update_user_sys = ndb.StringProperty()


# Emcars daily related information
class EmCarsDailyInformation(ndb.Model):
    date = ndb.DateProperty()
    time = ndb.TimeProperty()
    ftp_id = ndb.IntegerProperty(required=True)
    data_type = ndb.BooleanProperty(required=True)
    pid_data = ndb.PickleProperty()
    vin = ndb.StringProperty()


# ADMIN INITIALIZATION
class AdminAuthInformation(ndb.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    created_on = ndb.DateTimeProperty(auto_now_add=True)


# Emcars daily related information
class LastRunDate(ndb.Model):
    process_id = ndb.StringProperty(required=True)
    last_run_date = ndb.DateProperty(required=True)


def insertClient():
    client_name = '4.0 Analytics, Inc'
    lastname = ''
    phone = '862-237-7841'
    email = 'cowart.g@4-0analytics.com'
    address1 = '105 Lock Street'
    address2 = ''
    city = 'Newark'
    state = 'NJ'
    zipcode = '07103'
    # client = get_db()
    # return 'Hello World!.22...'
    key = client.key("ClientInformation")
    entity = datastore.Entity(key)

    entity.update(name=client_name, lastname=lastname, phone=phone, email=email,
                  address1=address1, address2=address2, city=city,
                  state=state, zipcode=zipcode)
    client.put(entity)
    c1_id = entity.id

    logging.info('client created {}'.format(c1_id))
    message = str('ClientInformation has been inserted with ID :{}'.format(c1_id))

    return message, c1_id


def insertUserAuthInformation(username, password, client_id):
    key = client.key("UserAuthInformation")
    entity = datastore.Entity(key)
    entity.update(username=username, password=password, client_id=client_id)

    client.put(entity)
    c1_id = entity.id

    logging.info('UserAuthInformation created {}'.format(c1_id))
    message = str('UserAuthInformation has been inserted for {} with ID :{}'.format(username, c1_id))

    return message


def insertInsuranceInformation(insurance_company, naic, policy, expiry, client_id):
    key = client.key("InsuranceInformation")
    entity = datastore.Entity(key)
    entity.update(insurance_company=insurance_company,
                  naic=naic,
                  policy=policy,
                  expiry=expiry,
                  client_id=client_id)

    client.put(entity)
    c1_id = entity.id

    logging.info('InsuranceInformation created {}'.format(c1_id))
    message = str('InsuranceInformation has been inserted ID :{}'.format(c1_id))
    return message


def insertLastRunDate(process_id, last_run_date):
    key = client.key("LastRunDate")
    entity = datastore.Entity(key)
    entity.update(process_id=process_id, last_run_date=last_run_date)
    client.put(entity)
    c1_id = entity.id

    logging.info('LastRunDate created {}'.format(c1_id))
    message = str('LastRunDate for {} has been inserted with :{}'.format(process_id, last_run_date))
    return message


def insertVehicleInformation(client_id,
                             ftp_id,
                             tenant_id,
                             imei,
                             department,
                             vin,
                             license_plate,
                             start_date,
                             make,
                             model,
                             year,
                             vehicle_id,
                             odometer,
                             ecm_expiry_date,
                             activity_date,
                             software,
                             latest_activity_date,
                             tested,
                             comments,
                             date_added,
                             user_id):
    key = client.key("VehicleInformation")
    entity = datastore.Entity(key)
    entity.update(client_id=client_id,
                  ftp_id=ftp_id,
                  tenant_id=tenant_id,
                  imei=imei,
                  department=department,
                  vin=vin,
                  license_plate=license_plate,
                  start_date=start_date,
                  make=make,
                  model=model,
                  year=year,
                  vehicle_id=vehicle_id,
                  odometer=odometer,
                  ecm_expiry_date=ecm_expiry_date,
                  activity_date=activity_date,
                  software=software,
                  latest_activity_date=latest_activity_date,
                  tested=tested,
                  comments=comments,
                  date_added=date_added,
                  user_id=user_id)
    client.put(entity)
    c1_id = entity.id
    logging.info('VehicleInformation created {}'.format(c1_id))
    message = str('VehicleInformation for vehicle {} has been inserted with ID:{}'.format(vehicle_id, c1_id))
    return message


def insertStickerInformation(sticker, expiry, ftp_id, client_id):
    key = client.key("StickerInformation")
    entity = datastore.Entity(key)
    entity.update(sticker=sticker, expiry=expiry, ftp_id=ftp_id, client_id=client_id)
    client.put(entity)
    c1_id = entity.id

    logging.info('StickerInformation created {}'.format(c1_id))
    message = str('StickerInformation for sticker {} has been inserted with :{}'.format(sticker, c1_id))
    return message


def insertEmCarsDailyRpt(
        res_sys_no_obd,
        lic_st_id,
        ets_id,
        etnj2_sw_ver,
        vin,
        vin_src,
        vehicle_vin,
        vehicle_vin_src,
        obd2_vin_obd,
        vin_mask,
        lic_no_obd,
        lic_jur_obd,
        lic_src,
        model_yr_obd,
        make_obd,
        model_obd,
        gvwr,
        no_of_cyl,
        eng_size,
        trans_type,
        fuel_cd,
        vid_sys_no,
        curr_odo_rdng_obd,
        prev_odo_rdng_obd,
        mvc_reg_code,
        mvc_vehicle_type_code,
        test_type,
        start_time_obd,
        end_time_obd,
        create_date_obd,
        prev_test_date,
        emiss_test_type,
        primary_emiss_test_code,
        bulb_check_res,
        chk_eng_light_on_obd,
        indicator_light_result,
        exempt_from_obd,
        obd_bypassed,
        bypass_obd_allowed,
        obd2_connect_res,
        communic_res,
        obd,
        obd2_test_fl,
        pcm_mudule_id,
        obd_module_id_2,
        obd_module_id_3,
        obd_type,
        obd_calid,
        obd_cvn,
        cvn_exclusion,
        pid_count_obd,
        obd_pid00_obd,
        obd_pid20_obd,
        obd_pid40_obd,
        obd_rpm_obd,
        rpm_exclusion,
        misfire_mon_res_obd,
        fuel_sys_mon_res_obd,
        comp_cmpnt_res_obd,
        catalyst_mon_res_obd,
        heat_cat_mon_res_obd,
        evap_sys_mon_res_obd,
        sec_air_sys_mon_res_obd,
        air_cond_mon_res_obd,
        oxy_sens_mon_res_obd,
        htd_oxy_sns_mon_res_obd,
        egr_sys_mon_res_obd,
        rdy_mon_obd,
        tot_unset_rdy_mon,
        readiness_status,
        continuous_monit_xclusion,
        exempt_from_readiness,
        mil_command_stat,
        dtc1_obd,
        dtc2_obd,
        dtc3_obd,
        dtc4_obd,
        dtc5_obd,
        dtc6_obd,
        dtc7_obd,
        dtc8_obd,
        dtc9_obd,
        dtc10_obd,
        tot_stored_dtcs_obd,
        catalyst_dtc_pres_obd,
        pend_dtc1_obd,
        pend_dtc2_obd,
        pend_dtc3_obd,
        pend_dtc4_obd,
        pend_dtc5_obd,
        pend_dtc6_obd,
        pend_dtc7_obd,
        pend_dtc8_obd,
        pend_dtc9_obd,
        pend_dtc10_obd,
        cat_retest_exclusion,
        obd_warmups_obd,
        obd_code_cleared_distance_obd,
        obd_mil_on_distance_obd,
        obd_code_cleared_time_obd,
        obd_mil_on_time_obd,
        emiss_clarification,
        misc_comnt,
        misc_comnt_res,
        misc_emiss_reject_comment,
        misc_emiss_reject_result,
        overall_tamper_result,
        ex_sys_res,
        overall_obd2_res,
        exh_emiss_test_res,
        overall_gas_cap_res,
        ovr_exh_obd2_em_res,
        overall_emiss_res,
        overall_saf_res,
        overall_test_res,
        created_date_sys,
        created_user_sys,
        update_date_sys,
        update_user_sys):
    key = client.key("EmCarsDailyRpt")
    entity = datastore.Entity(key)
    entity.update(res_sys_no_obd=res_sys_no_obd,
                  lic_st_id=lic_st_id,
                  ets_id=ets_id,
                  etnj2_sw_ver=etnj2_sw_ver,
                  vin=vin,
                  vin_src=vin_src,
                  vehicle_vin=vehicle_vin,
                  vehicle_vin_src=vehicle_vin_src,
                  obd2_vin_obd=obd2_vin_obd,
                  vin_mask=vin_mask,
                  lic_no_obd=lic_no_obd,
                  lic_jur_obd=lic_jur_obd,
                  lic_src=lic_src,
                  model_yr_obd=model_yr_obd,
                  make_obd=make_obd,
                  model_obd=model_obd,
                  gvwr=gvwr,
                  no_of_cyl=no_of_cyl,
                  eng_size=eng_size,
                  trans_type=trans_type,
                  fuel_cd=fuel_cd,
                  vid_sys_no=vid_sys_no,
                  curr_odo_rdng_obd=curr_odo_rdng_obd,
                  prev_odo_rdng_obd=prev_odo_rdng_obd,
                  mvc_reg_code=mvc_reg_code,
                  mvc_vehicle_type_code=mvc_vehicle_type_code,
                  test_type=test_type,
                  start_time_obd=start_time_obd,
                  end_time_obd=end_time_obd,
                  create_date_obd=create_date_obd,
                  prev_test_date=prev_test_date,
                  emiss_test_type=emiss_test_type,
                  primary_emiss_test_code=primary_emiss_test_code,
                  bulb_check_res=bulb_check_res,
                  chk_eng_light_on_obd=chk_eng_light_on_obd,
                  indicator_light_result=indicator_light_result,
                  exempt_from_obd=exempt_from_obd,
                  obd_bypassed=obd_bypassed,
                  bypass_obd_allowed=bypass_obd_allowed,
                  obd2_connect_res=obd2_connect_res,
                  communic_res=communic_res,
                  obd=obd,
                  obd2_test_fl=obd2_test_fl,
                  pcm_mudule_id=pcm_mudule_id,
                  obd_module_id_2=obd_module_id_2,
                  obd_module_id_3=obd_module_id_3,
                  obd_type=obd_type,
                  obd_calid=obd_calid,
                  obd_cvn=obd_cvn,
                  cvn_exclusion=cvn_exclusion,
                  pid_count_obd=pid_count_obd,
                  obd_pid00_obd=obd_pid00_obd,
                  obd_pid20_obd=obd_pid20_obd,
                  obd_pid40_obd=obd_pid40_obd,
                  obd_rpm_obd=obd_rpm_obd,
                  rpm_exclusion=rpm_exclusion,
                  misfire_mon_res_obd=misfire_mon_res_obd,
                  fuel_sys_mon_res_obd=fuel_sys_mon_res_obd,
                  comp_cmpnt_res_obd=comp_cmpnt_res_obd,
                  catalyst_mon_res_obd=catalyst_mon_res_obd,
                  heat_cat_mon_res_obd=heat_cat_mon_res_obd,
                  evap_sys_mon_res_obd=evap_sys_mon_res_obd,
                  sec_air_sys_mon_res_obd=sec_air_sys_mon_res_obd,
                  air_cond_mon_res_obd=air_cond_mon_res_obd,
                  oxy_sens_mon_res_obd=oxy_sens_mon_res_obd,
                  htd_oxy_sns_mon_res_obd=htd_oxy_sns_mon_res_obd,
                  egr_sys_mon_res_obd=egr_sys_mon_res_obd,
                  rdy_mon_obd=rdy_mon_obd,
                  tot_unset_rdy_mon=tot_unset_rdy_mon,
                  readiness_status=readiness_status,
                  continuous_monit_xclusion=continuous_monit_xclusion,
                  exempt_from_readiness=exempt_from_readiness,
                  mil_command_stat=mil_command_stat,
                  dtc1_obd=dtc1_obd,
                  dtc2_obd=dtc2_obd,
                  dtc3_obd=dtc3_obd,
                  dtc4_obd=dtc4_obd,
                  dtc5_obd=dtc5_obd,
                  dtc6_obd=dtc6_obd,
                  dtc7_obd=dtc7_obd,
                  dtc8_obd=dtc8_obd,
                  dtc9_obd=dtc9_obd,
                  dtc10_obd=dtc10_obd,
                  tot_stored_dtcs_obd=tot_stored_dtcs_obd,
                  catalyst_dtc_pres_obd=catalyst_dtc_pres_obd,
                  pend_dtc1_obd=pend_dtc1_obd,
                  pend_dtc2_obd=pend_dtc2_obd,
                  pend_dtc3_obd=pend_dtc3_obd,
                  pend_dtc4_obd=pend_dtc4_obd,
                  pend_dtc5_obd=pend_dtc5_obd,
                  pend_dtc6_obd=pend_dtc6_obd,
                  pend_dtc7_obd=pend_dtc7_obd,
                  pend_dtc8_obd=pend_dtc8_obd,
                  pend_dtc9_obd=pend_dtc9_obd,
                  pend_dtc10_obd=pend_dtc10_obd,
                  cat_retest_exclusion=cat_retest_exclusion,
                  obd_warmups_obd=obd_warmups_obd,
                  obd_code_cleared_distance_obd=obd_code_cleared_distance_obd,
                  obd_mil_on_distance_obd=obd_mil_on_distance_obd,
                  obd_code_cleared_time_obd=obd_code_cleared_time_obd,
                  obd_mil_on_time_obd=obd_mil_on_time_obd,
                  emiss_clarification=emiss_clarification,
                  misc_comnt=misc_comnt,
                  misc_comnt_res=misc_comnt_res,
                  misc_emiss_reject_comment=misc_emiss_reject_comment,
                  misc_emiss_reject_result=misc_emiss_reject_result,
                  overall_tamper_result=overall_tamper_result,
                  ex_sys_res=ex_sys_res,
                  overall_obd2_res=overall_obd2_res,
                  exh_emiss_test_res=exh_emiss_test_res,
                  overall_gas_cap_res=overall_gas_cap_res,
                  ovr_exh_obd2_em_res=ovr_exh_obd2_em_res,
                  overall_emiss_res=overall_emiss_res,
                  overall_saf_res=overall_saf_res,
                  overall_test_res=overall_test_res,
                  created_date_sys=created_date_sys,
                  created_user_sys=created_user_sys,
                  update_date_sys=update_date_sys,
                  update_user_sys=update_user_sys)
    client.put(entity)
    c1_id = entity.id

    logging.info('EmCarsDailyRpt created {}'.format(c1_id))
    message = str('EmCarsDailyRpt for vin {} has been inserted with :{}'.format(vehicle_vin, c1_id))
    return message


@app.route('/', methods=['GET', 'POST'])
def index():
    message, client_id = insertClient()

    username = 'scotland.m@4-0analytics.com'
    password = generate_password_hash('Njit!7841')
    message1 = insertUserAuthInformation(username=username, password=password, client_id=client_id)
    message = '<br/>'.join([message, message1])

    username = '4.0analytics'
    password = generate_password_hash('4624@Njit')
    message1 = insertUserAuthInformation(username=username, password=password, client_id=client_id)
    message = '<br/>'.join([message, message1])

    username = 'sandbox'
    password = generate_password_hash('sandbox')
    message1 = insertUserAuthInformation(username=username, password=password, client_id=client_id)
    message = '<br/>'.join([message, message1])

    username = 'cowart.g@4-0analytics.com'
    password = generate_password_hash('Njit!7841')
    message1 = insertUserAuthInformation(username=username, password=password, client_id=client_id)
    message = '<br/>'.join([message, message1])

    username = 'admin'
    password = generate_password_hash('sandbox')
    message1 = insertUserAuthInformation(username=username, password=password, client_id=client_id)
    message = '<br/>'.join([message, message1])

    insurance_company = "All State"
    naic = "9999999"
    insurance_policy_number = "77777"
    insurance_expiry = datetime.now()
    message1 = insertInsuranceInformation(insurance_company=insurance_company,
                                          naic=naic,
                                          policy=insurance_policy_number,
                                          expiry=insurance_expiry,
                                          client_id=client_id
                                          )
    message = '<br/>'.join([message, message1])

    message1 = insertLastRunDate(last_run_date=datetime.now(), process_id="EM CARS-MOD2")
    message = '<br/>'.join([message, message1])

    sticker_info = "ECM"
    sticker_expiry = datetime.now()
    vehiclelist1 = [5521719611621370, 9041081035, 5, 354235052865381, "4.0 Analytics", "1J4GR48K15C713085",
                    "Y30KXC",
                    "2019-8-23", "JEEP", "Cherokee", 2005, "1111", 417118, "2021-01-30", "2019-8-23",
                    {'ConfigVersion': 'C4A.04A', 'FirmwareVersion': '6.54'}, "2019-8-23", False, "NULL",
                    "2014-08-10",
                    5699902705238010]
    vehiclelist2 = [5521719611621371, 8042061009, 5, 354235052865382, "4.0 Analytics", "JTHBJ46G482271076",
                    "KKC72H",
                    "06/01/2019", "Lexus", "350ES", 2008, "1111", 169812, "01/30/2021", "46/46/2958",
                    {'ConfigVersion': 'C4A.04A', 'FirmwareVersion': '6.54'}, "46/46/2958", False, "Mark Scotland",
                    "10/15/2015", 5747175027900416]
    vehiclelist3 = [5521719611621373, 9073081168, 5, 354235052865383, "4.0 Analytics", "1J4GR48K15C713085",
                    "Y30KXC",
                    "2019-8-23", "JEEP", "Cherokee", 2005, "1111", 417118, "2021-01-30", "2019-8-23",
                    {'ConfigVersion': 'C4A.04A', 'FirmwareVersion': '6.54'}, "2019-8-23", False, "NULL",
                    "2014-08-10",
                    5699902705238010]
    vehiclelist4 = [5521719611621374, 9073081169, 5, 354235052865384, "4.0 Analytics", "JTHBJ46G482271076",
                    "KKC72H",
                    "06/01/2019", "Lexus", "350ES", 2008, "1111", 169812, "01/30/2021", "46/46/2958",
                    {'ConfigVersion': 'C4A.04A', 'FirmwareVersion': '6.54'}, "46/46/2958", False, "Mark Scotland",
                    "10/15/2015", 5747175027900416]
    vehiclelist5 = [5521719611621375, 9073081186, 5, 354235052865385, "4.0 Analytics", "1J4GR48K15C713085",
                    "Y30KXC",
                    "2019-8-23", "JEEP", "Cherokee", 2005, "1111", 417118, "2021-01-30", "2019-8-23",
                    {'ConfigVersion': 'C4A.04A', 'FirmwareVersion': '6.54'}, "2019-8-23", False, "NULL",
                    "2014-08-10",
                    5699902705238010]
    vehiclelist6 = [5521719611621376, 9073081195, 5, 354235052865386, "4.0 Analytics", "JTHBJ46G482271076",
                    "KKC72H",
                    "06/01/2019", "Lexus", "350ES", 2008, "1111", 169812, "01/30/2021", "46/46/2958",
                    {'ConfigVersion': 'C4A.04A', 'FirmwareVersion': '6.54'}, "46/46/2958", False, "Mark Scotland",
                    "10/15/2015", 5747175027900416]
    vehiclelist7 = [5521719611621377, 9073081216, 5, 354235052865387, "4.0 Analytics", "JTHBJ46G482271076",
                    "KKC72H",
                    "06/01/2019", "Lexus", "350ES", 2008, "1111", 169812, "01/30/2021", "46/46/2958",
                    {'ConfigVersion': 'C4A.04A', 'FirmwareVersion': '6.54'}, "46/46/2958", False, "Mark Scotland",
                    "10/15/2015", 5747175027900416]

    vehicllist = [vehiclelist1, vehiclelist2, vehiclelist3, vehiclelist4, vehiclelist5, vehiclelist6, vehiclelist7]
    start_date = datetime.strptime('2016-07-31', '%Y-%m-%d')
    ecm_expiry_date = datetime.strptime('2017-07-30', '%Y-%m-%d')
    activity_date = datetime.strptime('2017-07-30', '%Y-%m-%d')
    latest_activity_date = datetime.strptime('2016-06-05', '%Y-%m-%d')
    date_added = datetime.strptime('2016-07-31', '%Y-%m-%d')
    for ftpx in range(1, 2):
        for vehicle in vehicllist:
            message1 = insertVehicleInformation(
                client_id=vehicle[0],
                ftp_id=vehicle[1],
                tenant_id=vehicle[2],
                imei=vehicle[3],
                department=vehicle[4],
                vin=vehicle[5],
                license_plate=vehicle[6],
                start_date=start_date,
                make=vehicle[8],
                model=vehicle[9],
                year=vehicle[10],
                vehicle_id=vehicle[11],
                odometer=vehicle[12],
                ecm_expiry_date=ecm_expiry_date,
                activity_date=activity_date,
                software=vehicle[15],
                latest_activity_date=latest_activity_date,
                tested=vehicle[17],
                comments=vehicle[18],
                date_added=date_added,
                user_id=vehicle[20]
            )
            message = '<br/>'.join([message, message1])

        message1 = insertStickerInformation(sticker=sticker_info,
                                            expiry=sticker_expiry,
                                            ftp_id=ftpx,
                                            client_id=client_id
                                            )
        message = '<br/>'.join([message, message1])

        for tstx in range(0, 10):
            message1 = insertEmCarsDailyRpt(
                res_sys_no_obd='GDX1727_354235052865387_190204144507',
                lic_st_id=None,
                ets_id=None,
                etnj2_sw_ver='',
                vin='',
                vin_src='',
                vehicle_vin='1FTBW2CM2HKB47373',
                vehicle_vin_src='1FTBW2CM2HKB47373',
                obd2_vin_obd='1FTBW2CM2HKB47373',
                vin_mask='',
                lic_no_obd='XGGM75',
                lic_jur_obd='NJ',
                lic_src='',
                model_yr_obd=2017,
                make_obd='British Leyland',
                model_obd='Land Rover Range Rover Evoque 2.0 TD4 E-Capability 4x4 HSE Dynamic',
                gvwr='',
                no_of_cyl=None,
                eng_size=None,
                trans_type='',
                fuel_cd='',
                vid_sys_no=None,
                curr_odo_rdng_obd=999999999,
                prev_odo_rdng_obd=999999999,
                mvc_reg_code='',
                mvc_vehicle_type_code='',
                test_type='',
                start_time_obd=datetime.now(),
                end_time_obd=datetime.now(),
                create_date_obd=datetime.now(),
                prev_test_date=datetime.now(),
                emiss_test_type='',
                primary_emiss_test_code='',
                bulb_check_res='',
                chk_eng_light_on_obd='P',
                indicator_light_result='',
                exempt_from_obd='',
                obd_bypassed='',
                bypass_obd_allowed='',
                obd2_connect_res='',
                communic_res='',
                obd='',
                obd2_test_fl='',
                pcm_mudule_id='',
                obd_module_id_2='',
                obd_module_id_3='',
                obd_type='',
                obd_calid='',
                obd_cvn=None,
                cvn_exclusion='',
                pid_count_obd=45,
                obd_pid00_obd='BFBEA897',
                obd_pid20_obd='8007B119',
                obd_pid40_obd='FED09001',
                obd_rpm_obd=1210,
                rpm_exclusion=None,
                misfire_mon_res_obd='R',
                fuel_sys_mon_res_obd='R',
                comp_cmpnt_res_obd='R',
                catalyst_mon_res_obd='R',
                heat_cat_mon_res_obd='U',
                evap_sys_mon_res_obd='R',
                sec_air_sys_mon_res_obd='U',
                air_cond_mon_res_obd='U',
                oxy_sens_mon_res_obd='R',
                htd_oxy_sns_mon_res_obd='R',
                egr_sys_mon_res_obd='R',
                rdy_mon_obd=1,
                tot_unset_rdy_mon=None,
                readiness_status='',
                continuous_monit_xclusion='',
                exempt_from_readiness='',
                mil_command_stat='',
                dtc1_obd='P9999',
                dtc2_obd='P9999',
                dtc3_obd='P9999',
                dtc4_obd='P9999',
                dtc5_obd='P9999',
                dtc6_obd='P9999',
                dtc7_obd='P9999',
                dtc8_obd='P9999',
                dtc9_obd='P9999',
                dtc10_obd='P9999',
                tot_stored_dtcs_obd=10,
                catalyst_dtc_pres_obd='N',
                pend_dtc1_obd='P9999',
                pend_dtc2_obd='P9999',
                pend_dtc3_obd='P9999',
                pend_dtc4_obd='P9999',
                pend_dtc5_obd='P9999',
                pend_dtc6_obd='P9999',
                pend_dtc7_obd='P9999',
                pend_dtc8_obd='P9999',
                pend_dtc9_obd='P9999',
                pend_dtc10_obd='P9999',
                cat_retest_exclusion='',
                obd_warmups_obd='255',
                obd_code_cleared_distance_obd='5508',
                obd_mil_on_distance_obd='0',
                obd_code_cleared_time_obd=datetime.now(),
                obd_mil_on_time_obd=datetime.now(),
                emiss_clarification='',
                misc_comnt='',
                misc_comnt_res='',
                misc_emiss_reject_comment='',
                misc_emiss_reject_result='',
                overall_tamper_result='',
                ex_sys_res='',
                overall_obd2_res='',
                exh_emiss_test_res='',
                overall_gas_cap_res='',
                ovr_exh_obd2_em_res='',
                overall_emiss_res='',
                overall_saf_res='',
                overall_test_res='',
                created_date_sys=datetime.now(),
                created_user_sys='999999999',
                update_date_sys=datetime.now(),
                update_user_sys='999999999'
            )
            message = '<br/>'.join([message, message1])
    return message


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if os.getenv('TESTING', '').startswith('yes'):
        app.run(port=8080, host="localhost", debug=True)  # localhost
    else:
        app.run(debug=True)  # production
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
