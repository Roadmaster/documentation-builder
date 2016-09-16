# Core modules
import argparse
from tempfile import TemporaryDirectory
from os.path import join

# Third party modules
from git import Repo

# Local modules
from .mdbuild import build


def parse_arguments():
    """
    Parse command-line options for documentation-parser command-line script
    """

    parser = argparse.ArgumentParser(
        description=(
            "A tool to build documentation HTML files from markdown files "
            "stored in a repository somewhere"
        )
    )

    parser.add_argument(
        '--source-repository',
        required=True, help="Git repository URL for retrieving markdown files."
    )
    parser.add_argument(
        '--files-path',
        default="src", help="Where to look for files within the repository."
    )
    parser.add_argument(
        '--destination-folder',
        default=".", help="A folder for the compiled HTML files"
    )

    return parser.parse_args()


def main():
    """
    The starting point for the documentation-parser.
    Intended to be run through the command-line.
    """

    arguments = parse_arguments()

    with TemporaryDirectory(prefix='/dev/shm/') as temp_source_folder:
        Repo.clone_from(arguments.source_repository, temp_source_folder)

        build(
            source=join(temp_source_folder, arguments.files_path.strip('/')),
            outpath=arguments.destination_folder
        )


if __name__ == "__main__":
    main()