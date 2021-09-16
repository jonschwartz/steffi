import argparse
import os

root_dir = os.path.dirname(os.path.realpath(__file__))
service_dir = os.path.join(root_dir, "service")

requirements = []


def create_service_directory() -> None:
    if not os.path.exists(service_dir):
        os.mkdir(service_dir)
        info("Creating Service Directory at: " + service_dir)


def build_requirements() -> None:
    """Build requirements.txt file for the service"""
    requirements_path = os.path.join(service_dir, "requirements.txt")
    if not os.path.exists(requirements_path):
        info("Creating requirements.txt file")
    requirements_file = open(requirements_path, 'w')
    for requirement in requirements:
        if requirement[1] is None:
            requirements_file.write(requirement[0]+"\n")
        else:
            requirements_file.write(requirement[0]+" >= "+requirement[1])
    requirements_file.close()


def add_requirement(requirement, version=None) -> None:
    if requirement is not None:
        requirements.append((requirement, version))


def info(message) -> None:
    log(message, 4)


def warn(message) -> None:
    log(message, 3)


def error(message) -> None:
    log(message, 2)


def log(message, level=4) -> None:
    if log_level >= level:
        print(message)


if __name__ == "__main__":
    # change this to read from command line and default to 4

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l', '--log-level', dest="loglevel", help="Set the log level. 4(default) print everything, 3 print warnings and errors, 2 print errors, 1 print nothing", default=4, type=int, choices=[1, 2, 3, 4])
    args = parser.parse_args()
    log_level = args.loglevel
    print(args)
    print(log_level)
    create_service_directory()
    add_requirement("ariadne")
    build_requirements()
