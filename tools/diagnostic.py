"""Python module to diagnose possible missed installations or plugins on students computers..

Usage:

    python -m tools.diagnostic
"""

import colorama
import sys
import subprocess
import shutil


__author__ = "Ezri White <ezri@live.unc.edu>"


colorama.init()  # Color for windows!


class Check_Result:
    """Contains information on status of a run test."""

    def __init__(self, test_name):
        """Set's up properties of a test result object."""
        self.test_name = test_name
        self.description = ""
        self.status = False
        self.fail_messages = []
        self.success_messages = []
        self.error_codes = []


class bcolors:
    """Colors for printing."""
    HEADER = '\033[96m'
    ITALIC = '\033[3m'
    PASS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = "\033[91m"
    ECODE = '\033[95m'
    END = '\033[0m'
    BOLD = '\033[1m'
    BLINK = '\033[5m'
    UNDERLINE = '\033[4m'


def main() -> None:
    """Entry point of script. Expects to be run as CLI program."""
    mod: str = verbose()
    test_results = [test_python_in_path(), test_version(), test_pytest(), test_requirements(), test_git_in_PATH()]
    if test_results[4].status:
        test_results.append(test_git_config())
        test_results.append(test_git_upstream())
    else:
        test_results.append(test_not_run("Git Configuration Test",
                                         "Check for the existence of git author and email configuration.",
                                         "Git in Path test failed so test not run."))
        test_results.append(test_not_run("Git Upstream Test",
                                         "Check for git upstream repo set to the correct place.",
                                         "Git in Path test failed so test not run."))
    print("\n")
    all_passed = True
    for test in test_results:
        if not test.status or (mod == "--verbose"):
            print(wrap(bcolors.HEADER, "========== " + test.test_name + " =========="))
            print(wrap(bcolors.ITALIC, test.description))
            print(wrap(bcolors.UNDERLINE, "Status") + ": " + ((wrap(bcolors.PASS, "Passed"))
                                                              if test.status else (wrap(bcolors.FAIL, "Failed"))))
            for message in test.success_messages:
                print(message)
            for message in test.fail_messages:
                print(wrap(bcolors.WARNING, message))
            print("\n")
            all_passed = False
    if all_passed:
        print(wrap(bcolors.PASS, "========== All Tests Passed ==========\n"))
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(bcolors.ECODE + "The following diagnostic codes were raised:\n")
        for test in test_results:
            for code in test.error_codes:
                print(code)
        print("\nFor information on how to fix: https://20f.comp110.com/diagnostics.html" + bcolors.END)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def wrap(code, text) -> str:
    """Wraps input string with format literal."""
    return code + text + bcolors.END


def test_python_in_path() -> Check_Result:
    """Test for python versions in path and what python vs python3 commands output."""
    python_in_path_test = Check_Result("Python in Path test")
    python_in_path_test.description = "Checks what versions and binaries of python are present in PATH."
    python_paths = search_path(python="python", python3="python3")
    python_test, python3_test = python_paths[0], python_paths[1]
    if python_test is not None: 
        python_in_path_test.success_messages.append("Python Path: " + python_test)
    if python3_test is not None:
        python_in_path_test.success_messages.append("Python3 Path: " + python3_test)
    try:
        python_version = str(subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT))
        if "win" not in sys.platform:
            python_in_path_test.success_messages.append("Python Version: " + python_version[2:-3])
        else:
            python_in_path_test.success_messages.append("Python Version: " + python_version[2:-5])
        if ("Python 3.8" in python_version):
            python_in_path_test.status = True 
        else:
            python_in_path_test.fail_messages.append("Python interpreter is lower than 3.8.")
            python_in_path_test.error_codes.append("S102 - python command runs a version less than 3.8 ")
    except Exception:
        python_version = ""
        python_in_path_test.fail_messages.append("Python not installed.")
        python_in_path_test.error_codes.append("S101 - Python is not installed")
    return python_in_path_test


def test_version() -> Check_Result:
    """Test version of interpreter being run from vscode."""
    version_test = Check_Result("Python Interpreter Test")
    version_test.description = "Python version of interpreter that is being run in the workspace."
    version = sys.version[:3]
    if float(version) < 3.8:
        version_test.fail_messages.append("Python interpreter: " + version)
        version_test.fail_messages.append("Python interpreter used in workspace is lower than 3.8.")
        version_test.error_codes.append("S103 - Python version being run in vscode is lower than 3.8")
    else:
        version_test.success_messages.append("Python interpreter: " + version)
        version_test.status = True 

    return version_test


def test_requirements() -> Check_Result:
    """Test for packages intalled from requirements.txt."""
    requirements_test = Check_Result("Installed Packages Test")
    requirements_test.description = "Check for all packages in requirements.txt installed with pip"
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0].lower() for r in reqs.split()]

    with open('requirements.txt', 'r') as file:
        lines = file.readlines()
    required_packages = []
    for line in lines:
        if line[0].isalpha():
            required_packages.append(line.split('\n')[0].lower())

    missing_packages = True
    for package in required_packages:
        if package not in installed_packages:
            requirements_test.fail_messages.append("Missing: " + package)
            requirements_test.error_codes.append("S301 - Missing Required Packages")
            missing_packages = False
        else:
            requirements_test.success_messages.append("Installed: " + package)
    requirements_test.status = missing_packages

    return requirements_test


def test_git_in_PATH() -> Check_Result:
    """Test for the existence of git in the PATH."""
    git_path_test = Check_Result("Git on Path Test")
    git_path_test.description = "Check for the existence of git in the PATH."
    try:
        git_version = subprocess.check_output(["git", "--version"], stderr=subprocess.STDOUT)
        git_path_test.success_messages.append(str(git_version)[2:20].capitalize())
        git_path_test.status = True
    except Exception:
        git_path_test.fail_messages.append("Git could not be found.")
        git_path_test.error_codes.append("S201 - Git is not installed or not on path")
        git_path_test.status = False
    return git_path_test


def test_git_config() -> Check_Result:
    """Test for the existence of git author and email configuration."""
    git_config_test = Check_Result("Git Configuration Test")
    git_config_test.description = "Check for the existence of git author and email configuration."
    try:
        user_name = subprocess.check_output(["git", "config", "user.name"], stderr=subprocess.STDOUT)
        email = subprocess.check_output(["git", "config", "user.email"], stderr=subprocess.STDOUT)
        git_config_test.success_messages.append("User Name: " + str(user_name)[2:-3])
        git_config_test.success_messages.append("Email: " + str(email)[2:-3])
        git_config_test.status = True if '@' in str(email) else False
    except Exception:
        git_config_test.fail_messages.append("User Name: User name was not found.")
        git_config_test.fail_messages.append("Email: Email was not found")
        git_config_test.error_codes.append("S202 - Email and Username not configured")

    return git_config_test


def test_git_upstream() -> Check_Result:
    """Test for git upstream repo set to the correct place."""
    git_upstream_test = Check_Result("Git Upstream Test")
    git_upstream_test.description = "Check for git upstream repo set to the correct place."
    try:
        upstream = str(subprocess.check_output(["git", "remote", "get-url", "upstream"], stderr=subprocess.STDOUT))
        git_upstream_test.success_messages.append("Upstream: " + upstream[2:-3])
        if 'https://github.com/comp110-20f/course-material.git' in upstream:
            git_upstream_test.status = True
        else:
            git_upstream_test.status = False
            git_upstream_test.fail_messages.append("Upstream did not match course upstream")
            git_upstream_test.error_codes.append("S204 - Incorrect Upstream found")

    except Exception:
        upstream = "Upstream not found."
        git_upstream_test.fail_messages.append("Upstream: " + upstream)
        git_upstream_test.error_codes.append("S203 - No Upstream found")

    git_upstream_test.status = True if 'https://github.com/comp110-20f/course-material.git' in upstream else False
    return git_upstream_test


def test_pytest() -> Check_Result:
    """Test for errors finding pytests."""
    pytest_test = Check_Result("Pytest Test")
    pytest_test.description = "Test for errors finding pytests."
    try:
        collect_messages = str(subprocess.check_output(
            ["python", "-m", "pytest", "--collect-only", "."], stderr=subprocess.STDOUT))
        if 'error' not in collect_messages:
            pytest_test.status = True
    except Exception:
        pytest_test.status = False
        pytest_test.fail_messages.append(
            "Test collection threw an exception, most likely syntax errors in workspace.")
    return pytest_test


def test_not_run(test_name, description, message) -> Check_Result:
    """Create test result object for test not run."""
    test = Check_Result(test_name)
    test.description = description
    test.fail_messages.append(message)
    return test


def search_path(**kwargs) -> list:
    """Searches PATH for given executable strings.
    
    Returns the list of executable paths; returns None if no path found.
    """
    matches = []
    for key, val in kwargs.items():
        match = shutil.which(val)
        matches.append(match)
    return matches
    

def verbose() -> str:
    """Check for verbose mode."""
    if len(sys.argv) > 2:
        print("Usage: python -m tools.diagnostic [--verbose]")
        sys.exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--verbose":
            return "--verbose"
        else:
            print("Usage: python -m tools.diagnostic [--verbose]")
            sys.exit(1)
    else:
        return "quiet"


if __name__ == "__main__":
    main()