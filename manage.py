#!/usr/bin/env python
"""Utilitário de linha de comando do Django para tarefas administrativas."""
import os
import sys


def main():
    """Executa tarefas administrativas."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Você ativou o ambiente "
            "virtual (venv) e instalou as dependências (pip install -r "
            "requirements.txt)?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
