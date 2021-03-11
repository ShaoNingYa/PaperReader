#!/usr/bin/env python3
# coding: utf-8

# Sort and Clean conference data.
# It writes to `sorted_data.yml` and `cleaned_data.yml`, copy those to the conference.yml after screening.

import yaml
import datetime
import sys
from shutil import copyfile
from builtins import input
import pytz

import pdb

try:
    # for python newer than 2.7
    from collections import OrderedDict
except ImportError:
    # use backport from pypi
    from ordereddict import OrderedDict

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from yaml.representer import SafeRepresenter

_mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG


def dict_representer(dumper, data):
    return dumper.represent_dict(data.iteritems())


def dict_constructor(loader, node):
    return OrderedDict(loader.construct_pairs(node))


Dumper.add_representer(OrderedDict, dict_representer)
Loader.add_constructor(_mapping_tag, dict_constructor)

Dumper.add_representer(str, SafeRepresenter.represent_str)


def ordered_dump(data, stream=None, Dumper=yaml.Dumper, **kwds):
    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())

    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)


dateformat = '%Y-%m-%d %H:%M:%S'
tba_words = ["tba", "tbd"]

right_now = datetime.datetime.utcnow().replace(
    microsecond=0).strftime(dateformat)


# Helper function for yes no questions
def query_yes_no(question, default="no"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def get_tag2name_dict(pre_path="", file_path="types.yml") -> dict:
    data_return = {}
    with open(pre_path + file_path, 'r') as stream:
        try:
            data = yaml.load(stream, Loader=Loader)
            for data_one in data:
                data_return[data_one['sub']] = data_one['name']
        except yaml.YAMLError as exc:
            print(exc)
    return data_return


# Sort:
def sort_data_and_save(file_path="./conferences/conferences.yml", save_to='sorted_data.yml'):
    with open(file_path, 'r') as stream:
        try:
            data = yaml.load(stream, Loader=Loader)
            conf = [x for x in data if x['deadline'].lower() not in tba_words]
            tba = [x for x in data if x['deadline'].lower() in tba_words]

            conf.sort(key=lambda x: pytz.utc.normalize(datetime.datetime.strptime(x['deadline'], dateformat).replace(
                tzinfo=pytz.timezone(x['timezone'].replace('UTC+', 'Etc/GMT-').replace('UTC-', 'Etc/GMT+')))))
            conf.sort(key=lambda x: pytz.utc.normalize(datetime.datetime.strptime(x['deadline'], dateformat).replace(
                tzinfo=pytz.timezone(x['timezone'].replace('UTC+', 'Etc/GMT-').replace('UTC-', 'Etc/GMT+')))).strftime(
                dateformat) < right_now)
            with open(save_to, 'w') as outfile:
                for line in ordered_dump(
                        conf + tba,
                        Dumper=yaml.SafeDumper,
                        default_flow_style=False,
                        explicit_start=True).splitlines():
                    outfile.write(line.replace('- title:', '\n- title:'))
                    outfile.write('\n')
        except yaml.YAMLError as exc:
            print(exc)


def remove_repeat(data):
    title = list(set([x['title'] + str(x['year']) for x in data]))  # 去重
    data_temp = []  # 去重
    for data_one in data:  # 去重
        if data_one['title'] + str(data_one['year']) in title:
            title.remove(data_one['title'] + str(data_one['year']))
            data_temp.append(data_one)
    return data_temp


def sort_data_and_save_files(base_path="./conferences/", save_to='sorted_data.yml'):
    import glob
    data = []
    for file_one in glob.glob(base_path + "*.yml"):
        with open(file_one, 'r', encoding="utf-8") as stream:
            try:
                data += yaml.load(stream, Loader=Loader)
            except yaml.YAMLError as exc:
                print(exc)
    print("共{}个".format(len(data)))
    data = remove_repeat(data)
    print("去重后，剩{}个".format(len(data)))
    try:
        conf = [x for x in data if x['deadline'].lower() not in tba_words]
        tba = [x for x in data if x['deadline'].lower() in tba_words]

        conf.sort(key=lambda x: pytz.utc.normalize(datetime.datetime.strptime(x['deadline'], dateformat).replace(
            tzinfo=pytz.timezone(x['timezone'].replace('UTC+', 'Etc/GMT-').replace('UTC-', 'Etc/GMT+')))))
        conf.sort(key=lambda x: pytz.utc.normalize(datetime.datetime.strptime(x['deadline'], dateformat).replace(
            tzinfo=pytz.timezone(x['timezone'].replace('UTC+', 'Etc/GMT-').replace('UTC-', 'Etc/GMT+')))).strftime(
            dateformat) < right_now)
        with open(save_to, 'w') as outfile:
            for line in ordered_dump(
                    conf + tba,
                    Dumper=yaml.SafeDumper,
                    default_flow_style=False,
                    explicit_start=True).splitlines():
                outfile.write(line.replace('- title:', '\n- title:'))
                outfile.write('\n')

    except yaml.YAMLError as exc:
        print(exc)


# with open(file_path, 'r') as stream:
#     try:
#         data = yaml.load(stream, Loader=Loader)
#         conf = [x for x in data if x['deadline'].lower() not in tba_words]
#         tba = [x for x in data if x['deadline'].lower() in tba_words]
#
#         conf.sort(key=lambda x: pytz.utc.normalize(datetime.datetime.strptime(x['deadline'], dateformat).replace(
#             tzinfo=pytz.timezone(x['timezone'].replace('UTC+', 'Etc/GMT-').replace('UTC-', 'Etc/GMT+')))))
#         conf.sort(key=lambda x: pytz.utc.normalize(datetime.datetime.strptime(x['deadline'], dateformat).replace(
#             tzinfo=pytz.timezone(x['timezone'].replace('UTC+', 'Etc/GMT-').replace('UTC-', 'Etc/GMT+')))).strftime(
#             dateformat) < right_now)
#         with open(save_to, 'w') as outfile:
#             for line in ordered_dump(
#                     conf + tba,
#                     Dumper=yaml.SafeDumper,
#                     default_flow_style=False,
#                     explicit_start=True).splitlines():
#                 outfile.write(line.replace('- title:', '\n- title:'))
#                 outfile.write('\n')
#     except yaml.YAMLError as exc:
#         print(exc)


def get_data(pre_path="", file_path='sorted_data.yml'):
    tag_dict = get_tag2name_dict(pre_path=pre_path)
    with open(pre_path + file_path, 'r') as stream:
        try:
            data = yaml.load(stream, Loader=Loader)
            data = [dict(data_one) for data_one in data]
            for data_one in data:
                if data_one['sub'] in tag_dict:
                    data_one['sub'] = tag_dict[data_one['sub']]
            return data
        except yaml.YAMLError as exc:
            print(exc)
    return []


if __name__ == '__main__':
    sort_data_and_save_files()
    # print(get_tag2name_dict())
