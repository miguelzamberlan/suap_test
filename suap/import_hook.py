# # my_import_hook.py
# import sys
# from importlib.abc import MetaPathFinder
# from importlib.util import spec_from_loader


# class MyImportHook(MetaPathFinder):
#     def find_spec(self, fullname, path, target=None):
#         print(f"Verificando se o módulo {fullname} está disponível")
#         if fullname == 'aluno.models':
#             # Interceptando apenas se estiver importando de aluno.models
#             return self
#         return None

#     def loader(self, fullname):
#         class AlunoLoader:
#             def exec_module(self, module):
#                 # Substituindo Aluno por Aluno dentro do módulo
#                 from implements.models import Aluno
#                 module.Aluno = Aluno

#         return AlunoLoader()

#     @staticmethod
#     def install():
#         sys.meta_path.append(MyImportHook())
