from behave.__main__ import main as behave_main
import subprocess


def run_behave(tags=None, features=None, scenarios=None):
    command = ['behave']

    if tags:
        command.extend(['-k', tags])

    if features:
        command.extend(features)

    if scenarios:
        command.extend(scenarios)

    subprocess.run(command, check=True)


if __name__ == "__main__":
    # Specify the tags, features, or scenarios you want to run
    # Example: run_behave(tags='@smoke', features=['features/login.feature'])
    run_behave(tags='')

'''
tags = [] # define the tags you want to run
features = "login.feature" # which feature file you want to run


if __name__ == "__main__":
    args = []
    if tags:
        args.append("--tags=" + ",".join(tags))
    if features:
        args.append("features/"+features)
    args.append("--no-capture")
    behave_main(args)
'''
