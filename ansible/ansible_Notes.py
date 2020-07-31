"""
    Capture all notes related to Ansible
"""

""" pbs stands for playbooks """


# path of Ansible install files
cd /etc/ansible/

# copy folder to new location
cp -Rf source_dir dest_dir

# change the ownership of folder
chown -Rf vmadmin folder

# change the group of the folder
chgrp -Rf vmadmin folder