import configparser
import collections

if '__main__' == __name__:
    svnConfig = configparser.ConfigParser()
    svnConfig.read('svnaccess.apache')
    user_name_dict = collections.defaultdict(list)
    for section in svnConfig.sections():
        print(section)
        for item_of_section in svnConfig.items(section):
            if 'groups' == section:
                repository_group_name = item_of_section[0]
                print(repository_group_name)
                for user_list in item_of_section[1:]:
                    for user in user_list.split(','):
                        user_name_dict[user].append(repository_group_name)
                        # in an other option: dict.setdefault(key,[]).append(value)
                        print(user, end=',')
                print()
    print(user_name_dict['cshuang'])
