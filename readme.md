# learnDjangoDocs

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```


### wepack config in django

#### npm init
#### npm install -D webpack webpack-cli
#### npm install -D webpack-dev-server
##### create assets a la racine du projet
##### create webpack.config.js dans le meme endroit que package.json
```
const path = require('path');
module.exports = {
    entry: './assets/scripts/index.js'
    output: {
        'path': path.resolve(__dirname, 'core', 'static'),
        'filename': 'bundle.js'
    }
};
```

#### dans package.json ajout save-dev
``` "scripts": {
    "dev": "webpack --watch --mode development",
    "build": "webpack --mode production"
  }
```

#### dans settings.py
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'core', 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### dans core/urls.py
```
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
```
