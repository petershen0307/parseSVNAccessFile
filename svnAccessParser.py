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
    user_repo_permission_dict = {}
    for user in user_name_dict:
        permission_repositories = collections.defaultdict(set) # should use set struct
        for repo_group in user_name_dict[user]:
            for repo_permission_pair in repository_group_dict[repo_group]:
                permission_repositories[repo_permission_pair['permission']].add(repo_permission_pair['repo'])
        user_repo_permission_dict[user] = permission_repositories
    print(user_repo_permission_dict['peter_shen'])
    print([ee for ee in user_repo_permission_dict['peter_shen']['r'] if ee not in user_repo_permission_dict['peter_shen']['rw']])
    with open('out.csv', mode='w') as output:
        for user in user_repo_permission_dict:
            output.write(user + ',r/w,' + ','.join(user_repo_permission_dict[user]['rw']) + '\n')
            output.write(user + ',read only,' + ','.join([element for element in user_repo_permission_dict[user]['r'] if element not in user_repo_permission_dict[user]['rw']]) + '\n\n')
