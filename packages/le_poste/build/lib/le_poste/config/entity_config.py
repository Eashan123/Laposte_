# fearures:

from le_poste.config import config
from le_poste import __version__ as _version

FEATURES = ['Résumé', 'Descriptif']

DROP_FEATURES = ['Résumé', 'Descriptif']

FEATURES_ORDER = ['Résumé', 'Descriptif', 'SubCat Translated', 'Application', 'Module', 'Rfc', 'Environment', 'Version']


# parameters
name = f"{config.ENTITY_SAVE_FILE}{_version}.xlsx"
path = config.DATASET_DIR / config.ENTITY_FILE
path_s = config.ENTITY_DIR


### pre-processing

exp1 = r'\d{2}/\d{2}/\d{4}'
exp2 = r'\d{2}:\d{2}:\d{2}'
exp3 = r"[A-Za-z0-9]+[\.'\-]*[a-z0-9]+@(laposte|googlemail)\.(com|fr)$"
exp4 = r'[=>|?|$|!|\-|#|*|&|/|%|,|"|:|;|*|@|#|\[|\]|\(|\)|\n|\\t|\xa0|\\n]'
exp5 = r"{color d0\d{4}}"
exp6 = r"{color \d{6}}"
exp7 = r"{color}|{code}|{code java}|tag|s"
spaces = r"\s+"
space = " "
subb = r" "
subb_ = r''

### application:

app1 = '([a-zA-Z]{1}[a-zA-Z0-9]{1}_)([Uu]{1}[a-z0-9A-Z]{1}(?!\w))'
app2 = '[a-zA-Z]{1}[a-zA-Z0-9]{1}_(?!\w)'

### module

mod1 = '\s[uU]{1}[a-zA-Z0-9]{1}(?!\w)'
mod2 = '(\s[a-zA-Z]{1}[a-zA-Z0-9]{1}_)([Uu]{1}[a-zA-Z0-9]{1}(?!\w))'
mod3 = "(\s[a-zA-Z]{1}[0-9a-zA-Z]{1})\s([a-zA-Z0-9]{1,3}[_|.]{1}\d{2}[_|.]{1}\d{2}[.]{1}\d{3})"
mod4 = "\s([a-zA-Z]{1}[a-zA-Z0-9]{1}[_]{1})([a-zA-Z]{1}[a-zA-Z0-9]{1})\s([a-zA-Z0-9]{1,3}[_|.]{1}\d{2}[_|.]{1}\d{1,2}[.]{1}\d{1,3}|[_]{1}[a-zA-Z0-9]{2,4})"

nan = 'None'

### rfc

rfc = '[cC]{1}\d{6,10}(?!\w)'

### version

ver1 = '[vV]{1}\d{2}_\d{2}_\d{2}.{1}\d{3}_[IT]{2}\d{1,2}'
ver2 = '[vV]{1}\d{2}_\d{2}_\d{2}.{1}\d{3}'
ver3 = "\s[a-zA-Z0-9]{1,2}[_|.]{1}\d{2}[_|.]{1}\d{2}[.]{1}\d{3}"

# look up

mod_lk = [' ur']


env_lk = ['PRODUCTION', 'PREPROD', 'QUALIF', 'RECETTE', 'REFPROD', 
                   'pre-production', 'PROD', 'PPRD', 'recette', 'REC', 'prod', 'production',
                    'preprod', 'qualif', 'refprod', 'rec', 'pprd']

## column names:

app = "Application"
mod = "Module"
ver = "Version"
rf = "Rfc"
env = "Environment"