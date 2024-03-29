def main():
    # imports
    import os
    import subprocess

    # path to top of rep dir
    repoPath = "./.."
    repoPath = os.path.abspath(os.path.join(os.path.dirname(__file__), repoPath))

    # running python tests
    coms = [
        f'cd "{repoPath}"',
        "python3 -m pytest -p no:warnings -vv --cov --cov-report term-missing",
    ]
    coms = "&& ".join(coms)
    subprocess.run(coms, shell=True, capture_output=False)


if __name__ == "__main__":
    main()
