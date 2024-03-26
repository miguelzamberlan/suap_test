from django.apps import apps

class AlunoPlusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Substituir a classe Aluno pelo AlunoPlus em todos os apps, exceto em 'alunoplus'
        for app_config in apps.get_app_configs():
            if app_config.name != 'alunoplus':
                try:
                    module = app_config.models_module
                    if module:
                        if hasattr(module, 'AlunoPlus'):
                            module.Aluno = module.AlunoPlus
                except ImportError:
                    pass

        response = self.get_response(request)
        return response
