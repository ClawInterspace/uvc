# What's is uvc?

A command line adapter for operating multiple git repositories. 
This tool will parse all git repos under specified root path at first, 
and then operate commands to all of these repos.


# Installaion

```
py -m pip install git+https://github.com/ClawInterspace/uvc.git@master#egg=uvc
```

# Command Usage

See the usage from help doc:

`python -m uvc.main --help`

## Fire

This command group will issue the original command to all git repos.

* Issue a command to all repos

```
python -m uvc.main -r "D:\workspace\project-expr" fire git status -h
```


## Git
This command group will issue a customized command to all git repos.

* Update a branch to all repos:

```
python -m uvc.main -r "D:\workspace\project-expr" git update develop
```

* Extract all diff jira issues

```
python -m uvc.main -r "D:\workspace\project-tis" git diff-msgs -t 1.2rc9 1.2rc12 -re "(?i)CTIS\-\d+"  -o jira 
```

* Extract all diff jira issues without output

```
python -m uvc.main -r "D:\workspace\project-tis" --no-trace-command git diff-msgs -t 1.2rc9 1.2rc12 -re "(?i)CTIS\-\d+"  -o jira 
```