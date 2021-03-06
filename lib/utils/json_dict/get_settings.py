from lib.utils.settings.settings import Settings
from lib.utils.json_dict.dict_json_consumer import load_json_file
from lib.utils.path.get_path import get_settings_path


# Função que carrega a configuração de modelo de execução do arquivo settings.json
def get_model_settings():
    settings = load_json_file(get_settings_path())
    Settings.execution_model = settings["execution_model"]


# Função que carrega a configuração de plataforma e desired capabilities do arquivo settings.json
def get_platform_settings():
    settings = load_json_file(get_settings_path())
    Settings.platform = settings["platform_settings"]["platform"]
    if Settings.platform in ("firefox", "chrome", "edge", "ie", "opera"):
        pass
    elif Settings.platform == "mobile":
        Settings.platform_name = settings["platform_settings"]["platform_name"]
        Settings.command_executor = settings["platform_settings"]["command_executor"]
        Settings.platform_version = settings["platform_settings"]["platform_version"]
        Settings.device_name = settings["platform_settings"]["device_name"]
        Settings.application_package = settings["platform_settings"]["application_package"]
        Settings.application_activity = settings["platform_settings"]["application_activity"]
        Settings.automation_name = settings["platform_settings"]["automation_name"]
        Settings.browser_name = settings["platform_settings"]["browser_name"]
        Settings.app = settings["platform_settings"]["app"]
        Settings.no_reset = settings["platform_settings"]["no_reset"]
        Settings.workspace_name = settings["platform_settings"]["workspace_name"]
        Settings.oauth_client_id = settings["platform_settings"]["oauth_client_id"]
        Settings.oauth_client_secret = settings["platform_settings"]["oauth_client_secret"]
        Settings.tenant_id = settings["platform_settings"]["tenant_id"]
        Settings.auto_grant_permissions = settings["platform_settings"]["auto_grant_permissions"]
        Settings.udid = settings["platform_settings"]["udid"]
    elif Settings.platform == "desktop":
        Settings.application_path = settings["platform_settings"]["application_path"]
    elif Settings.platform == "api":
        pass
    else:
        raise Exception('Plataforma configurada não suportada pela aplicação. Selecione uma plataforma válida!')


# Função que carrega a configuração de execução com ou sem interface gráfica do arquivo settings.json
def get_headless_settings():
    settings = load_json_file(get_settings_path())
    Settings.headless = settings["headless"]


# Função que carrega a configuração de execução do lint para o diretório de implementação dos testes
def get_lint_settings():
    settings = load_json_file(get_settings_path())
    Settings.lint = settings["lint"]
