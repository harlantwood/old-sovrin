#! /usr/bin/env python3

import os

from git import Repo, InvalidGitRepositoryError


def getDirInPath(dirName):
    cwd = os.getcwd()
    while True:
        parent, cur = os.path.split(cwd)
        if cur == dirName:
            return cwd
        if parent == cwd:
            raise RuntimeError("no {} dir in path".format(dirName))
        cwd = parent


def thisRepo():
    cwd = os.getcwd()
    while True:
        try:
            return Repo(cwd)
        except InvalidGitRepositoryError:
            precwd = cwd
            cwd = os.path.dirname(cwd)
            if precwd == cwd:
                raise RuntimeError("no git repo in path")


def main():
    repo = thisRepo()
    print('repo: {}'.format(repo))
    remote = repo.remotes['origin']
    remote
    edir = getDirInPath('evernym')
    print('evernym directory: {}'.format(edir))

if __name__ == '__main__':
    main()

# g = git.cmd.Git(git_dir)
# g.pull()

# GACTION=pull
#
# pushd ../sovrin-priv
# pwd
# git $GACTION
#
# cd ../plenum-priv
# pwd
# git $GACTION
#
# cd ../anoncreds-priv/
# pwd
# git $GACTION
#
# popd