# encoding: utf-8


class GitDirStatus(object):
    class Status:
        def __init__(self, path):
            self.path = path
            self.current_branch = ''
            self.is_clear = False
            self.has_changed = False
            self.local_branches = []

    def __init__(self, git_folders):
        self.map = {}
        for wd in git_folders:
            self.map[wd] = self.Status(wd)
