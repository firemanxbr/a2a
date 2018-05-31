#!/usr/bin/env python3
'''
Python Aggregator to Ansible Playbook
'''
import os
import shutil

from git import Repo, Git
from termcolor import colored

import fire
import ruamel.yaml


def parameter(file):
    ''' parameter file is mandatory to run a2a !!! '''
    try:
        data = ruamel.yaml.load(open(file), ruamel.yaml.RoundTripLoader)
        current_dir = '{0}{1}'.format(os.getcwd(), '/repositories/')

        for item in data:
            repo = None
            branch = None
            clone_dir = None

            if ('repo' in data[item] and len(data[item]['repo']) != 0):
                repo = data[item]['repo']
                clone_dir = '{0}{1}'.format(current_dir,
                                            data[item]['repo'].split('/')[-1].split('.')[0])

            if ('branch' in data[item] and len(data[item]['branch']) != 0):
                branch = data[item]['branch']

            if ('force_clone' in data[item] and data[item]['force_clone'] is True):
                shutil.rmtree(clone_dir, ignore_errors=True)

            if (not repo is None and not branch is None and not clone_dir is None):
                repo = Repo.clone_from(data[item]['repo'], clone_dir)
                repo.remotes.origin.fetch(data[item]['branch'])
                git_cmd = Git(clone_dir)
                git_cmd.checkout('FETCH_HEAD')

            print(colored("[A2A COMMAND ID: {0}]".format(item), 'green'))
            os.system(data[item]['command'])

    except Exception as error:
        print(colored("[ERROR] - {0}\n".format(error), 'red'))


def main():
    ''' Main function '''
    fire.Fire(parameter)


if __name__ == '__main__':
    main()
