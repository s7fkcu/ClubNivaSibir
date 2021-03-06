# -*- coding: utf-8 -*-

import os
def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('GladkiyVA', 'GladkiyVA@gmail.com'),
	('PoluninaOA', 'poa.webaspect@gmail.com'),
)
MANAGERS_FORUM_PARTNER = ['poa.webaspect@gmail.com', 'niva.sibir@yandex.ru',]


MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'club_niva_sibir',
		'USER': 'postgres',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}

TIME_ZONE = 'Asia/Novosibirsk'
LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = rel('media')
STATIC_ROOT = MEDIA_ROOT

MEDIA_URL = '/media/'
STATIC_URL = MEDIA_URL

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '#09vt1wob9o2g(z73n*q@25mxqi7$b9=j8ycuhsft3_ayh_iaf'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.gzip.GZipMiddleware',
	
	'my_flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'www.urls'

TEMPLATE_DIRS = (
	rel('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',

	# django 1.2 only
	'django.contrib.messages.context_processors.messages',

	# required by django-admin-tools
	'django.core.context_processors.request',
	
	'configuration.context_processors.custom_proc',
	'forum.context_processors.custom_proc',
	'user_msg.context_processors.custom_proc',
)

INSTALLED_APPS = (
	'tinymce',
	'filebrowser',
	
	'admin_tools',
	'admin_tools.theming',
	'admin_tools.menu',
	'admin_tools.dashboard',
	
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.sitemaps',
	
	
	'registration',

	'project',
	'my_flatpages',
	'banners',
	'news',
	'gallery',
	'yandex_map',
	'paginator',
	'configuration',
	'forum',
	'like',
	'userphoto',
	'partners',
	'user_msg',
	
	'perm',
	'cleaner',
	'django.contrib.markup',
	'markitup',

	'sorl.thumbnail',
	'captcha',
	'pymorphy',
	'admintrans',
	
	'django.contrib.comments',
)

CLEANER_APPS = (
	'banners',
	'news',
	'gallery',
	'userphoto',
)

APPS_PERM = {
	'auth': ['user', 'group', 'permission'],
	'sites': ['site'],
	#'menu': ['bookmark'],
	
	'my_flatpages': ['flat page'],
	'banners': ['banner'],
	'news': ['news_article'],
	'yandex_map': ['map'],
	'userphoto': ['user photo'],
	'gallery': ['gallery category', 'gallery photo'],
	'forum': ['Forum', 'Thread', 'Post', 'Subscription'],
}

AUTH_PROFILE_MODULE = 'project.UserProfile'

FORUM_BASE = '/forum'

NEWS_PAGINATE_BY = 10
GALLERY_PAGINATE_BY = 10
FORUM_PAGINATION = 100
USER_MSG_PAGINATION = 100

FORUM_MAIL_PREFIX = u'[Форум]'
JQUERY_URL = None

CACHE_BACKEND = 'db://cache_table?max_entries=100000'

ACCOUNT_ACTIVATION_DAYS = 2

AUTH_USER_EMAIL_UNIQUE = True
DEFAULT_FROM_EMAIL = 'tester@web-aspect.ru'
EMAIL_HOST = 'smtp.locum.ru'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'tester@web-aspect.ru'
EMAIL_HOST_PASSWORD = 'iostream'
EMAIL_USE_TLS = False

PYMORPHY_DICTS = {
	'ru': { 'dir': os.path.join(MEDIA_ROOT, 'morphy_ru') },
}

ADMIN_TOOLS_MENU = 'www.dashboard.CustomMenuDashboard'
ADMIN_TOOLS_INDEX_DASHBOARD = 'www.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'www.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_THEMING_CSS = 'admin_tools/css/theming_tomu.css'

TINYMCE_JS_URL = '/media/js/tiny_mce/tiny_mce_src.js'
TINYMCE_SPELLCHECKER=False
TINYMCE_PLUGINS = [
    'safari',
    'table',
    'advlink',
    'advimage',
    'iespell',
    'inlinepopups',
    'media',
    'searchreplace',
    'contextmenu',
    'paste',
    'wordcount'
]

TINYMCE_DEFAULT_CONFIG={
	'theme' : "advanced",
	'plugins' : ",".join(TINYMCE_PLUGINS),
	#'language' : 'ru',
	'theme_advanced_buttons1' : "undo,redo,|,bold,italic,underline,strikethrough,|,bullist,numlist,|,justifyleft,justifycenter,justifyright,justifyfull,fontselect,fontsizeselect,|,outdent,indent,blockquote,|,forecolor,backcolor",
	'theme_advanced_buttons2' : "table,|,delete_row,delete_table,|,row_after,row_before,|,cut,copy,paste,pastetext,pasteword,|,search,replace,|,link,unlink,|,link,unlink,anchor,image,media,|,cleanup,|,code",
	'theme_advanced_buttons3' : "",
	'theme_advanced_buttons4' : "",
	'theme_advanced_toolbar_location' : "top",
	'theme_advanced_toolbar_align' : "left",
	'theme_advanced_statusbar_location' : "bottom",
	'theme_advanced_resizing' : True,
	'table_default_cellpadding': 2,
	'table_default_cellspacing': 2,
	'cleanup_on_startup' : False,
	'cleanup' : False,
	'paste_auto_cleanup_on_paste' : False,
	'paste_block_drop' : False,
	'paste_remove_spans' : False,
	'paste_strip_class_attributes' : False,
	'paste_retain_style_properties' : "",
	'forced_root_block' : False,
	'force_br_newlines' : False,
	'force_p_newlines' : True,
	'remove_linebreaks' : False,
	'convert_newlines_to_brs' : False,
	'inline_styles' : False,
	'relative_urls' : False,
	'formats' : {
		'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
		'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
		'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
		'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
		'strikethrough' : {'inline' : 'del'},
		'italic' : {'inline' : 'em'},
		'bold' : {'inline' : 'strong'},
		'underline' : {'inline' : 'u'}
	},
	'pagebreak_separator' : "",
	'content_css' : MEDIA_URL + "css/text.css",
}

FILEBROWSER_DIRECTORY = 'upload/'
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_MEDIA_URL = MEDIA_URL
FILEBROWSER_URL_TINYMCE = MEDIA_URL + 'js/tiny_mce/'
FILEBROWSER_PATH_TINYMCE = os.path.join(MEDIA_ROOT, 'js', 'tiny_mce')

FILEBROWSER_MAX_UPLOAD_SIZE = 1048576000

FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm','swf'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p'],
    'Code': ['.html','.py','.js','.css']
}

FILEBROWSER_VERSIONS = {
    'fb_thumb': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (140px)', 'width': 140, 'height': '', 'opts': ''},
    'small': {'verbose_name': 'Small (300px)', 'width': 300, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (460px)', 'width': 460, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (620px)', 'width': 620, 'height': '', 'opts': ''},
    'cropped': {'verbose_name': 'Cropped (60x60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'croppedthumbnail': {'verbose_name': 'Cropped Thumbnail (140x140px)', 'width': 140, 'height': 140, 'opts': 'crop'},
}
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True, 'extensions': ['video']})

