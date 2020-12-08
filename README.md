# uvc

A command line adapter for operating multiple git repositories.

# Install

```
py -m pip install git+https://github.com/ClawInterspace/uvc.git@master#egg=uvc
```

# Command Examples

* Issue a command to all repos:

```
python -m uvc.main -r "D:\workspace\project-expr" fire git status -h
```

* Update a branch to all repos:

```
python -m uvc.main -r "D:\workspace\project-expr" git update develop
```

* Extract all diff jira issues

```
python -m uvc.main -r "D:\workspace\project-tis" git diff-msgs -t 1.2rc9 1.2rc12 -re "(?i)CTIS\-\d+"  -o jira 
```