import configparser
import collections

if '__main__' == __name__:
    svnConfig = configparser.ConfigParser()
    svnConfig.read('svnaccess.apache')
    user_name_dict = collections.defaultdict(list) # key: user, value: list of str repository groups
    repository_group_dict = collections.defaultdict(list) # key: repository group, value: list of dist {repo:, permission:}
    for section in svnConfig.sections():
        print(section)
        for item_of_section in svnConfig.items(section):
            if 'groups' == section:
                repository_group_name = item_of_section[0]
                print(repository_group_name)
                for user in item_of_section[1].split(','):
                    user_name_dict[user].append(repository_group_name)
                    # in an other option: dict.setdefault(key,[]).append(value)
                    print(user, end=',')
                print()
            else:
                print(item_of_section[0].replace('@', ''))
                repository_group_dict[item_of_section[0].replace('@', '')].append({'repo': section, 'permission': item_of_section[1]})
    print(user_name_dict['cshuang'])
    print(repository_group_dict['g_admin'])
