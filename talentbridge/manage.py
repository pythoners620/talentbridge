#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    import django
    from django.core.management import call_command, execute_from_command_line

    # Make sure the database tables exist before the dev server starts.
    if len(sys.argv) > 1 and sys.argv[1] == "runserver":
        django.setup()
        call_command("migrate", interactive=False, verbosity=1)
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
