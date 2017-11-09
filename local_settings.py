# -*- coding: utf-8 -*-
import os
import geonode

# Setting debug to true makes Django serve static media and
# present pretty error pages.
DEBUG = TEMPLATE_DEBUG = False

# Set to True to load non-minified versions of (static) client dependencies
# Requires to set-up Node and tools that are required for static development 
# otherwise it will raise errors for the missing non-minified dependencies
DEBUG_STATIC = False

SITENAME = 'GeoNode'
SITEURL = 'http://10.75.19.229/'

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'geonode'
DATABASE_USER = 'geonode'
DATABASE_PASSWORD = 'yJi7HiQT'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    },
    'datastore': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geonode_data',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

GEOSERVER_URL = SITEURL + 'geoserver/'

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost:8080/geoserver/',
        'PUBLIC_LOCATION' : GEOSERVER_URL,
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : True,
        'LOG_FILE':'/usr/share/geoserver/data/logs/geoserver.log',
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
    }
}

LANGUAGE_CODE = 'en'

MEDIA_ROOT = '/var/www/geonode/uploaded'
STATIC_ROOT = '/var/www/geonode/static/'

# secret key used in hashing, should be a long, unique string for each
# site.  See http://docs.djangoproject.com/en/1.2/ref/settings/#secret-key
SECRET_KEY = '97ZDVKBbyVrAm9wjxZ'


CATALOGUE = {
    'default': {
        # The underlying CSW backend
        # ("pycsw_http", "pycsw_local", "geonetwork", "deegree")
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

# A Google Maps API key is needed for the 3D Google Earth view of maps
# See http://code.google.com/apis/maps/signup.html
GOOGLE_API_KEY = ''

GEONODE_ROOT = os.path.dirname(geonode.__file__)

TEMPLATE_DIRS = (
    '/etc/geonode/templates',
    os.path.join(GEONODE_ROOT, 'templates'),
)

# Additional directories which hold static files
STATICFILES_DIRS = [
    '/etc/geonode/media',
    os.path.join(GEONODE_ROOT, 'static'),
]

#REGISTRATION_OPEN = False
#ACCOUNT_APPROVAL_REQUIRED = False

#ACCOUNT_EMAIL_CONFIRMATION_EMAIL = False
#ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False

# Allowed values for the preview library are 'geoext' and 'leaflet'.
#LAYER_PREVIEW_LIBRARY = 'geoext'

# Uncomment the following to receive emails whenever there are errors in GeoNode
# or to be notified of new user requests when ACCOUNT_APPROVAL_REQUIRED has been set.
#ADMINS = (
#            ('John', 'john@example.com'), 
#         )

# Uncomment the following to use a Gmail account as the email backend
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'youremail@gmail.com'
#EMAIL_HOST_PASSWORD = 'yourpassword'
#EMAIL_PORT = 587

# For more information on available settings please consult the Django docs at
# https://docs.djangoproject.com/en/dev/ref/settings
ALLOWED_HOSTS=['localhost', '10.75.19.229', ]
SILENCED_SYSTEM_CHECKS = ['1_8.W001', 'fields.W340']

# GeoNode javascript client configuration

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (0, 0)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 0

ALT_OSM_BASEMAPS = os.environ.get('ALT_OSM_BASEMAPS', False)
CARTODB_BASEMAPS = os.environ.get('CARTODB_BASEMAPS', False)
STAMEN_BASEMAPS = os.environ.get('STAMEN_BASEMAPS', False)
THUNDERFOREST_BASEMAPS = os.environ.get('THUNDERFOREST_BASEMAPS', False)
MAPBOX_ACCESS_TOKEN = os.environ.get('MAPBOX_ACCESS_TOKEN', None)
BING_API_KEY = os.environ.get("Ahm2kLnjjfvga2m2G4Yho_nOv_tvZXYGk23QT90casDbdkwC6M1IU0Yhr9Ja-O4t", None)
GOOGLE_API_KEY = os.environ.get("AIzaSyDCaNAA5TF7diidvKFjkhHmntBoqZqJDUI", None)

MAP_BASELAYERS = [{
    "source": {"ptype": "gxp_olsource"},
    "type": "OpenLayers.Layer",
    "args": ["No background"],
    "name": "background",
    "visibility": False,
    "fixed": True,
    "group":"background"
}, {
    "source": {"ptype": "gxp_osmsource"},
    "type": "OpenLayers.Layer.OSM",
    "name": "mapnik",
    "visibility": True,
    "fixed": True,
    "group": "background"
},{
     "source": {
     "ptype":"gxp_googlesource",
     "apiKey": GOOGLE_API_KEY
          },
     "group":"background",
     "name":"SATELLITE",
     "visibility": False,
     "fixed": True,
},{
     "source": {
     "ptype":"gxp_bingsource",
     "apiKey": BING_API_KEY
          },
     "group":"background",
     "name":"Aerial",
     "visibility": False,
     "fixed": True,

}]
