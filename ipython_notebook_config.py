# Configuration file for ipython-notebook.

c = get_config()

#------------------------------------------------------------------------------
# NotebookApp configuration
#------------------------------------------------------------------------------

# NotebookApp will inherit config from: BaseIPythonApplication, Application

# The date format used by logging formatters for %(asctime)s
# c.NotebookApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# extra paths to look for Javascript notebook extensions
# c.NotebookApp.extra_nbextensions_path = []

# The base URL for the notebook server.
# 
# Leading and trailing slashes can be omitted, and will automatically be added.
# c.NotebookApp.base_url = '/'

# DEPRECATED, use tornado_settings
# c.NotebookApp.webapp_settings = {}

# The default URL to redirect to from `/`
# c.NotebookApp.default_url = '/tree'

# The login handler class to use.
# c.NotebookApp.login_handler_class = <class 'IPython.html.auth.login.LoginHandler'>

# The logout handler clIPython.kernel.kernelspec.KernelSpecManager'>

# The IPython profile to use.
# c.NotebookApp.profile = 'default'

# The port the notebook server will listen on.
# c.NotebookApp.port = 8888

# Path to an extra config file to load.
# 
# If specified, load this config file in addition to any other IPython config.
# c.NotebookApp.extra_config_file = ''

# Set the Access-Control-Allow-Credentials: true header
# c.NotebookApp.allow_credentials = False

# The directory to use for notebooks and kernels.
# c.NotebookApp.notebook_dir = ''

# 
# c.NotebookApp.file_to_run = ''

# Hashed password to use for web authentication.
# 
# To generate, type in a python/IPython shell:
# 
#   from IPython.lib import passwd; passwd()
# 
# The string should be of the form type:salt:hashed-password.
# c.NotebookApp.password = ''

# Set the log level by value or name.
# c.NotebookApp.log_level = 30

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default isotebookApp.jinja_environment_options = {}

#------------------------------------------------------------------------------
# KernelManager configuration
#------------------------------------------------------------------------------

# Manages a single kernel in a subprocess on this host.
# 
# This version starts kernels with Popen.

# KernelManager will inherit config from: ConnectionFileMixin

# Should we autorestart the kernel if it dies.
# c.KernelManager.autorestart = False

# DEPRECATED: Use kernel_name instead.
# 
# The Popen Command to launch the kernel. Override this if you have a custom
# kernel. If kernel_cmd is specified in a configuration file, IPython does not
# pass any arguments to the kernel, because it cannot make any assumptions about
# the  arguments that the kernel understands. In particular, this means that the
# kernel does not receive the option --debug if it given on the IPython command
# line.
# c.KernelManager.kernel_cmd = []

# set the heartbeat port [defaulD of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# The maximum number of digests to remember.
# 
# The digest history will be culled when it exceeds this value.
# c.Session.digest_history_size = 65536

# Threshold (in bytes) beyond which an object's buffer should be extracted to
# avoid pickling.
# c.Session.buffer_threshold = 1024

# The UUID identifying this session.
# c.Session.session = ''

# Metadata dictionary, which serves as the default top-level metadata dict for
# each message.
# c.Session.metadata = {}

# The digest scheme used to construct the message signatures. Must have the form
# 'hmac-HASH'.
# c.Session.sigcalled on a contents model prior to save.
# 
# This can be used to process the structure, such as removing notebook outputs
# or other side effects that should not be saved.
# 
# It will be called as (all arguments passed by keyword)::
# 
#     hook(path=path, model=model, contents_manager=self)
# 
# - model: the model to be saved. Includes file contents.
#   Modifying this dict will affect the file that is stored.
# - path: the API path of the save destination
# - contents_manager: this ContentsManager instance
# c.ContentsManager.pre_save_hook = None

#------------------------------------------------------------------------------
# FileContentsManager configuration
#------------------------------------------------------------------------------

# FileContentsManager will inherit config from: ContentsManager

# 
# c.FileContentsManager.checkpoints = None

# DEPRECATED, use post_save_hook
# c.FileContentsManager.save_script = False

# c.KernelSpecManager.whitelist = set()
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.ip = '*' # ローカルホスト以外からもアクセス可能にする
c.NotebookApp.open_browser = False # ブラウザが自動で開かないようにする
c.NotebookApp.port = 3001 # サーバーのポートを指定する  security groupも合わせて設定
