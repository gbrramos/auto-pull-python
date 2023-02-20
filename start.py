from git import Repo
import os
import message

try:
    repo = Repo('c:\inetpub\wwwroot\unico')

    ssh_key = os.path.join('c:/Windows/System32/OpenSSH/ssh.exe')

    with repo.git.custom_environment(GIT_SSH=ssh_key):
        repo.remotes.origin.pull()

    message.Mbox('Success', 'Repositórios sincronizados com sucesso', 0)
    
except Exception as e:
    message.Mbox('Error', 'Erro ao sincronizar repositórios', 0)