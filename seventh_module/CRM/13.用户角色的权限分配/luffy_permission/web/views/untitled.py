DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'django',
		'USER': 'root',
		'PASSWORD': '123456',
		'HOST': '127.0.0.1',
		'PORT': 3306,
		'OPTIONS':{
			'init_command':'SET default_storage_engine=INNODB;',
		}
	}
}

