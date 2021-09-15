import getopt
import os

root_dir = os.path.dirname(os.path.realpath(__file__))
service_dir = os.path.join(root_dir, "service")

requirements = []


def create_service_directory():
    if not os.path.exists(service_dir):
        os.mkdir(service_dir)
        log("Creating Service Directory at: " + service_dir, 4)


def build_requirements():
    """Build requirements.txt file for the service"""
    requirements_path = os.path.join(service_dir, "requirements.txt")
    if not os.path.exists(requirements_path):
        log("Creating requirements.txt file", 4)
    requirements_file = open(requirements_path, 'w')
    for requirement in requirements:
        if requirement[1] is None:
            requirements_file.write(requirement[0]+"\n")
        else:
            requirements_file.write(requirement[0]+" >= "+requirement[1])
    requirements_file.close()


def add_requirement(requirement, version=None):
    if requirement is not None:
        requirements.append((requirement, version))


def log(message, level=4):
    if log_level >= level:
        print(message)


if __name__ == "__main__":
    # change this to read from command line and default to 4
    log_level = 4
    create_service_directory()
    add_requirement("ariadne")
    build_requirements()
