import git
import os
import sys
import configparser

def list_submodules(repo_path, commit_sha=None):
    """
    List submodules for a specific commit or current HEAD
    Works for both bare and non-bare repositories

    Args:
        repo_path (str): Path to the git repository
        commit_sha (str, optional): Specific commit SHA to check submodules for
    """
    try:
        repo = git.Repo(repo_path)

        # Get the commit object (current HEAD or specified commit)
        if commit_sha:
            commit = repo.commit(commit_sha)
        else:
            commit = repo.head.commit

        # Get submodule information from the commit
        gitmodules_content = None

        try:
            # Try to get .gitmodules file content from the commit
            gitmodules_blob = commit.tree['.gitmodules']
            gitmodules_content = gitmodules_blob.data_stream.read().decode('utf-8')
        except (KeyError, AttributeError):
            # No .gitmodules file found at this commit
            print("No submodules found for this commit.")
            return

        # Parse the .gitmodules content
        submodule_data = {}

        config = configparser.ConfigParser()
        config.read_string(gitmodules_content)
        for section in config.sections():
            if section.startswith('submodule '):
                section_name = section[len('submodule '):].strip('"')
                submodule_data[section_name] = {
                    'path': config.get(section, 'path'),
                    'url':  config.get(section, 'url')
                }


        # Get the submodule commit SHAs
        for name, data in submodule_data.items():
            path = data['path']
            url = data['url']

            try:
                # Get the submodule commit using gitlink
                submodule_sha = commit.tree[path].hexsha

                print(f"Submodule {path}")
                print(f"{url}")
                print(f"{submodule_sha}")
                print()
            except KeyError:
                # This can happen if the submodule entry exists but isn't properly initialized
                print(f"Submodule {path}")
                print(f"{url}")
                print("Not initialized")
                print()

    except git.exc.InvalidGitRepositoryError:
        print(f"Error: '{repo_path}' is not a valid git repository")
    except git.exc.NoSuchPathError:
        print(f"Error: Path '{repo_path}' does not exist")
    except git.exc.GitCommandError as e:
        print(f"Git error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Default to current directory
    repo_path = "."
    commit_sha = None

    # Parse command line arguments
    if len(sys.argv) > 1:
        repo_path = sys.argv[1]
    if len(sys.argv) > 2:
        commit_sha = sys.argv[2]

    list_submodules(repo_path, commit_sha)

